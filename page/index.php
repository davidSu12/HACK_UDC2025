<?php

$request_uri = $_SERVER['REQUEST_URI'];

$request_uri = parse_url($request_uri, PHP_URL_PATH);


switch ($request_uri) {
    case '/':
        include './page/login/login.html';
        break;

    case '/register':
        include './page/register/register.html';
        break;

}