<?php
namespace app\goods\controller;

use think\Controller;
use think\Db;
use app\Goods\model\Goods as GoodsModel;

class Goods extends Controller
{

	public function list(){
		
		$goods_model = new GoodsModel();
		$data = $goods_model->paginate(5);
		$page = $data->render();
		// 模板变量赋值
		$this->assign('data', $data);
		$this->assign('page', $page);
		return $this->fetch();
	}

	public function add(){
		return $this->fetch();
	}
	public function edit(){
		if(request()->isGet()){
			$data=input('get.');
			$model = new GoodsModel();
			$obj = $model::get($data['id']);
			$this->assign('data',$obj);
			return $this->fetch();
		}
	}
	public function del($id){
		if(request()->isGet()){
			// $data=input('get.');
			// $id=$data['id'];
			$model = new GoodsModel();
			$obj = $model::get($id);
			if($obj->delete()){
				return $this->success("操作成功");
			}else{
				return $this->error("操作失败");
			}
		}
	}

	public function save(){
		if(request()->isPost()){
			// $data=input('post.');
			$goods_model = new GoodsModel();
			if($goods_model->submit($_POST)){
				return $this->success("操作成功","goods/list");
			}else{
				return $this->error("操作失败");
			}
		}elseif(request()->isGet()){
			return $this->error("错误请求Get");
		}
	}	
}
