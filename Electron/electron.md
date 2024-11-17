# Electron

## .npmrc

安装`electron`依赖经常会不成功
在项目目录下创建`.npmrc`文件，设置镜像地址

```javascript
registry=https://registry.npm.taobao.org
electron-mirror=https://npm.taobao.org/mirrors/electron/
```

## 热更新/热加载

### 方案一

1. 安装：`npm install electron-reloader --save-dev`
2. 在主进程 js 文件

   ```javascript
   try {
     require("electron-reloader")(module);
   } catch (_) {}
   ```

3. 重启

### 方案二

1. 安装：`npm i nodemon --D`
2. 修改`scripts`：`"start": "nodemon --watch index.js --exec electron ."`
3. 再次运行`npm run start`，仅当`index.js`内容变化时，就会自动重新执行`electron .`来重启应用

## 菜单栏与边框

```javascript
app.on("ready", () => {
  mainWindow = new BrowserWindow({
    // 窗口位置
    x: 0,
    y: 0,
    //设置窗口宽高
    width: 400,
    height: 600,
    frame: false, // 无边框页面(同时菜单栏也不会显示，只是不会显示，可以通过快捷键操作)
  });
  mainWindow.removeMenu(); //去掉菜单栏
  mainWindow.loadFile("./src/main.html");
});
```

默认情况下，无边框窗口是不可拖拽的,可以通过设置

1. `-webkit-app-region: drag`来告诉`Electron`哪些区域是可拖拽的
2. `-webkit-app-region: no-drag;`来告诉`Electron`哪些区域是不可拖拽的

```CSS
html,body {
  height: 100%;
  width: 100%;
}

body{
  -webkit-app-region: drag;
}

.enable-click {
  -webkit-app-region: no-drag;
}
```

## 系统托盘

程序启动时，将应用程序加入系统托盘。在 Electron 中，借助 Tray 模块实现。

```javascript
//app 模块，控制整个应用程序的事件生命周期。
//BrowserWindow 模块，它创建和管理程序的窗口。
const { app, BrowserWindow, Tray, Menu } = require("electron");
const path = require("path");

const iconPath = path.join(__dirname, "./src/img/logo.png"); //应用运行时的标题栏图标

let mainWindow, tray;

//在 Electron 中，只有在 app 模块的 ready 事件被激发后才能创建浏览器窗口
app.on("ready", () => {
  mainWindow = new BrowserWindow({
    // frame: false, // 无边框页面
    resizable: false, //不允许用户改变窗口大小
    width: 800, //设置窗口宽高
    height: 600,
    icon: iconPath, //应用运行时的标题栏图标
    webPreferences: {
      backgroundThrottling: false, //设置应用在后台正常运行
      nodeIntegration: true, //设置能在页面使用nodejs的API
      contextIsolation: false,
      preload: path.join(__dirname, "./preload.js"),
    },
  });
  mainWindow.removeMenu(); //去掉菜单栏（菜单栏的快捷键）
  //   mainWindow.loadURL(`file://${__dirname}/src/main.html`);
  mainWindow.loadFile("./src/main.html");
  //   系统托盘
  tray = new Tray(iconPath); //实例化一个tray对象，构造函数的唯一参数是需要在托盘中显示的图标url
  tray.setToolTip("Tasky"); //鼠标移到托盘中应用程序的图标上时，显示的文本
  tray.on("click", () => {
    //点击图标的响应事件，这里是切换主窗口的显示和隐藏
    if (mainWindow.isVisible()) {
      mainWindow.hide();
    } else {
      mainWindow.show();
    }
  });
  tray.on("right-click", () => {
    //右键点击图标时，出现的菜单，通过Menu.buildFromTemplate定制，这里只包含退出程序的选项。
    const menuConfig = Menu.buildFromTemplate([
      {
        label: "Quit",
        click: () => app.quit(),
      },
      {
        label: "Next Step",
        click: () => app.quit(),
      },
    ]);
    tray.popUpContextMenu(menuConfig);
  });
});
```

## IPC 通信

以隐藏窗口为例

### 渲染进程 TO 主进程

```javascript
// 页面文件
const { ipcRenderer } = require("electron");
ipcRenderer.send("mainWindow:close");
```

```javascript
// index.js
const { ipcMain } = require("electron");
ipcMain.on("mainWindow:close", () => {
  mainWindow.hide();
});
```

### 主进程 TO 渲染进程

### 窗口置顶

```javascript
mainWindow.setAlwaysOnTop(true); // 置顶
```

### 关闭窗口

```javascript
// 提醒窗口会在一段时间后关闭，可以通过remindWindow.close()来关闭窗口。
// 当窗口关闭后，我们可以设置remindWindow = null来回收分配给该渲染进程的资源。
mainWindow.on("closed", () => {
  mainWindow = null;
});
mainWindow.close();
```

### 访问后页面注入脚本

```javascript

```
