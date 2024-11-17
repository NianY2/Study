const { app, BrowserWindow, session, dialog } = require("electron");
const path = require("path");
const axios = require("axios");
const fs = require("fs");

// try {
//   require("electron-reloader")(module);
// } catch (_) {}

const createWindow = (
  url = "https://jwc.mmpt.edu.cn/xtgl/login_slogin.html"
) => {
  const win = new BrowserWindow({
    x: 0,
    y: 0,
    width: 2048,
    height: 1080,
    webPreferences: {
      nodeIntegration: process.env.ELECTRON_NODE_INTEGRATION,
      contextIsolation: !process.env.ELECTRON_NODE_INTEGRATION,
      // preload: path.join(__dirname, "preload.js"),
    },
  });
  
  win.loadURL(url);

  win.webContents.on("did-finish-load", () => {
    const script = fs.readFileSync("login.js", "utf-8");
    win.webContents.executeJavaScript(script);
  });

  win.webContents.setWindowOpenHandler(({ url }) => {
    console.log(`New window opened for ${url}`);
    return {
      action: "allow",
      overrideBrowserWindowOptions: {
        webPreferences: {
          nodeIntegration: true,
        },
      },
    };
  });
};

app.whenReady().then(() => {
  // dialog.showErrorBox("错误", "错误错误错误");
  createWindow();
});
