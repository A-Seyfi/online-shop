const pd_values = document.querySelectorAll('.main-detail li span');
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




const select_ram = document.getElementById('id_ram');
const custom_ram = document.getElementById('custom_ram');
const ram_val = document.getElementById('ram_val');

function createOptionRam() {
    Array.from(select_ram.options).forEach(option => {
        if(option.value != 0){
            const div = document.createElement('div');
            div.className = 'custom-option';
            div.textContent = option.text;
            div.dataset.value = option.value;
            
            if(option.value == 1){
                div.click();
                div.classList.add('active-custom')
                ram_val.innerText = option.text;
                select_ram.value = option.value;
            }
            
            div.addEventListener('click', () => {
                const options = document.querySelectorAll('#custom_ram .custom-option')
                options.forEach(clicked_option => {
                    clicked_option.classList.remove('active-custom')
                })
                select_ram.value = option.value;
                ram_val.innerText = option.text;
                div.classList.add('active-custom')
            });
            
            custom_ram.appendChild(div);
        }
    });
}
createOptionRam();




const id_storage = document.getElementById('id_storage');
const custom_storage = document.getElementById('custom_storage');

function createOptionStorage() {
    Array.from(id_storage.options).forEach(option => {
        if(option.value != 0){
            const div = document.createElement('div');
            div.className = 'custom-option';
            div.textContent = option.text;
            div.dataset.value = option.value;
            
            if(option.value == 1){
                div.click();
                div.classList.add('active-custom')
                id_storage.value = option.value;
            }
            
            div.addEventListener('click', () => {
                const options = document.querySelectorAll('#custom_storage .custom-option')
                options.forEach(clicked_option => {
                    clicked_option.classList.remove('active-custom')
                })
                id_storage.value = option.value;
                div.classList.add('active-custom')
            });
            
            custom_storage.appendChild(div);
        }
    });
}
createOptionStorage();



const id_color = document.getElementById('id_color');
const custom_color = document.getElementById('custom_color');

function createOptionColor() {
    Array.from(id_color.options).forEach(option => {
        if(option.value != 0){
            const div = document.createElement('div');
            div.className = 'custom-option';
            div.textContent = option.text;
            div.dataset.value = option.value;

            if(option.value == 1){
                div.click();
                div.classList.add('active-custom')
                id_color.value = option.value;
            }
            
            div.addEventListener('click', () => {
                const options = document.querySelectorAll('#custom_color .custom-option')
                options.forEach(clicked_option => {
                    clicked_option.classList.remove('active-custom')
                })
                id_color.value = option.value;
                div.classList.add('active-custom')
            });
    
            custom_color.appendChild(div);
        }
    });
}
createOptionColor();



const id_warranty = document.getElementById('id_warranty');
const custom_warranty = document.getElementById('custom_warranty');

function createOptionWarranty() {
    Array.from(id_warranty.options).forEach(option => {
        if(option.value != 0){
            const div = document.createElement('div');
            div.className = 'custom-option';
            div.textContent = option.text;
            div.dataset.value = option.value;

            if(option.value == 1){
                div.click();
                div.classList.add('active-custom')
                id_warranty.value = option.value;
            }
            
            div.addEventListener('click', () => {
                const options = document.querySelectorAll('#custom_warranty .custom-option')
                options.forEach(clicked_option => {
                    clicked_option.classList.remove('active-custom')
                })
                id_warranty.value = option.value;
                div.classList.add('active-custom')
            });
    
            custom_warranty.appendChild(div);
        }
    });
}
createOptionWarranty();