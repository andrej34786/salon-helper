@echo off
chcp 65001 >nul
title Telegram Server + Tunnel
echo ========================================
echo    ЗАПУСК ВСЕЙ СИСТЕМЫ
echo ========================================
cd /d "C:\Users\Андрей\Desktop\telegram_server"

echo [%time%] Запускаем сервер в отдельном окне...
start "Telegram Server" cmd /c start_server.bat

timeout /t 3 /nobreak >nul

echo [%time%] Запускаем туннель в отдельном окне...
start "Cloudflare Tunnel" cmd /c start_tunnel.bat

echo [%time%] Система запущена!
echo - Сервер: http://localhost:5000
echo - Туннель: запускается...
echo.
echo Для остановки закройте оба окна.
pause