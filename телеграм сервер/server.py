from flask import Flask, request, jsonify
import datetime
import threading
import time

app = Flask(__name__)
users_data = {}

# Функция для поддержания активности (упрощенная)
def keep_alive():
    while True:
        try:
            # Просто ждем и ничего не делаем
            time.sleep(300)  # 5 минут
        except:
            time.sleep(300)

@app.route('/')
def home():
    server_status = "✅ АКТИВЕН"
    users_count = len(users_data)
    messages_count = sum(len(messages) for messages in users_data.values())
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Telegram Server Status</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
            .container {{ background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            .status {{ color: green; font-weight: bold; }}
            .info {{ margin: 10px 0; padding: 10px; background: #e8f5e8; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🤖 Telegram Сервер</h1>
            <div class="info">
                <p><strong>Статус:</strong> <span class="status">{server_status}</span></p>
                <p><strong>Время:</strong> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                <p><strong>Пользователей:</strong> {users_count}</p>
                <p><strong>Сообщений:</strong> {messages_count}</p>
            </div>
            <p><a href="/users">📊 Посмотреть пользователей</a></p>
            <p><a href="/test">🧪 Тест API</a></p>
            <p><em>Сервер работает на вашем ПК</em></p>
        </div>
    </body>
    </html>
    """

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] 📨 Получено сообщение")
        
        if 'message' in data:
            user_id = data['message']['from']['id']
            text = data['message'].get('text', '')
            first_name = data['message']['from'].get('first_name', 'Неизвестный')
            
            if user_id not in users_data:
                users_data[user_id] = []
            
            users_data[user_id].append({
                'text': text,
                'time': str(datetime.datetime.now()),
                'first_name': first_name
            })
            
            print(f"✅ Сообщение от {first_name}: {text}")
        
        return jsonify({'status': 'ok'})
    
    except Exception as e:
        print(f"❌ Ошибка в webhook: {e}")
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/users')
def show_users():
    return jsonify({
        'total_users': len(users_data),
        'users': users_data
    })

@app.route('/test')
def test():
    return jsonify({
        'status': 'success',
        'message': 'Сервер работает корректно!',
        'timestamp': str(datetime.datetime.now()),
        'users_count': len(users_data)
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'timestamp': str(datetime.datetime.now())})

if __name__ == '__main__':
    # Запускаем фоновый процесс для поддержания активности
    maintenance_thread = threading.Thread(target=keep_alive)
    maintenance_thread.daemon = True
    maintenance_thread.start()
    
    print("=" * 50)
    print("🚀 ЗАПУСК TELEGRAM СЕРВЕРА")
    print("=" * 50)
    print(f"Время запуска: {datetime.datetime.now()}")
    print("Сервер доступен по адресу: http://localhost:5000")
    print("Для остановки нажмите Ctrl+C")
    print("=" * 50)
    
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    except KeyboardInterrupt:
        print("\n⏹️ Сервер остановлен пользователем")
    except Exception as e:
        print(f"\n❌ Ошибка запуска сервера: {e}")