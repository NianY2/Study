// pages/from/index.js
Page({
    data: {
        obj:null
    },
    onLoad() {
        wx.request({
            url: 'http://172.26.43.142:3000/v1/form',
            success: (res) => {
                this.setData({obj:res.data.data})
            }
        })
    },
    submit: (e) => {
        wx.request({
            url: 'http://172.26.43.142:3000/v1/form',
            method: "POST",
            data: e.detail.value,
            success: (res) => {
                console.log(res);
            }
        })
    }
})