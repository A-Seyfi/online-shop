window.addEventListener('scroll', function() {
    const reaction = document.querySelector('.compare-detail-section');
    const compare_menu = document.getElementById('compare_menu');
    
    const activation = reaction.getBoundingClientRect();
    if (activation.top <= 0) {
        compare_menu.style.top = '0';
        compare_menu.style.display = 'block';
    } else {
        compare_menu.style.display = 'none';
    }
});



const compared_product = document.querySelectorAll('.value');
compared_product.forEach(val => {
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