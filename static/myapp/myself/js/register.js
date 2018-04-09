$(function () {
    $("#username").change(function () {
        var username = $('#username').val()
        $.getJSON('/myapp/check_user/', {'username': username}, function (data) {
            console.log(data)
            if (data['status'] = '888') {

                $('#username_info').html(data['msg']).css('color', 'green')

            } else {

                $('#username_info').html(data['msg']).css('color', 'red')


            }


        })

    })

    $('#password').change(function () {

        var password = $(this).val();
        if (password.length < 6 | password.length > 16) {
            $("#password_info").html('密码不符合规范').css('color', 'red')


        } else {
            $('#password_info').html('密码符合规范').css('color', 'green')
        }


    })

    $('#password_confirm').change(function () {

        var password_confirm = $(this).val()
        var password = $("#password").val()
        if (password == password_confirm) {
            $('#password_confirm_info').html('密码输入一致').css('color', 'green')


        } else {

            $('#password_confirm_info').html('密码输入不一致').css('color', 'red')

        }

    })


})


function check() {
    var password = $("#password").val();
    var passwordconfirm = $("#password_confirm").val();
    if (password != passwordconfirm) {
        return false;
    }
    var newpassword = md5(password);
    $("#password").val(newpassword);
    return true;
}

