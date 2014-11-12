angular.module('SarpritApp', [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
})
.controller('SurveyCtrl', ['$http', function ($http) {
	var survey = this;
	
	survey.splitReviews = function() {
		var sentence1 = survey.review1;
		var sentence2 = survey.review2;
		var sentence3 = survey.review3? survey.review3 : "";
		var sentence4 = survey.review4? survey.review4 : "";

		var result1 = sentence1.match( /((#[\w^#]+ *)|([^\.!\?]+[\.!\?]* *))/g );
		var result2 = sentence2.match( /((#[\w^#]+ *)|([^\.!\?]+[\.!\?]* *))/g );
		var result3 = sentence3.match( /((#[\w^#]+ *)|([^\.!\?]+[\.!\?]* *))/g );
		var result4 = sentence4.match( /((#[\w^#]+ *)|([^\.!\?]+[\.!\?]* *))/g );
		
		survey.sentences1 = [];
		survey.sentences2 = [];
		survey.sentences3 = [];
		survey.sentences4 = [];

		for (var i = 0; i < result1.length; i++) {
			survey.sentences1.push({value: result1[i], subjective: true});
		}
		for (var i = 0; i < result2.length; i++) {
			survey.sentences2.push({value: result2[i], subjective: true});
		}
		for (var i = 0; i < result3.length; i++) {
			survey.sentences3.push({value: result3[i], subjective: true});
		}
		for (var i = 0; i < result4.length; i++) {
			survey.sentences4.push({value: result4[i], subjective: true});
		}
	}

	survey.removeRatings = function (sentence) {
		if(sentence.subjective) {
			delete sentence.rating
			delete sentence.clue
		}
	}
}]);