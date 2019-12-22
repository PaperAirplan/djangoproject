$(document).ready(function(){
	$('td:nth-child(7),th:nth-child(7)').hide();
	$('#btnShow').click(function() {
	$('td:nth-child(7),th:nth-child(7)').show();
	$('forms')[0].reset();
	});

$(function () {
        $('#datetimepicker1').datetimepicker({
			locale: 'ru',
            viewMode: 'years',
			format: 'YYYY'
    });
});

});
