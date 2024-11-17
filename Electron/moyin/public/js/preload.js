// 注入的脚本

// const { globalShortcut, screen } = require("electron");
// const {  } = require("electron");

const btn = document.createElement("button");
btn.innerText = "评价";
// 设置按钮的样式：固定定位，居中对齐
btn.style.position = "fixed";
btn.style.left = "0";
btn.style.top = "0";
btn.style.zIndex = 2000;
btn.style.backgroundColor = "red"; // 设置背景颜色
btn.style.color = "white"; // 设置文本颜色
btn.style.border = "none"; // 取消边框
btn.style.padding = "10px"; // 设置内边距
btn.style.fontSize = "16px"; // 设置字体大小
// 将按钮添加到 body 元素中
document.body.appendChild(btn);
btn.addEventListener("mousedown", function (event) {
  checkeds(0);
});
function checkeds(i){
  // setTimeout(checkeds, 4000);
  let pjfs = document.getElementsByClassName("radio-pjf");
  for (let index = 0; index < pjfs.length; index++) {
    if (index % 5 == 0) {
      pjfs[index].checked = true;
    }
  }
  window.scrollTo(0, document.documentElement.scrollHeight);
  document.getElementsByClassName("form-control")[0].innerText = "挺好的";
  setTimeout(()=>{
    document.getElementById("btn_xspj_bc").click();
    document.getElementById("btn_ok").click();
    i++
    setItem(i);
  },2000)
  
}
function setItem(i){
  var s =  document.getElementsByClassName("ui-widget-content jqgrow ui-row-ltr");
  if(i < s.length){
    s[i].click()
    setTimeout(()=>{checkeds(i)}, 500);
  }else{
    alert("suc")
  }
}