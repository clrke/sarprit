var phraseSplitter = /(([@#][\w]+ *)|([^\.!\?@#]*[\.!\?]* *))/g

angular.module('SarpritApp', [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
})
.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}])
.controller('SarpritCtrl', ['$http', function ($http) {
	var Sarprit = this;
	Sarprit.loading = false;
	Sarprit.prohibited = false;
	Sarprit.overallSentiment = 0;

	Sarprit.analyze = function (review) {
		Sarprit.sentences = []

		var sentences = review.match( phraseSplitter );
		sentences.pop();

		Sarprit.loading = true;
		Sarprit.curLoaded = 0;
		Sarprit.maxLoaded = sentences.length * 3;
		Sarprit.overallSentiment = 0;

		for (var i = 0; i < sentences.length; i++) {
			Sarprit.sentences.push({value: sentences[i]});
		};

		for (var i = 0; i < Sarprit.sentences.length; i++) {
			$http.get('/classify/1/'+i+'/'+encodeURIComponent(Sarprit.sentences[i].value)).success(function (data) {
				Sarprit.sentences[data.id] = data;

				if(Sarprit.sentences[data.id].is_subjective) {
					Sarprit.curLoaded++;

					if (Sarprit.analysisType == 0) {
						$http.get('/classify/2/'+data.id+'/'+encodeURIComponent(Sarprit.sentences[data.id].value)).success(function (data) {
							Sarprit.sentences[data.id].clue = data.clue;
							Sarprit.sentences[data.id].clue_id = data.clue_id;
							Sarprit.sentences[data.id].features2 = data.features;

							Sarprit.curLoaded++;

							$http.get('/classify/3/'+Sarprit.sentences[data.id].clue.toLowerCase()[0]+'/'+data.id+'/'+encodeURIComponent(Sarprit.sentences[data.id].value)).success(function (data) {
								Sarprit.sentences[data.id].rating = data.rating;
								Sarprit.sentences[data.id].features3 = data.features;

								Sarprit.curLoaded++;

								if(Sarprit.curLoaded == Sarprit.maxLoaded) {
									var functional = 0;
									var humanic = 0;
									var mechanic = 0;
									var general = 0;

									var fcount = 0;
									var hcount = 0;
									var mcount = 0;
									var gcount = 0;

									for (var i = 0; i < Sarprit.sentences.length; i++) {
										sentence = Sarprit.sentences[i];

										if(sentence.clue_id == 0) {
											functional += sentence.rating;
											fcount++;
										}
										else if(sentence.clue_id == 1) {
											humanic += sentence.rating;
											hcount++;
										}
										else if(sentence.clue_id == 2) {
											mechanic += sentence.rating;
											mcount++;
										}
										else if(sentence.clue_id == 3) {
											general += sentence.rating;
											gcount++;
										}
									};

									if(fcount == 0)
										fcount = 1;

									if(hcount == 0)
										hcount = 1;

									if(mcount == 0)
										mcount = 1;

									if(gcount == 0)
										gcount = 1;

									functional /= fcount;
									humanic /= hcount;
									mechanic /= mcount;
									general /= gcount;

									$http.get('/classify/4/'+functional+'/'+humanic+'/'+mechanic+'/'+general).success(function (data) {
										Sarprit.overallSentiment = data.rating;
										Sarprit.loading = false;
									});
								}
							});
						});
					}
					else {
						$http.get('/classify/3/n/'+data.id+'/'+encodeURIComponent(Sarprit.sentences[data.id].value)).success(function (data) {
							Sarprit.sentences[data.id].rating = data.rating;
							Sarprit.sentences[data.id].features3 = data.features;

							Sarprit.curLoaded += 2;
							Sarprit.overallSentiment += data.rating;

							if(Sarprit.curLoaded == Sarprit.maxLoaded) {
								Sarprit.overallSentiment = Math.round(Sarprit.overallSentiment / Sarprit.sentences.length);
								Sarprit.loading = false;
							}
						});
					}
				}
				else {
					Sarprit.curLoaded += 3;
					if(Sarprit.curLoaded == Sarprit.maxLoaded) {
						var functional = 0;
						var humanic = 0;
						var mechanic = 0;
						var general = 0;

						for (var i = 0; i < Sarprit.sentences.length; i++) {
							sentence = Sarprit.sentences[i];

							if(sentence.clue_id == 0)
								functional += sentence.rating;
							else if(sentence.clue_id == 1)
								humanic += sentence.rating;
							else if(sentence.clue_id == 2)
								mechanic += sentence.rating;
							else if(sentence.clue_id == 3)
								general += sentence.rating;
						};

						functional /= Sarprit.sentences.length;
						humanic /= Sarprit.sentences.length;
						mechanic /= Sarprit.sentences.length;
						general /= Sarprit.sentences.length;

						if(functional == humanic && humanic == mechanic && mechanic == general && general == 0) {
							functional = humanic = mechanic = general = 3;
						}
						$http.get('/classify/4/'+functional+'/'+humanic+'/'+mechanic+'/'+general).success(function (data) {
							Sarprit.overallSentiment = data.rating;
							Sarprit.loading = false;
						});
					}
				}
			}).error(function (data) {
				Sarprit.loading = false;
				Sarprit.prohibited = true;
				Sarprit.sentences = [];
			});
		};
	}

	Sarprit.range = function(n) {
        return new Array(n);
    };
}])
.controller('SurveyCtrl', ['$http', function ($http) {
	var survey = this;

	survey.review1 = '';
	survey.review2 = '';
	survey.review3 = '';
	survey.review4 = '';

	survey.sentences1 = [];
	survey.sentences2 = [];
	survey.sentences3 = [];
	survey.sentences4 = [];

	survey.overallRating1 = 0;
	survey.overallRating2 = 0;
	survey.overallRating3 = 0;
	survey.overallRating4 = 0;

	var Sentence = function (value) {
		return {
			value: value? value: "Loading...",
			subjective: true,
			rating: 0
		};
	}
	survey.splitReviews = function() {
		var review1 = survey.review1;
		var review2 = survey.review2;
		var review3 = survey.review3? survey.review3 : "";
		var review4 = survey.review4? survey.review4 : "";

		survey.sentences1 = [Sentence()];
		survey.sentences2 = [Sentence()];
		if(review3) survey.sentences3 = [Sentence()];
		if(review4) survey.sentences4 = [Sentence()];

		$http.get('/sentence/preprocess/'+survey.review1)
			.success(function (data) {
				survey.sentences1 = data.sentences;
			})
			.error(function () {
				survey.sentences = [review1];
			});

		$http.get('/sentence/preprocess/'+survey.review2)
			.success(function (data) {
				survey.sentences2 = data.sentences;
			})
			.error(function () {
				survey.sentences = [review2];
			});

		if(review3)
			$http.get('/sentence/preprocess/'+survey.review3)
				.success(function (data) {
					survey.sentences3 = data.sentences;
				})
				.error(function () {
					survey.sentences = [review3];
				});

		if(review4)
			$http.get('/sentence/preprocess/'+survey.review4)
				.success(function (data) {
					survey.sentences4 = data.sentences;
				})
				.error(function () {
					survey.sentences = [review4];
				});
	}

	survey.removeRatings = function (sentence) {
		if(sentence.subjective) {
			delete sentence.clue
			delete sentence.rating
			sentence.rating = 0;
		}
	}

	survey.classify = function () {
		for (var i = 0; i < survey.sentences1.length; i++) {
			sentence = survey.sentences1[i];
			$http.get('/sentence/classify/'+i+'/'+sentence.value)
				.success(function (data) {
					survey.sentences1[data.id] = data.sentence;
				});
		};
		for (var i = 0; i < survey.sentences2.length; i++) {
			sentence = survey.sentences2[i];
			$http.get('/sentence/classify/'+i+'/'+sentence.value)
				.success(function (data) {
					survey.sentences2[data.id] = data.sentence;
				});
		};
		for (var i = 0; i < survey.sentences3.length; i++) {
			sentence = survey.sentences3[i];
			$http.get('/sentence/classify/'+i+'/'+sentence.value)
				.success(function (data) {
					survey.sentences3[data.id] = data.sentence;
				});
		};
		for (var i = 0; i < survey.sentences4.length; i++) {
			sentence = survey.sentences4[i];
			$http.get('/sentence/classify/'+i+'/'+sentence.value)
				.success(function (data) {
					survey.sentences4[data.id] = data.sentence;
				});
		};
	}

	survey.classifyOverallSentiment = function () {
		var f = 0; var f_count = 0;
		var h = 0; var h_count = 0;
		var m = 0; var m_count = 0;
		var g = 0; var g_count = 0;
		for (var i = 0; i < survey.sentences1.length; i++) {
			var sentence = survey.sentences1[i];
			switch(sentence.clue) {
				case 'f': f += sentence.rating; f_count++;
				case 'h': h += sentence.rating; h_count++;
				case 'm': m += sentence.rating; m_count++;
				case 'g': g += sentence.rating; g_count++;
			}
		};
		if(f_count > 0) f = f / f_count;
		if(h_count > 0) h = h / h_count;
		if(m_count > 0) m = m / m_count;
		if(g_count > 0) g = g / g_count;

		$http.get('/review/classify/'+f+'/'+h+'/'+m+'/'+g)
			.success(function (data) {
				survey.overallRating1 = data.overall_sentiment;
			});

		var f = 0; var f_count = 0;
		var h = 0; var h_count = 0;
		var m = 0; var m_count = 0;
		var g = 0; var g_count = 0;
		for (var i = 0; i < survey.sentences2.length; i++) {
			var sentence = survey.sentences2[i];
			switch(sentence.clue) {
				case 'f': f += sentence.rating; f_count++;
				case 'h': h += sentence.rating; h_count++;
				case 'm': m += sentence.rating; m_count++;
				case 'g': g += sentence.rating; g_count++;
			}
		};
		if(f_count > 0) f = f / f_count;
		if(h_count > 0) h = h / h_count;
		if(m_count > 0) m = m / m_count;
		if(g_count > 0) g = g / g_count;

		$http.get('/review/classify/'+f+'/'+h+'/'+m+'/'+g)
			.success(function (data) {
				survey.overallRating2 = data.overall_sentiment;
			});

		if(survey.review3) {
			var f = 0; var f_count = 0;
			var h = 0; var h_count = 0;
			var m = 0; var m_count = 0;
			var g = 0; var g_count = 0;
			for (var i = 0; i < survey.sentences3.length; i++) {
				var sentence = survey.sentences3[i];
				switch(sentence.clue) {
					case 'f': f += sentence.rating; f_count++;
					case 'h': h += sentence.rating; h_count++;
					case 'm': m += sentence.rating; m_count++;
					case 'g': g += sentence.rating; g_count++;
				}
			};
			if(f_count > 0) f = f / f_count;
			if(h_count > 0) h = h / h_count;
			if(m_count > 0) m = m / m_count;
			if(g_count > 0) g = g / g_count;

			$http.get('/review/classify/'+f+'/'+h+'/'+m+'/'+g)
				.success(function (data) {
					survey.overallRating3 = data.overall_sentiment;
				});
		}

		if(survey.review4) {
			var f = 0; var f_count = 0;
			var h = 0; var h_count = 0;
			var m = 0; var m_count = 0;
			var g = 0; var g_count = 0;
			for (var i = 0; i < survey.sentences4.length; i++) {
				var sentence = survey.sentences4[i];
				switch(sentence.clue) {
					case 'f': f += sentence.rating; f_count++;
					case 'h': h += sentence.rating; h_count++;
					case 'm': m += sentence.rating; m_count++;
					case 'g': g += sentence.rating; g_count++;
				}
			};
			if(f_count > 0) f = f / f_count;
			if(h_count > 0) h = h / h_count;
			if(m_count > 0) m = m / m_count;
			if(g_count > 0) g = g / g_count;

			$http.get('/review/classify/'+f+'/'+h+'/'+m+'/'+g)
				.success(function (data) {
					survey.overallRating4 = data.overall_sentiment;
				});
		}

	}

	survey.step2ok = function () {
		for (var i = 0; i < survey.sentences1.length; i++) {
			sentence = survey.sentences1[i];
			if( ! sentence.value)
				return false;
		};

		for (var i = 0; i < survey.sentences2.length; i++) {
			sentence = survey.sentences2[i];
			if( ! sentence.value)
				return false;
		};

		for (var i = 0; i < survey.sentences3.length; i++) {
			sentence = survey.sentences3[i];
			if( ! sentence.value)
				return false;
		};

		for (var i = 0; i < survey.sentences4.length; i++) {
			sentence = survey.sentences4[i];
			if( ! sentence.value)
				return false;
		};

		return true;
	}
	survey.step3ok = function () {
		for (var i = 0; i < survey.sentences1.length; i++) {
			sentence = survey.sentences1[i];
			if(sentence.subjective && (!sentence.rating || !sentence.clue))
				return false;
		};

		for (var i = 0; i < survey.sentences2.length; i++) {
			sentence = survey.sentences2[i];
			if(sentence.subjective && (!sentence.rating || !sentence.clue))
				return false;
		};

		for (var i = 0; i < survey.sentences3.length; i++) {
			sentence = survey.sentences3[i];
			if(sentence.subjective && (!sentence.rating || !sentence.clue))
				return false;
		};

		for (var i = 0; i < survey.sentences4.length; i++) {
			sentence = survey.sentences4[i];
			if(sentence.subjective && (!sentence.rating || !sentence.clue))
				return false;
		};

		return true;
	}

	survey.step4ok = function () {

		if(survey.review1 && !survey.overallRating1)
			return false;
		if(survey.review2 && !survey.overallRating2)
			return false;
		if(survey.review3 && !survey.overallRating3)
			return false;
		if(survey.review4 && !survey.overallRating4)
			return false;

		return true;
	}
}])
.controller('StudentsCtrl', ['$http', '$interval', function ($http, $interval) {
	var students = this;
	students.value = [];

	students.refresh = function () {
		$http.get('/admin/data').success(function (data) {
			for (var i = 0; i < data.length; i++) {
				if(data[i].current) {
					students.value = data[i].students;
					break;
				}
			};
		});
	}

	$interval( function () {
		students.refresh();
	}, 10000);

	students.refresh();
}])
.controller('SystemCtrl', ['$http', function ($http) {
	var system = this;

	$http.get("api/data").success( function (data) {
		system.reviews = data.reviews;
		system.sentences = data.sentences;
	});
}])
.controller('TwitterCtrl', ['$http', function ($http) {
	var twitter = this;
}])
.controller('ReviewsCtrl', ['$http', function ($http) {
	var Review = this;
	Review.save = function (review) {
		$http.get("/review/save/"+review.id+"/"+review.flag);
	}
	Review.range = function(n) {
        return new Array(n);
    };
}]);
