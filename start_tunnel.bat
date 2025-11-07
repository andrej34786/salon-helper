@echo off
chcp 65001 >nul
title Cloudflare Tunnel
echo ========================================
echo    ЗАПУСК CLOUDFLARE ТУННЕЛЯ
echo ========================================
cd /d "C:\Users\Андрей\Desktop\telegram_server"
:restart_tunnel
echo [%time%] Запускаем Cloudflare туннель...
cloudflared tunnel --url http://localhost:5000
echo [%time%] Туннель упал. Перезапуск через 10 секунд...
timeout /t 10 /nobreak >nul
goto restart_tunnel