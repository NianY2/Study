// index.js
Page({
    data:{
        percent_num:50,
        obj:{"name":"CY"},
        num1:null,
        num2:null,
        res:""
    },
    async getObj(){
        this.setData({obj:{"name":"CY222"}})
    },
    // 1
    getMaxnum(e){
        console.log(e.currentTarget.dataset.data);
        
        if(this.data.num1 > this.data.num2){
            this.setData({res:"第一个数字大"})
        }else if(this.data.num1 < this.data.num2){
            this.setData({res:"第二个数字大"})
        }else{
            this.setData({res:"相等"})
        }
    }
})
