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
		
		survey.sentences1 = result1;
		survey.sentences2 = result2;
		survey.sentences3 = result3;
		survey.sentences4 = result4;
	}	
}]);