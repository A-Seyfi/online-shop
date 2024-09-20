$('#sl2').slider();
	var RGBChange = function() {
	  $('#RGB').css('background', 'rgb('+r.getValue()+','+g.getValue()+','+b.getValue()+')')
	};	



let slider = document.getElementById('slider');
let items = document.querySelectorAll('.main-slider .list .item');
let next = document.getElementById('next');
let prev = document.getElementById('prev');
let thumbnails = document.querySelectorAll('.slider-thumbnail .item');

let countItem = items.length;
let itemActive = 0;

let startX;

if(slider){
   next.onclick = function(){
       itemActive = itemActive + 1;
       if(itemActive >= countItem){
           itemActive = 0;
       }
       showSlider();
   }
   
   prev.onclick = function(){
       itemActive = itemActive - 1;
       if(itemActive < 0){
           itemActive = countItem - 1;
       }
       showSlider();
   }
   
   let refreshInterval = setInterval(() => {
       next.click();
   }, 4000)
   function showSlider(){
       let itemActiveOld = document.querySelector('.main-slider .list .item.active');
       let thumbnailActiveOld = document.querySelector('.slider-thumbnail .item.active');
       itemActiveOld.classList.remove('active');
       thumbnailActiveOld.classList.remove('active');
   
       items[itemActive].classList.add('active');
       thumbnails[itemActive].classList.add('active');
   
       
       clearInterval(refreshInterval);
       refreshInterval = setInterval(() => {
           next.click();
       }, 4000)
   }
   
   
   slider.addEventListener('touchstart', (e) => {
      startX = e.touches[0].clientX;
   });
   slider.addEventListener('touchmove', (e) => {
      const moveX = e.touches[0].clientX;
      const diffX = startX - moveX;
   
      if (diffX > 10) {
        itemActive = itemActive + 1;
        if(itemActive >= countItem){
            itemActive = 0;
        }
        showSlider();
        startX = null;
      }
      if (diffX < 10) {
         itemActive = itemActive - 1;
         if(itemActive < 0){
             itemActive = countItem - 1;
         }
         showSlider();
        startX = null;
      }
   });
   
   
   thumbnails.forEach((thumbnail, index) => {
       thumbnail.addEventListener('click', () => {
           itemActive = index;
           showSlider();
       })
   })
}
		



function updatePrice(container, n) {
   var priceTag = container.find('.cd-price'),
       selectedItem = container.find('.cd-item-wrapper li').eq(n);
   if( selectedItem.data('sale') ) { 
      // if item is on sale - cross old price and add new one
      priceTag.addClass('on-sale');
      var newPriceTag = ( priceTag.next('.cd-new-price').length > 0 ) ? priceTag.next('.cd-new-price') : $('<em class="cd-new-price"></em>').insertAfter(priceTag);
      newPriceTag.text(selectedItem.data('price'));
      setTimeout(function(){ newPriceTag.addClass('is-visible'); }, 100);
   } else {
      // if item is not on sale - remove cross on old price and sale price
      priceTag.removeClass('on-sale').next('.cd-new-price').removeClass('is-visible').on('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', function(){
         priceTag.next('.cd-new-price').remove();
      });
   }
}



function setActiveColor(event) {
   const links = document.querySelectorAll('.sort');
   links.forEach(link => {
       link.classList.remove('active');
   });
   event.target.classList.add('active');
   localStorage.setItem('activeLink', event.target.textContent);
}

window.onload = () => {
   const activeLink = localStorage.getItem('activeLink');
   if (activeLink) {
       const links = document.querySelectorAll('.sort');
       links.forEach(link => {
           if (link.textContent === activeLink) {
               link.classList.add('active');
           }
       });
   }
};



const links = document.querySelectorAll('.sort');
links.forEach(link => {
   link.addEventListener('click', setActiveColor);
});

function clearActiveClass() {
   links.forEach(link => {
       link.classList.remove('active');
   });
}

document.addEventListener('click', function(event) {
   if (!event.target.classList.contains('sort')) {
      clearActiveClass();
   localStorage.setItem('activeLink', event.target.textContent);
   }
});




/* brand slider */
const brand_slides = document.getElementById('brand_slides')
const lastSlide = document.querySelectorAll('.brand-slide');
const lastDiv = lastSlide[lastSlide.length - 1];

if(lastDiv){
   const lastDivPositionX = lastDiv.getBoundingClientRect().left + window.scrollX;
   if(lastDivPositionX < 0){
      setInterval(()=>{
         brand_slides.style.transition = 'all 20s'
         brand_slides.style.transform = `translateX(${-lastDivPositionX + 20}px)`

         if (brand_slides.getBoundingClientRect().left + window.scrollX >= -lastDivPositionX + 10) {
            brand_slides.style.transition = 'none'
            brand_slides.style.transform = `translateX(0)`
         }
      },1)
   }
}



const panel_menu = document.getElementById('panel_menu')
const panel_list_menu = document.getElementById('panel_list_menu')
let menu = -1

if (panel_menu) {
   panel_menu.addEventListener('click', ()=>{
      menu = -menu
      
      if(menu > 0){
         panel_list_menu.style.right = '0'
      }
      else{
         panel_list_menu.style.right = '-100%'
      }
   })
}



const product_val = document.querySelectorAll('.laptop-detail div span')
if (product_val) {
   product_val.forEach(val => {
      if (val.innerHTML == 'None' || val.innerHTML == ''){
         val.innerHTML = '-'
      }
   });
}