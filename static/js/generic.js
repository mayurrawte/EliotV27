$(document).ready(function()
{
    console.log("Js loaded");
	$('#burgerMenu').on('click',function()
	{
		$('#burgerMenu').toggleClass('burgerActive');
		$('#side-bar').toggleClass('side-bar-active');
	});

	$('#staff-login').on('click',function(event)
	{
	    event.preventDefault();
        var csrftoken = getCookie('csrftoken');
        var username = document.getElementById('staffemail').value;
        var password = document.getElementById('staffpassword').value;
		$.ajax({
			type: "POST",
			url: "/stafflogin/",
			data : {
			    csrfmiddlewaretoken : csrftoken,
                username: username,
                password: password
            },
			success : function(data)
			{
				if(data == "OK")
                {
                    window.location = "/staff";
                }
                else
                {
                    showdialog(data);
                }

			},
			error : function(xhr,errmsg,err)
			{
				alert(xhr.status + ": " + xhr.responseText);
			}

		});
	});

	$('#add-user').on('click',function(event)
    {
        event.preventDefault();
        var csrf = getCookie('csrftoken');
        var firstname = document.getElementById('s-firstname').value;
        var lastname = document.getElementById('s-lastname').value;
        var email = document.getElementById('s-email').value;
        var mob = document.getElementById('mob-no').value;
        var aadhar = document.getElementById('aadhar-id').value;
        var address = document.getElementById('address').value;
        $.ajax({
            type: "POST",
            url: "/adduser/",
            data: {
                csrfmiddlewaretoken: csrf,
                firstname: firstname,
                lastname : lastname,
                email : email,
                mobile : mob,
                aadhar : aadhar,
                address : address
            },
            success : function(data)
            {
                if(data == "OK")
                {
                    showdialog('User Added');
                }
                else
                {
                    showdialog(data);
                }
            },

            error : function(xhr,errmsg,err)
			{
				alert(xhr.status + ": " + xhr.responseText);
			}
        });

       console.log(csrf + firstname +lastname );
    });

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

    $('#u-login').on('click',function(event)
    {
        event.preventDefault();
        var email = document.getElementById('u-email').value;
        var csrf = getCookie('csrftoken');
        var password = document.getElementById('u-password').value;
        console.log(email + password);
        $.ajax({
            type : 'POST',
            url  : '/userlogin/',
            data : {
                csrfmiddlewaretoken : csrf,
                email : email,
                password : password
            },
            success : function(data)
            {
                console.log(data);
                if(data == "OK")
                {
                    window.location = "/dashboard/"
                }
            },
            error : function (xhr,errmsg,err)
			{
				alert(xhr.status + ": " + xhr.responseText);
			}
        })
    });

    $('#user-logout').on('click',function()
    {
        console.log("Triggered");
        var csrf = getCookie('csrftoken');
        $.ajax({
           type : "POST",
            url : "/userlogout/",
            data : {
               csrfmiddlewaretoken : csrf
            },
            success : function(data)
            {
                if(data == "OK")
                {
                    window.location = "/";
                }
            },
            error : function (xhr,errmsg,err)
			{
				alert(xhr.status + ": " + xhr.responseText);
			}
        });
    });


    $('.pins').on('click',function(event)
    {
        if (event.target.tagName.toUpperCase() == "SPAN") {
            return;
        }
        var csrf = getCookie('csrftoken');
        var target = $(this).attr('pin');
        var status = $('#pin'+target).is(":checked");
        $.ajax({
            type : "POST",
            url  : "/mqttclient/",
            data : {
                csrfmiddlewaretoken : csrf,
                pin : target,
                status: status
            },
            success : function(data)
            {
                showdialog(data);
            },
            error : function (xhr,errmsg,err)
			{
				alert(xhr.status + ": " + xhr.responseText);
			}

        });
    });

    $('#u-proceed').on('click',function(event)
    {
        event.preventDefault();
        var device = document.getElementById('u-device-id').value;
        var amount = document.getElementById('u-recharge-amount').value;
        var username = document.getElementById('u-username').value;
        var csrf = getCookie('csrftoken');

        $.ajax({
            type: 'POST',
            url: '/recharge-proceed/',
            data : {
                csrfmiddlewaretoken :csrf,
                device : device,
                username  : username,
                amount : amount
            },
            success : function(data)
            {
                showdialog(JSON.stringify(data));
            },
            error : function (xhr,errmsg,err)
			{
				alert(xhr.status + ": " + xhr.responseText);
			}
        })
    });


    function showdialog(message)
    {
        var msg ="<p>"+message+"</p>";
        document.getElementById('notification-content').innerHTML = msg;
        document.getElementById('notification-trigger').click();
    }

    if(document.getElementById('graph')!= null)
    {
        getgraph();
    }
    function getgraph()
    {
        alert('clocked');
        var device = document.getElementById('device_id').innerHTML;
        var csrf = getCookie('csrftoken');
        alert(device);
        $.ajax({
            type: "POST",
            url: "/graphvalues/",
            data:{
                device_id : device,
                csrfmiddlewaretoken :csrf,

            },
            success:function(data)
            {
                showdialog(data);
            },
            error : function (xhr,errmsg,err)
			{
				alert(xhr.status + ": " + xhr.responseText);
			}
        });
    }



});
