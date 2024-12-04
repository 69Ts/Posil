function updateClock(clockId) {
    const now = new Date();
    const options = { timeZone: "Europe/Moscow", hour: "2-digit", minute: "2-digit", second: "2-digit" };
    const timeString = now.toLocaleTimeString("ru-RU", options);
    document.getElementById(clockId).textContent = timeString;
}

// Обновляем часы
setInterval(() => updateClock("clock-hourly-time"), 1000);
setInterval(() => updateClock("clock-daily-time"), 1000);
