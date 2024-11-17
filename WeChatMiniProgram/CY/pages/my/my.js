// pages/my/my.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        foods:["红烧🐟","清蒸鱼","油麦菜","腊肠"],
        obj:{},
        list_obj:[],
        select:null,

        shop:[
            {id:1,name:"清蒸鱼"},
            {id:2,name:"油麦菜"},
            {id:3,name:"腊肠",}
        ],
        my_shop:[

        ]
    },

    onLoad(options) {
        this.getObj()
    },
    async getShopNum(e){

    },
    async getObj(){
        this.setData({obj:{name:"CY",phone:"16607512918",class:"21软件1班"}}) 
    },
    async getListObj(){
        
    },
    setSelect(e){
        
        let l = []
        l.push({id:"1"})
        l.push({id:"2"})
        console.log(l);

        this.setData({select:e.target.dataset.food})
        wx.showToast({
          title: e.target.dataset.food,
          icon:"none"
        })
    },
    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady() {

    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow() {

    },

    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide() {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload() {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh() {

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom() {

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage() {

    }
})