const {
  app,
  BrowserWindow,
  globalShortcut,
  screen,
  ipcMain,
} = require("electron");
// const robot = require("electron-rebuild");

const path = require("path");
const axios = require("axios");
const fs = require("fs");

// try {
//   require("electron-reloader")(module);
// } catch (_) {}

var loginWindow;
const createLoginWindow = () => {
  loginWindow = new BrowserWindow({
    x: 0,
    y: 0,
    width: 1500,
    height: 700,
    webPreferences: {
      // backgroundThrottling: false, //设置应用在后台正常运行
      // nodeIntegration: true, //设置能在页面使用nodejs的API
      // contextIsolation: false,
      nodeIntegration: process.env.ELECTRON_NODE_INTEGRATION,
      contextIsolation: !process.env.ELECTRON_NODE_INTEGRATION,
    },
  });
  loginWindow.loadURL("https://jwc.mmpt.edu.cn/xtgl/login_slogin.html");
  loginWindow.webContents.on("did-finish-load", () => {
    const script = fs.readFileSync("/public/js/login.js", "utf-8");
    loginWindow.webContents.executeJavaScript(script);
  });
  loginWindow.webContents.on("did-start-navigation", (event, url) => {
    loginWindow.webContents.on("did-finish-load", () => {
      const script = fs.readFileSync("/public/js/preload.js", "utf-8");
      loginWindow.webContents.executeJavaScript(script);
    });
  });
  loginWindow.webContents.setWindowOpenHandler((data) => {
    createNewWindow(data.url);
    return { action: "deny" };
  });
};

const createNewWindow = (url) => {
  let newWindow = new BrowserWindow({
    x: 0,
    y: 0,
    width: 1500,
    height: 700,
    webPreferences: {
      nodeIntegration: process.env.ELECTRON_NODE_INTEGRATION,
      contextIsolation: !process.env.ELECTRON_NODE_INTEGRATION,
    },
  });
  newWindow.loadURL(url);

  newWindow.webContents.on("did-finish-load", () => {
    const script = fs.readFileSync("/public/js/preload.js", "utf-8");
    newWindow.webContents.executeJavaScript(script);
  });

  // 处理链接跳转
  newWindow.webContents.on("did-start-navigation", (event, url) => {
    newWindow.close();
    createNewWindow(url);
  });

  // 处理 window.open 跳转
  newWindow.webContents.setWindowOpenHandler((data) => {
    newWindow.close();
    createNewWindow(data.url);
  });
};

app.whenReady().then(() => {
  createLoginWindow();
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});