$(function () {

    $(".ischoose").click(function (event) {

        event.stopPropagation();

        var ischoose = $(this);
        var cartid = ischoose.parents("li").attr("cartid");
        console.log(cartid);
        $.getJSON("/myapp/changecheck/", {"cartid": cartid}, function (data) {

            if (data["is_select"]) {
                console.log("呵呵");
                ischoose.find("span").show();
            } else {
                console.log("你真是一个小天才");
                ischoose.find("span").hide();
            }
        })
    })

    $(".subgoods").click(function () {
        var clickNode = $(this);
        var cartid = clickNode.parents("li").attr("cartid");
        console.log(cartid);
        $.getJSON("/myapp/subcartgoods/", {"cartid": cartid}, function (data) {
            console.log(data);
            if (data["num"] == 0) {
                clickNode.parents("li").hide();
            } else {
                clickNode.next().html(data["num"]);
            }
        })
    })


    $(".addgoods").click(function () {
        var clickNode = $(this);
        var cartid = clickNode.parents("li").attr("cartid");
        console.log(cartid);
        $.getJSON("/myapp/addcartgoods/", {"cartid": cartid}, function (data) {
            console.log(data);

            clickNode.prev().html(data["num"]);

        })
    })


    $(".confirm").click(function () {
        var select_length = $(".select_status").length;
        var select_array = [];
        var unselect_array = [];
        $(".select_status").each(function (index) {
            console.log(index);
            var item = $(".select_status").eq(index);
            var cartid = item.parents("li").attr("cartid");
            if (item.css("display") == "block") {
                console.log(cartid);
                select_array.push(cartid);
            } else {
                unselect_array.push(cartid);
            }
        })

        if (select_array.length == select_length) {
            //    所有都变成未选中
            $(".select_status").css("display", "none");
            $(".confirm").find(".all_select").css("display", "none");
        } else {
            //    所有都变成选中
            $(".select_status").css("display", "block");
            $(".confirm").find(".all_select").css("display", "block");
        }


    })
    $(".generate_order").click(function () {
        var select_length = $(".select_status").length;
        var select_array = [];
        var unselect_array = [];
        $(".select_status").each(function (index) {
            console.log(index);
            var item = $(".select_status").eq(index);
            var cartid = item.parents("li").attr("cartid");
            if (item.css("display") == "block") {
                console.log(cartid);
                select_array.push(cartid);
            } else {
                unselect_array.push(cartid);
            }
        })

        if (select_array.length == 0) {
            alert("请添加商品");
            return "HeHe";
        }

        var selects = select_array.join("#");
        $.getJSON("/myapp/generateorder/", {"selects": selects}, function (data) {
            console.log(data);
            if (data["status"] == "200") {
                window.open("/myapp/orderdetail/?orderid=" + data["order_num"], target = "_self");
            }
        })


    })


})