
<?php

error_reporting(0);

$rahasia = "-- MAU TAU AJA --";

  if(isset($_GET["password"])){
    $password = $_GET["password"];
      if(strcmp($password, $secret) == 0){
        echo "<h1>Flag nya : $rahasia</h1>";
      }else{
        echo "<script>alert('Password Salah')</script>";
      }
    }

?>
<!doctype html>
<html lang="en">

<meta http-equiv="content-type" content="text/html;charset=utf-8" />
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Jekyll v3.8.5">
    <title>Login Bang</title>

    <link rel="canonical" href="index.html">

    <!-- Bootstrap core CSS -->
<link href="https://getbootstrap.com/docs/4.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">


    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>
    <!-- Custom styles for this template -->
    <link href="signin.css" rel="stylesheet">
  </head>
  <body class="text-center">
    <form class="form-signin" method="GET" action="">
  <img class="mb-4" src="http://ctf.batamlinux.com/files/f7310947ca12961899ca460bd835fbac/logo-blug-stroke.png" alt="" width="150" height="150">
  <h1 class="h3 mb-3 font-weight-normal">Login Dulu</h1>
  <label for="inputPassword" class="sr-only">Password</label>
  <input type="password" id="inputPassword" class="form-control" placeholder="Password" required name="password">
  <input class="btn btn-lg btn-primary btn-block" type="submit" value="Login">
  <p class="mt-5 mb-3 text-muted">&copy; 2019</p>
</form>
</body>

</html>
