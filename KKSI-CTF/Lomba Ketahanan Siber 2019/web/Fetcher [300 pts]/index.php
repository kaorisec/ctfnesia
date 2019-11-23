<?php

class Fetcher {
    private function protocol_allowed($url) {
        return (strpos($url, 'http://') === 0) || (strpos($url, 'https://') === 0);
    }

    private function not_contains_blacklist($url) {
        $blacklist = array(
            '127.',
            '192.',
            '172.',
            '10.',
            'localhost',
            '0.',
            '0/',
            'file://',
        );
        foreach($blacklist as $forbidden) {
            if (stripos($url, $forbidden) !== false) {
                return false;
            }
        }
        return true;
    }

    public function fetch($url) {
        $url = escapeshellcmd(trim($url));
        if ($this->protocol_allowed($url) && $this->not_contains_blacklist($url)) {
            return shell_exec("curl $url");
        }
        return "";
    }
}

$fetcher = new Fetcher;
echo $fetcher->fetch($_GET['url']);