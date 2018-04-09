function check() {
    var password = $("#password").val();
    if (password.trim().length == 0){
        return true
    }
    
    if (password.length < 6 | password.length > 16){
        return false;
    }
    var passwordconfirm = $("#password_confirm").val();
    if (password != passwordconfirm){
        return false;
    }
    var newpassword = md5(password);
    $("#password").val(newpassword);
    return true;
}

$(function () {
    $("#password").change(function () {
        var password = $(this).val();
        // 去掉字符串左右的空格
        password = password.trim();
        if (password.length == 0){
            console.log("不想改变密码了");
        }else if (password.length < 6 | password.length > 16){
        //    错误提示
            console.log("密码格式错误");
        }else{
            console.log("密码符合规范");
        }
    })

    $("#password_confirm").change(function () {
        var password = $("#password").val().trim();
        var passwordconfirm = $(this).val();
        if (password == passwordconfirm){
            console.log("两次密码一致");
        }else{
            console.log("两次输入不一致");
        }
    })


})



