$(function () {

    initTopSwiper();
    initSwiperMenu();



})

function initTopSwiper() {
    var swiper = Swiper("#topSwiper",{
        pagination:'.swiper-pagination',
        autoplay:4000,
    })
}

function initSwiperMenu() {
    var swiper = new Swiper('#swipermenu',
    {
        slidesPerView :3,
    })


}