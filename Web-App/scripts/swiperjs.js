let viewScreenButtons = document.querySelectorAll('.view-screen');
let swiperCloseButtons = document.querySelectorAll('.swiper-close');

for (let item of viewScreenButtons) {
  item.addEventListener('click', () => {
      let element_id = item.id;
      window.alert('.swiperjs .'+element_id);
      let swiperjs = document.querySelector('.swiperjs .'+element_id);
      swiperjs.classList.add('active');
  });
}
for (let item of swiperCloseButtons){
    item.addEventListener('click', () => {
      swiperjs.classList.remove('active');
    });
}
