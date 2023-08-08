@echo off
pip install pygame
cls
title Pingpong Launcher
color 0a
echo PingPong Launcher By TAEIN
echo.
echo 0) Super Easy - Developer cleared
echo 1) Easy - Developer cleared
echo 2) Normal - Developer cleared
echo 3) Hard - Developer cleared
echo 4) Very hard - Developer cleared
echo 5) ULTRA HARD - Developer 7.5
echo.
set /p cho=">"
if "%cho%" == "0" python pingpong_supereasy.py
if "%cho%" == "1" python pingpong_easy.py
if "%cho%" == "2" python pingpong_normal.py
if "%cho%" == "3" python pingpong_hard.py
if "%cho%" == "4" python pingpong_veryhard.py
if "%cho%" == "5" python pingpong_ultrahard.py
exit