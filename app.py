
from datetime import datetime, timedelta
import pytz
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/daily")
def daily_message():
    return render_template("daily_message.html")

from datetime import datetime, timedelta
import pytz
from flask import Flask, render_template

@app.route('/hourly')
def hourly_message():
    # Настройка Московского времени
    now = datetime.now(pytz.timezone('Europe/Moscow'))
    
    # Логика для текста
    time_mapping = {
        (10, 55): "Покаяние и Молитва",
        (11, 0): "Духовное укрепление",
        (11, 5): "Вера и надежда",
        (11, 10): "Смирение и мудрость",
        (11, 15): "Любовь и сострадание",
        (11, 20): "Терпение и усердие",
        (11, 25): "Прощение и очищение",
        (11, 30): "Забота о ближнем",
        (11, 35): "Благодарность и радость",
        (11, 40): "Благословение и защита",
        (11, 45): "Мир и покой",
        (11, 50): "Уверенность в пути",
        (11, 55): "Свет и жизнь",
        (12, 0): "Начало нового",
        (12, 5): "Завершение посыла",
    }

    # Определяем текущий текст
    current_text = "Текст не найден"
    for (hour, minute), text in time_mapping.items():
        target_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if now >= target_time:
            current_text = text

    return render_template("hourly_message.html", time=now, upper_text=current_text, lower_text=current_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
