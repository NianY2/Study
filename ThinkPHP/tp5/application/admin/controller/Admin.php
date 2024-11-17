<?php
namespace app\admin\controller;

use think\Controller;
use think\Db;
use app\admin\model\Admin as AdminModel;

class Admin extends Controller
{
  public function __construct()
  {
    parent::__construct();
    if (!session('username')) {
      return $this->error("No!你没有登入", url("Login/index"));
    }
  }

  public function index()
  {
    $model = new AdminModel();
    // $adminData = $model->all();
    $data = $model->paginate(4);
		$page = $data->render();
    $this->assign('adminData', $data);
    $this->assign('page', $page);
    return $this->fetch("admin-list");
  }
  public function add()
  {
    if (request()->isPost()) {
      $data = input("post.");
      $data["create_time"] = time();
      if($data["password"] != $data["password2"]){
        echo "<script>alert('密码不一致');history.back(-1);</script>";
        exit;
      }
      $data["password"] = md5($data["password"]);
      $model = new AdminModel();
      $res = $model->submit($data);
      if ($res) {
        echo "<script>alert('添加成功');window.parent.location.reload()</script>";
        exit;
      } else {
        return $this->error("操作失败");
      }
    }
    return $this->fetch("admin-add");
  }

}