@echo off
chcp 65001 >nul
title Telegram Server
echo ========================================
echo    ЗАПУСК TELEGRAM СЕРВЕРА
echo ========================================
cd /d "C:\Users\Андрей\Desktop\telegram_server"
:restart_server
echo [%time%] Запускаем Flask сервер...
python server.py
echo [%time%] Сервер остановлен. Перезапуск через 5 секунд...
timeout /t 5 /nobreak >nul
goto restart_server