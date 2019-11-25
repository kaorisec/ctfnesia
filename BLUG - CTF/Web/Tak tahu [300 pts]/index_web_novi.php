<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Jekyll v3.8.5">
    <title>My Awesome Website</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/4.3/examples/cover/">

    <!-- Bootstrap core CSS -->
<link href="https://getbootstrap.com/docs/4.3/dist/css/bootstrap.min.css" rel="stylesheet">

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
    <link href="cover.css" rel="stylesheet">
  </head>
  <body class="text-center">
    <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
  <header class="masthead mb-auto">
    <div class="inner">
      <h3 class="masthead-brand">My Site</h3>
      <nav class="nav nav-masthead justify-content-center">
        <a class="nav-link active" href="#">Home</a>
        <a class="nav-link" href="?page=about">About</a>
        <a class="nav-link" href="?page=contact">Contact</a>
        <a class="nav-link" href="?page=flag">Flag</a>
      </nav>
    </div>
  </header>

  <?php
  
  if(isset($_GET['page']))
  {
  	include $_GET['page'].'.php';
  }
  else{

  echo '
  <main role="main" class="inner cover">
    <h1 class="cover-heading">Selamat Datang di website saya</h1>
    <p class="lead">Cuma simple blog kok</p>
    <p class="lead">
      <a href="#" class="btn btn-lg btn-secondary">Kenalan skuy</a>
    </p>
  </main>
  ';
	}
  ?>

  <footer class="mastfoot mt-auto">
    <div class="inner">
      <p>Hacker 1337 - 2019</p>
    </div>
  </footer>
</div>
</body>
</html>