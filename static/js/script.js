function animateTransition(event, targetUrl) {
    event.preventDefault(); // Остановить стандартное поведение ссылки

    // Анимация исчезновения
    anime({
        targets: 'body',
        opacity: [1, 0],
        duration: 500,
        easing: 'easeInOutQuad',
        complete: function () {
            // Перейти на новую страницу после завершения анимации
            window.location.href = targetUrl;
        }
    });
}
