// index.js
Page({
    data:{
        obj:[]
    },
    onLoad(){
        wx.request({
          url: 'http://172.26.43.142:3000/v1/music',
          success:res=>{
              console.log(res.data.data);
              this.setData({obj:res.data.data})
          },
          fail(){
              wx.showToast({
                title: '请求失败',
                icon:"error"
              })
          }
        })
    },

    
})
