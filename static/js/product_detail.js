const listItems = document.querySelectorAll('#detail_list li');
if(listItems.length > 0){
   const toggleButton = document.getElementById('toggleButton');
   const item_5 = document.getElementById('item_5');
   let isExpanded = false;
   
   item_5.style.borderBottom = 'none';
   
   for (let i = 5; i < listItems.length; i++) {
      listItems[i].classList.add('hidden');
   }
   toggleButton.addEventListener('click', () => {
      isExpanded = !isExpanded;
      for (let i = 5; i < listItems.length; i++) {
         listItems[i].classList.toggle('hidden');
      }
      toggleButton.innerHTML = isExpanded ? 'نمایش کمتر<span class="fa fa-chevron-up"></span>' : 'نمایش بیشتر<span class="fa fa-chevron-down"></span>';
      item_5.style.borderBottom = isExpanded ? '1px solid #d3d3d3' : 'none';
   });
   
   
   const pd_values = document.querySelectorAll('#detail_list li span');
   pd_values.forEach(val => {
       if (val.innerHTML == 'None' || val.innerHTML == ''){
           val.innerHTML = '-'
       }
   
       if (val.innerHTML == 'False'){
           val.innerHTML = 'ندارد'
       }
       if (val.innerHTML == 'True'){
           val.innerHTML = 'دارد'
       }
   });
}




const more_pd = document.getElementById('more_pd')
const comment = document.getElementById('comment')

const pd_tab = document.getElementById('pd_tab')
const comment_tab = document.getElementById('comment_tab')

function scroll_down() {
    document.getElementById('category_tab').scrollIntoView({ 
        behavior: 'smooth' 
    });
}

more_pd.addEventListener('click', ()=>{
    scroll_down();
    pd_tab.click();
});
comment.addEventListener('click', ()=>{
    scroll_down();
    comment_tab.click();
});