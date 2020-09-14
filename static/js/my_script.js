// функція для перенаправлення для написання коментів користувачу
function addReview(name, id) {
    document.getElementById("comment_parent").value = id;
    document.getElementById("comment_text").innerText = `${name}, `
}

// Add star rating
const rating = document.querySelector('form[name=rating]');

rating.addEventListener("change", function (e) {
    // Получаем данные из формы
    let data = new FormData(this);
    fetch(`${this.action}`, {
        method: 'POST',
        body: data
    })
        .then(response => alert("Рейтинг установлен"))
        .catch(error => alert("Ошибка"))
});



