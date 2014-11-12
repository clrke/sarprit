$(document).ready(function() {
	$("#survey-submit").click(function(event) {
		$(this).closest('form').submit();
	});
});