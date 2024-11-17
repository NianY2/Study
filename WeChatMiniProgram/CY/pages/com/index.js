// pages/com/index.js
Page({
    data: {
        msg: ""
    },
    btn: function (e) {
        if (!isNaN(Number(e.target.dataset.val))) {
            this.setData({
                msg: this.data.msg += e.target.dataset.val
            })
        } else {
            if (isNaN(this.data.msg.substr(this.data.msg.length - 1, 1))) {
                if (this.data.msg.substr(this.data.msg.length - 1, 1) == e.target.dataset.val) {
                    return;
                }else{
                    this.setData({msg: this.data.msg.substr(0, this.data.msg.length - 1)})
                    this.setData({msg: this.data.msg += e.target.dataset.val})
                }
            } else{
                if (e.target.dataset.val == "DEL") {
                    this.setData({msg: this.data.msg.substr(0, this.data.msg.length - 1)})
                }else if(e.target.dataset.val == "C"){
                    this.setData({msg: ""})
                }else{
                    this.data.msg += e.target.dataset.val
                }
            }
        }
            
        //     else if (e.target.dataset.val == "C") {
        //         this.setData({
        //             msg: ""
        //         })
        //     } else if (e.target.dataset.val == "DEL") {
        //         this.setData({
        //             msg: this.data.msg.substr(0, this.data.msg.length - 1)
        //         })
        //     } else {
        //         this.setData({
        //             msg: this.data.msg += e.target.dataset.val
        //         })
        //     }
        // }
        // if(isNaN(Number(e.target.dataset.val)) && !isNaN(Number())){
        //     if(e.target.dataset.val == "C"){
        //         this.setData({msg:""})
        //         return;
        //     }else if(e.target.dataset.val == "DEL"){
        //         this.setData({msg:""})
        //         return;
        //     }
        //     this.setData({msg:this.data.msg+=e.target.dataset.val})
        // }else if(!isNaN(Number(e.target.dataset.val))){

        // }
        // if(e.target.dataset.val == "C"){
        //     this.setData({msg:""})
        // }else if(e.target.dataset.val == "."){
        //     if(this.data.msg.substr(this.data.msg.length-1,1)!="."){
        //         this.setData({msg:this.data.msg+="."})
        //     }
        // }else if(isNaN(Number(e.target.dataset.val))){
        //     this.setData({msg:this.data.msg+=" "+e.target.dataset.val+" "})
        // }else{
        //     this.setData({msg:this.data.msg+=e.target.dataset.val})
        // }
    }
})