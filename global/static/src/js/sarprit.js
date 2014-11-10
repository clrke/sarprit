angular.module('SarpritApp', [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
})
.controller('SurveyCtrl', ['$http', function ($http) {
	var survey = this;
	survey.title = "Hello World";
	survey.messages = [];

	$http.get('/test').success(function(data) {
		survey.messages = data;
	});

	function hasReview() {
		while((restaurantReview1.length > 0) && (restaurantReview2.length > 0)) {
			return true;
		};
	}

	var sentence1 = "Sarap talaga ng sisig! Kaya nga lang pagkalabas mo, sisig ka na rin! #sisigLord";
	var sentence2 = "Punta ulit tayo bukas. Pogi talaga ni kuyang waiter! #panalo";

	var result1 = sentence1.match( /((#[\w^#]+ *)|([^\.!\?]+[\.!\?]* *))/g );
	var result2 = sentence2.match( /((#[\w^#]+ *)|([^\.!\?]+[\.!\?]* *))/g );
	
	alert(result2);
	survey.sentences = result2;
}]);