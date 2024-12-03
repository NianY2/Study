git config --global user.name '陈煜'
git config --global user.email '1871263099@qq.com'
git add .
set /p var=CommitMessage:
git commit -m %var%
@REM Gitee
git push
pause "======ok======"