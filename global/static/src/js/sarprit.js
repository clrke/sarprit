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
}]);