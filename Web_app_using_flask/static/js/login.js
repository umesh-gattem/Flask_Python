	$(document).ready(function() {
	alert("hai")
		$('#signin').click(function() {
			var username = $('#username').val();
			var password = $('#password').val();
			$.ajax({
				type : 'post',
				data : {
					username : username,
					password : password,
				},
				url : '../login',
				success : function(res) {
					if(res=="Successful!!"){
					}
					else{
						alert("Invalid Credentials!!!!!!");
					}
				},
				error : function(res) {
					alert(res);
				}
			});
		});
	});
