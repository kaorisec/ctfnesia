<?php

class File
{
    public $filename = 'db.txt';
    public $content= 'wasyu';
    public function __destruct()
    {
        file_put_contents($this->filename , $this->content);
    }
}
?>
