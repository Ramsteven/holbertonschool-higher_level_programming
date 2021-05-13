$(function () {
    let $gretting = $("#hello")
    $.ajax({
	type: 'GET',
	url: "https://fourtonfish.com/hellosalut/?lang=fr",
	success: function(data) {
	    $gretting.text(data.hello);
	}
    });
});
