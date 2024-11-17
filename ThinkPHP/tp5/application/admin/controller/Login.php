<?php
namespace app\admin\controller;

use think\Controller;
use think\Db;
use app\admin\model\Login as LoginModel;

class Login extends Controller
{
    public function index(){
        return view('login');
    }

    public function login(){
        $data = input("post.");
        if(empty($data)){
            $this->error("用户名或密码不能为空");
        }
        $model = new LoginModel();
        $res = $model->checkLogin($data['username'],$data["password"]);
        if($res){
            $this->success('登入成功',"Index/index");
        }else{
            $this->error("账号或密码错误");
        }
    }
}
