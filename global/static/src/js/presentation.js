angular.module('PresentationApp', [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
})
.controller('Presentation1Ctrl', function () {
	var Presentation = this;
});

$(document).ready(function () {
	var top = $('.scroll-follower').offset().top;

	function goWithTheFlow () {
		if($(document).width() > 992) {
			$('.scroll-follower').css('position','');
			top = $('.scroll-follower').offset().top;
			$('.scroll-follower').css('position','absolute');
			$('.scroll-follower').css('top',Math.max(top, $(document).scrollTop()-10)-237);
		}
	}

	goWithTheFlow();
	$(document).scroll(goWithTheFlow);
});
