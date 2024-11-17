<?php
namespace app\admin\controller;

use think\Controller;
use think\Db;


class Index extends Controller
{
    public function __construct(){
        parent::__construct();
        if(!session('username')){
            return $this->error("No!你没有登入",url("Login/index"));
        }
    }

    public function index(){
        $this->assign('username',session('username'));
        return $this->fetch("index");
    }
    public function welcome(){
        $this->assign('username',session('username'));
        return $this->fetch("welcome");
    }
}
