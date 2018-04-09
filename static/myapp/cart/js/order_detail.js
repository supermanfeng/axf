$(function () {
    $("#alipay").click(function () {

        var orderid = $(this).attr("orderid");

        $.getJSON("/myapp/pay/",{"orderid":orderid},function (data) {
            console.log(data);
            if (data["status"] == "200"){
                window.open("/myapp/myself/",target="_self");
            }else{
                console.log("支付失败");
            }
        })

    })
})