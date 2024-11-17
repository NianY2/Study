<?php
namespace app\admin\controller;

use think\Controller;
use think\Db;
use app\admin\model\CategoryModel as CategoryModel;

class Category extends Controller
{
    public function __construct(){
        parent::__construct();
        if(!session('username')){
            return $this->error("No!你没有登入",url("Login/index"));
        }
    }

    public function index(){
        $model = new CategoryModel();
        $data = $model->all();
        $data = $this->getTree($data);
        $this->assign('data', $data);
        return $this->fetch("cate");
    }
    public function getTree($array, $pid = 0, $level = 0)
    {
        //声明静态数组,避免递归调用时,多次声明导致数组覆盖
        static $list = [];
        foreach ($array as $key => $value) {
            //第一次遍历,找到父节点为根节点的节点 也就是pid=0的节点
            if ($value['pid'] == $pid) {
                //父节点为根节点的节点,级别为0，也就是第一级
                $value['level'] = $level;
                $str1 = "";
                for ($i=0; $i < $level; $i++) { 
                    $str1 =  $str1."&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
                }
                $value['sp'] = $str1;
                
                //把数组放到list中
                $list[] = $value;
                //把这个节点从数组中移除,减少后续递归消耗
                unset($array[$key]);
                //开始递归,查找父ID为该节点ID的节点,级别则为原级别+1
                $this->getTree($array, $value['cid'], $level + 1);
            }
        }
        return $list;
    }
  
}