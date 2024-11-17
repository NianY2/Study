<?php
namespace app\Goods\model;

class Goods extends \think\Model
{
	
	protected $table = 'tp5_tb_goods';
	protected $pk = 'id';
	
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