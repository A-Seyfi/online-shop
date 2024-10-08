function sendProductComment(productId) {
    var comment = $('#commentText').val();
    var parentId = $('#parent_id').val();
    $.get('/products/add-product-comment?product_id=' + productId + '&product_comment=' + comment + '&parent_id=' + parentId).then(res => {
        $('#comments_area').html(res);
        $('#commentText').val('');
        $('#parent_id').val('');

        if (parentId !== null && parentId !== '') {
            document.getElementById('single_comment_box_' + parentId).scrollIntoView({behavior: "smooth"});
        } else {
            document.getElementById('comments_area').scrollIntoView({behavior: "smooth"});
        }
    });
}

function fillParentId(parentId) {
    $('#parent_id').val(parentId);
    document.getElementById('comment_form').scrollIntoView({behavior: "smooth"});
}

function filterProducts() {
    const start_price = $('#start_p').val();
    const end_price = $('#end_p').val();
    $('#start_price').val(start_price);
    $('#end_price').val(end_price);
    $('#filter_form').submit();
}

function fillPage(page) {
    $('#page').val(page);
    $('#filter_form').submit();
}

function showLargeImage(imageSrc) {
    $('#main_image').attr('src', imageSrc);
    $('#show_large_image_modal').attr('href', imageSrc);
}

function addProductToOrder(productId) {
    const productCount = $('#product-count').val();
    const productColor = $('#id_color').val();
    const productRam = $('#id_ram').val();
    const productStorage = $('#id_storage').val();
    const productWarrany = $('#id_warranty').val();
    $.get('/order/add-to-order?product_id=' + productId + '&count=' + productCount + '&color=' + productColor + '&ram=' + productRam + '&storage=' + productStorage + '&warranty=' + productWarrany).then(res => {
        Swal.fire({
            title: 'اعلان',
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: '#3085d6',
            confirmButtonText: res.confirm_button_text
        }).then((result) => {
            if (result.isConfirmed && res.status === 'not_auth') {
                window.location.href = '/login';
            }
        });
    });
}

function removeOrderDetail(detailId) {
    $.get('/user/remove-order-detail?detail_id=' + detailId).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}


// detail id => order detail id
// state => increase , decrease
function changeOrderDetailCount(detailId, state) {
    $.get('/user/change-order-detail?detail_id=' + detailId + '&state=' + state).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
            location.reload();
        }
    });
}



const remove_all = document.getElementById('remove_all')
const more_detail = document.getElementById('more_detail')
if (more_detail != null) {
    more_detail.addEventListener('click', ()=>{
        if (remove_all.style.display != 'block'){
            remove_all.style.display = 'block'
        }
    })
    document.addEventListener('click', function(event) {
        if (!event.target.closest('#remove_all') && (!event.target.closest('#more_detail'))){
            if (remove_all.style.display == 'block'){
                remove_all.style.display = 'none'
            }
        }
    });
}




const filter_btn = document.getElementById('filter_btn')
const shop_product = document.getElementById('shop_product')
const filter = document.getElementById('filter')
const back = document.getElementById('back')

if (filter_btn != null) {
    filter_btn.addEventListener("click", ()=>{
        back.style.display = 'block'

        filter.style.top = '0%'
        filter.style.backgroundColor = '#ececeb'
    })
}

if (back != null) {
    back.addEventListener("click", ()=>{
        filter.style.top = '100%'

        back.style.display = 'none'
    })
}