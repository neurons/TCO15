from django.http import HttpResponse
from win import *

PAGE = """
<title>GameTime</title>
<style>
  body {
    padding-top: 120px;
    padding-bottom: 40px;
    background-color: #eee;
  
  }
  .btn 
  {
   outline:0;
   border:none;
   border-top:none;
   border-bottom:none;
   border-left:none;
   border-right:none;
   box-shadow:inset 2px -3px rgba(0,0,0,0.15);
  }
  .btn:focus
  {
   outline:0;
   -webkit-outline:0;
   -moz-outline:0;
  }
  .fullscreen_bg {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background-size: cover;
    background-position: 50% 50%;
    background-image: url('http://i.imgur.com/RnZaR6o.jpg');
    background-repeat:repeat;
  }
  .form-signin {
    max-width: 280px;
    padding: 15px;
    margin: 0 auto;
      margin-top:50px;
  }
  .form-signin .form-signin-heading, .form-signin {
    margin-bottom: 10px;
  }
  .form-signin .form-control {
    position: relative;
    font-size: 16px;
    height: auto;
    padding: 10px;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
  }
  .form-signin .form-control:focus {
    z-index: 2;
  }
  .form-signin input[type="text"] {
    margin-bottom: -1px;
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
    border-top-style: solid;
    border-right-style: solid;
    border-bottom-style: none;
    border-left-style: solid;
    border-color: #000;
  }
  .form-signin input[type="password"] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
    border-top-style: none;
    border-right-style: solid;
    border-bottom-style: solid;
    border-left-style: solid;
    border-color: rgb(0,0,0);
    border-top:1px solid rgba(0,0,0,0.08);
  }
  .form-signin-heading {
    color: #fff;
    text-align: center;
    text-shadow: 0 2px 2px rgba(0,0,0,0.5);
  }
</style>

<div id="fullscreen_bg" class="fullscreen_bg"/>

<link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css">

<script src="https://code.jquery.com/jquery-2.1.4.min.js"></script>
<link rel="stylesheet" href="view.css">

<script>
$(document).ready(function(){
  $('#submit_all').on('click',function(){
    $.get("/send_sms_django/",{
      'phonenum': $('#phonenumber').val()
    });
  });
});
</script>


<div class="container">

	<div class="form-signin">
		<h1 style='color:rgb(252,250,104);margin-bottom:40px' class="form-signin-heading text-muted">GameTime</h1>
		<input id='phonenumber' style='margin-bottom:10px' type="text" class="form-control" placeholder="Phone Number" required="" autofocus="">
		<input style='margin-bottom:10px' type="text" class="form-control" placeholder="City" required="">
		<button id='submit_all' class="btn btn-lg btn-primary btn-block">
			Get events!
		</button>
	</div>
</div>
"""

def homepage(request):
  return HttpResponse(PAGE)

def send_sms_django(request):
  phone = request.GET.get('phonenum','')
  print phone
  send_sms_to(phone)
  return HttpResponse('')
