// pages/newsInfo/newsInfo.js
Page({
    /**
     * 页面的初始数据
     */
    data: {
        obj:{}
    },
    onLoad(options) {
        this.getObj(options.id)
    },
    getObj(id){
        wx.request({
          url: `http://127.0.0.1:3000/homework/news/${id}`,
          success:res=>{
              console.log(res.data.data);
              this.setData({obj:res.data.data})
          }
        })
    }
})