<?php
namespace app\admin\model;
use think\Db;
class Login extends \think\Model
{
	
	protected $pk = 'id';
	
	public function checkLogin($username,$password){
		$has = db('admin')->where('username',$username)->find();

		if(empty($has)){
			return false;
		}

		if($has['password'] != md5($password)){
			return false;
		}
		
		session('username',$has['username']);
		session('isLogin',true);
		return true;
	}
	

	/***
	 * 保存当前数据对象  
	 * 含有主键则更新,否则插入
     * @access public
     * @param  array  $data     数据
     * @return bool
	 */
	public function submit($data){
		if(array_key_exists($this->pk,$data) && $data[$this->pk] != ""){
			return $this->allowField(true)->save($data,[$this->pk=>$data[$this->pk]]);
		}else{
			return $this->allowField(true)->save($data);
		}
	}
}