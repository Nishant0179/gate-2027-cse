@echo off
title GATE 2027 CSE Preparation Platform
echo ========================================================
echo    GATE 2027 Computer Science Preparation Platform
echo    Organizing Institute: IIT Madras
echo ========================================================
echo.
echo Setting up Node environment...
set "PATH=C:\Program Files\nodejs;%PATH%"
cd /d "%~dp0web_platform"

echo Launching GATE 2027 Study Platform on http://localhost:3000 ...
call npm.cmd run preview -- --port 3000 --host
pause
