<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Data Provinsi di Indonesia</title>
</head>
<body>
    <h1>Cari Data Provinsi di Indonesia</h1>
    <form action="" method="POST">
    Untuk Alasan Keamanan, kami memfilter beberapa karakter<br>
        Nama Provinsi : <input type="text" name="nama"><br>
        <input type="submit" name="submit" value="Cari">
    </form>
</body>
</html>
<pre>
<?php

error_reporting(0);

$cari = "";

if (array_key_exists("nama", $_REQUEST))
{
        $cari = $_REQUEST["nama"];
}
if ($cari != "")
{
        if (preg_match('/[;|&]/', $cari)) {
                print "Mengandung karakter ilegal";
        }
        else
        {
                echo passthru("grep -i $cari data.txt");
        }
}

?>
</pre>