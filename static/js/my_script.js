// функція для переключання мов
$(document).ready(function(){
    $(".dropdown-item").click(function(){
        language_code = $(this).attr('value');
        $("#language").val(language_code);
        $('form[name=language_form]').submit();
    });
});


