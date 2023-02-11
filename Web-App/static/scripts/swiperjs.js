let viewScreenButtons = document.querySelectorAll('');
let swiperCloseButtons = document.querySelectorAll('.swiper-close');

for (let item of viewScreenButtons) {
  item.addEventListener('click', () => {
      let element_id = item.id;
      item.innerText = '.swiperjs .'+element_id;
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
window.alert('Hello');
