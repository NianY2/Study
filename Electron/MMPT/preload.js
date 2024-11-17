// 注入的脚本


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
  console.log("aaa");
});