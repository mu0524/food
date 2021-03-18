$('#menubtn').click(function () {
        $('.leftmenu').toggleClass('active');
    })

    $('#menuUl li').click(function () {
        $(this).parent().find('li').each(function () {
            if ($(this).hasClass('current-active')) {
                $(this).toggleClass('current-active');
            }
        })
        $(this).toggleClass('current-active');
    })

    $('.closebtn').click(function () {
        $('.leftmenu').toggleClass('active');
})