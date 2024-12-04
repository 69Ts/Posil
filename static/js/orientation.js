function updateOrientation() {
    const orientation = window.matchMedia("(orientation: landscape)").matches ? "landscape" : "portrait";
    console.log(`Ориентация: ${orientation}`);
    // Здесь можно добавить дополнительные действия, если потребуется
}

// Слушатель на изменение ориентации
window.addEventListener("resize", updateOrientation);

// Инициализация
updateOrientation();
