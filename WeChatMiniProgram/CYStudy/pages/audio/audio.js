// pages/audio/audio.js
Page({
    innerAudioContext: wx.createInnerAudioContext({}),
    data: {
        num: 0,
        num1: 0,
        num2: 0,
        obj: {},
        isPlay: true,
        url: "http://172.26.43.142:3000/",
    },
    onLoad(options) {
        this.getObj(options.id)
        this.innerAudioContext.onWaiting(() => {
            this.innerAudioContext.pause()
            this.setData({
                isPlay: false
            })
        })
        this.innerAudioContext.onCanplay(() => {
            this.innerAudioContext.play()
            this.setData({
                isPlay: true
            })
        })
        this.innerAudioContext.onTimeUpdate(() => {
            this.setData({
                num1: this.innerAudioContext.duration
            })
            this.setData({
                num2: this.innerAudioContext.currentTime
            })
            this.setData({
                num: Math.ceil(this.data.num2 / this.data.num1 * 100)
            })
        })
    },
    getObj(id) {
        wx.request({
            url: 'http://172.26.43.142:3000/v1/music/' + id,
            success: res => {
                this.setData({
                    obj: res.data.data
                })
                console.log(this.data.obj);
                this.innerAudioContext.src = this.data.url + this.data.obj.src
                this.innerAudioContext.play()


            },
            fail() {
                wx.showToast({
                    title: '请求失败',
                    icon: "error"
                })
            }
        })
    },
    upt() {
        this.setData({
            isPlay: !this.data.isPlay
        })
        if (this.data.isPlay) {
            this.innerAudioContext.play() // 播放
        } else {
            this.innerAudioContext.pause() // 暂停
        }
    },
    listener(res) {
        console.log(res);
    }
})