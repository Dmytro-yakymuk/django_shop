function ajaxSend(url, params) {
    // Отправляем запрос
    fetch(`${url}?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
        .then(response => response.json())
        .then(json => render(json))
        .catch(error => console.error(error))
}

const forms = document.querySelector('form[name=filter]');

 forms.addEventListener('submit', function (e) {
     // Получаем данные из формы
     e.preventDefault();
     let url = this.action;
     let params = new URLSearchParams(new FormData(this)).toString();
     ajaxSend(url, params);
 });

function render(data) {
    // Рендер шаблона
    let template = Hogan.compile(html);
    let output = template.render(data);

    const div = document.querySelector('#content>.row');
    div.innerHTML = output;
}


let html = '\
{{#products}}\
    <div class="col-12 col-sm-6 col-lg-4 featureCol mb-7">\
        <div class="border">\
            <div class="imgHolder position-relative w-100 overflow-hidden">\
                  <img src="/media/{{ product.get_image_root.url }}" alt="image description" class="img-fluid w-100">\
                <ul class="list-unstyled postHoverLinskList d-flex justify-content-center m-0">\
                    <li class="mr-2 overflow-hidden"><a href="javascript:void(0);" class="icon-heart d-block"></a></li>\
                    <li class="mr-2 overflow-hidden"><a href="javascript:void(0);" class="icon-cart d-block"></a></li>\
                    <li class="mr-2 overflow-hidden"><a href="javascript:void(0);" class="icon-eye d-block"></a></li>\
                    <li class="overflow-hidden"><a href="javascript:void(0);" class="icon-arrow d-block"></a></li>\
                </ul>\
            </div>\
            <div class="text-center py-5 px-4">\
                <span class="title d-block mb-2"><a href="{{ product.get_absolute_url }}">{{ product.name }}</a></span>\
                <span class="price d-block fwEbold"><del>75.00 $</del>{{ product.price|floatformat:2 }} $</span>\
                <span class="hotOffer fwEbold text-uppercase text-white position-absolute d-block">HOT</span>\
                <span class="hotOffer green fwEbold text-uppercase text-white position-absolute d-block ml-8">Sale</span>\
            </div>\
        </div>\
    </div>\
{{/products}}'




