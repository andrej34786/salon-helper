@echo off
chcp 65001 >nul
echo Добавление в автозагрузку Windows...

set "bat_path=C:\Users\Андрей\Desktop\telegram_server\start_all.bat"
set "startup_folder=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

copy "%bat_path%" "%startup_folder%\TelegramServer.lnk" >nul 2>&1

if %errorlevel% == 0 (
    echo ✅ Успешно добавлено в автозагрузку!
    echo Сервер будет запускаться автоматически при включении компьютера.
) else (
    echo ❌ Не удалось добавить в автозагрузку.
    echo Создайте ярлык вручную в папке:
    echo %startup_folder%
)

pause