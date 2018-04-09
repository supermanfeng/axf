function check() {

    var password = $("#password_login").val();
    var newpassword = md5(password);
    $("#password_login").val(newpassword);
    return true;
}
