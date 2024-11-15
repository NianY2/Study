@REM 设置IP
SET BigDataLANIP=192.168.111.135


@REM 设置命令以管理员身份运行
%1 start "" mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
@REM  清空所有转发规则
netsh interface portproxy reset


@REM 转发9000
netsh interface portproxy add v4tov4 listenport=9000 connectport=9000 connectaddress=%BigDataLANIP%
@REM 转发9870（HDFS的web管理界面）
netsh interface portproxy add v4tov4 listenport=9870 connectport=9870 connectaddress=%BigDataLANIP%
echo "succeed"
timeout /t 5 /nobreak >nul