// pages/news/news.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        obj:[]
    },
    /**
     * 生命周期函数--监听页面加载
     */
    onLoad(options) {
        this.getObj()
    },
    getObj(){
        wx.request({
          url: 'http://127.0.0.1:3000/homework/news',
          success:res=>{
              this.setData({obj:res.data.data})
              console.log(res.data.data);
          }
        })
    }
})