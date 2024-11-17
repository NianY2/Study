const { app, BrowserWindow, session, dialog } = require("electron");
const path = require("path");
const axios = require("axios");
const fs = require("fs");

try {
  require("electron-reloader")(module);
} catch (_) {}

const createWindow = () => {
  const win = new BrowserWindow({
    x: 0,
    y: 0,
    width: 2048,
    height: 400,
    webPreferences: {
      nodeIntegration: process.env.ELECTRON_NODE_INTEGRATION,
      contextIsolation: !process.env.ELECTRON_NODE_INTEGRATION,
      preload: path.join(__dirname, "preload.js"),
    },
  });
  win.loadURL("https://www.baidu.com/");

  win.webContents.on("did-finish-load", () => {
    const script = fs.readFileSync("preload.js", "utf-8");
    win.webContents.executeJavaScript(script);
  });
  // 请求拦截
  const ses = win.webContents.session;
  ses.webRequest.onBeforeSendHeaders((details, callback) => {
    console.log(
      details.url.toString().includes("https://www.baidu.com/sugrec")
    );
    if (details.url.toString().includes("https://www.baidu.com/sugrec")) {
      callback({ cancel: true });
      return;
      // console.log(true);
    }
    callback({ cancel: false });
  });
};

app.whenReady().then(() => {
  // dialog.showErrorBox("错误", "错误错误错误");
  createWindow();

  axios
    .get("http://121.37.66.46:9999/api/boke/essay/")
    .then((response) => {
      // console.log(`Status code: ${response.status}`);
      // console.log(response.data);
    })
    .catch((error) => {
      console.error(error.message);
    });

  session.defaultSession.cookies.get({}).then((cookies) => {
    for (var i = 0; i < cookies.length; i++) {
      //删除cookie
      session.defaultSession.cookies.remove(
        "https://www.baidu.com/",
        cookies[i].name,
        (error) => {}
      );
    }
  });

  const cookie = [
    {
      url: "https://www.baidu.com/",
      name: "BAIDUID",
      value: "C17B30405D3C000255A69FF70EBAAA22:FG=1",
    },
    {
      url: "https://www.baidu.com/",
      name: "BDUSS",
      value:
        "JGUGkxdWUzU2oyYnN6UkhmYUtJTFJJQm9qTGRQdjU5R1BUZWU2cVNQdW4tNnhrSUFBQUFBJCQAAAAAAAAAAAEAAACszLOpwe~By8Hvwcu087G-06oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKduhWSnboVkRE",
    },
  ];

  cookie.forEach((item) => {
    session.defaultSession.cookies.set(item).then(() => {
      console.log("cookies suc");
    });
  });
});
