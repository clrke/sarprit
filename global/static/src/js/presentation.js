angular.module('PresentationApp', [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
})
.controller('Presentation1Ctrl', function () {
	var Presentation = this;
});