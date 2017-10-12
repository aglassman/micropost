$.ajaxSetup({ 
	 beforeSend: function(xhr, settings) {
	     function getCookie(name) {
	         var cookieValue = null;
	         if (document.cookie && document.cookie != '') {
	             var cookies = document.cookie.split(';');
	             for (var i = 0; i < cookies.length; i++) {
	                 var cookie = jQuery.trim(cookies[i]);
	                 // Does this cookie string begin with the name we want?
	             if (cookie.substring(0, name.length + 1) == (name + '=')) {
	                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	                 break;
	             }
	         }
	     }
	     return cookieValue;
	     }
	     if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
	         // Only send the token to relative URLs i.e. locally.
	         xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
	     }
	 } 
});

$( "#dialog-form" ).dialog({
	autoOpen: false,
	height: 350,
	width: 500,
	modal: true,
	buttons: {
		"Report": function() {
			var bug_data = {};
			bug_data['bug_description'] = $("#bug_description").val();   
			
			$.ajax({
			    type : 'POST',
			    data : bug_data,
			    cache : false,
			    url : '/micropost/create/',
			    dataType : 'html',
			    success : function(){
			        //if HTTP response is ok, diplay data
			        //else if HTTP response gets 403 error, display some other message
			        $( "#dialog-form" ).dialog( "close" );
			        alert("success")
			    },
			    error: function(){
			        // Handle your error here
			        $( "#dialog-form" ).dialog( "close" );
			        alert("failed");
			    }
			});
			
		},
		Cancel: function() {
			$( this ).dialog( "close" );
		}
	},
	close: function() {
	}
});

$( "#report-bug" )
	.button()
	.click(function() {
		$( "#dialog-form" ).dialog( "open" );
});