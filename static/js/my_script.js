    // функція для перенаправлення для написання коментів користувачу
    function addReview(name, id) {
        document.getElementById("comment_parent").value = id;
        document.getElementById("comment_text").innerText = `${name}, `
    }
