// $(document).ready(function() {
//     let resultField = $(".filter-panel-item-conten");

//     $(document).on('click', function(event) {
//         if (!resultField.is(event.target) && resultField.has(event.target).length === 0) {
//             deleteAllActiveClasses(resultField);
//         }
//     });
// });

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).on('click', '#add-to-cart-button', async function(e) {
    e.preventDefault();
    let button = document.querySelector('#add-to-cart-button')
    button.disabled = true;

    setTimeout(function() {
        button.disabled = false;
    }, 5000);

    const productId = document.querySelector('.product-info').getAttribute('data-product-id');

    fetch("/api/cart/add_to_cart/", {
        method: "POST",
        credentials: "same-origin",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({product_id: productId,})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        $("#add-to-cart-button").css("background-color", "#4cd964");
        $("#add-to-cart-button").css("border-color", "#4cd964");
        $("#add-to-cart-button").html("Добавлено в корзину");
    });
});

async function deleteProductFromCart(productId) {
    fetch("/api/cart/delete_from_cart/", {
        method: "DELETE",
        credentials: "same-origin",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({product_id: productId,})
    })
    .then(response => response.json())
    .then(data => {
        window.location.reload();
    });
}

async function updateProductQuantity(element, productId){
    let quantity = element.value;
    console.log(quantity)

    fetch("/api/cart/update_product_quantity/", {
        method: "UPDATE",
        credentials: "same-origin",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({
            product_id: productId,
            quantity: quantity,
        })
    })
    .then(response => response.json())
    .then(data => {
        // window.location.reload();
    });
}

function deleteAllActiveClasses(productClasses) {
    productClasses.forEach(product => {
        product_filter_class_list = product.className.split(' ')
        if (product_filter_class_list.includes('active')) {
            product.classList.remove('active');
        }
    });
}

let product_filters = document.querySelectorAll('.filter-panel-item');
product_filters.forEach(product_filter => {
    product_filter.addEventListener("click", function() {
        product_filter_class_list = product_filter.className.split(' ')
        if (product_filter_class_list.includes('active')) {
            product_filter.classList.remove('active');
        }
        else {
            deleteAllActiveClasses(product_filters);
            product_filter.classList.add('active');
        }
    });
});

$(document).on('submit', '#make-order', async function(e) {
    e.preventDefault();

    $.ajax({
        type: "POST",
        url: "/api/cart/make_order/",
        data: new FormData(this),
        dataType:'json',
        contentType:false,
        cache:false,
        processData:false,
        success: function (response) {
            window.location.href = '/order/success'
        },
        error: function (error) {
            showNotification(error.responseJSON.message);
        }
    });
});

function showNotification(text) {
    let notification = document.getElementById("layout__boxFooter");
    notification.textContent = text;
    notification.style.transform = "translateY(0)";

    setTimeout(function() {
        notification.style.transform = "translateY(100%)";
    }, 5000);
} 

$(document).on('click', '[data-test="price"]', function(e) {
    e.preventDefault();
    let dataTestItem = $(this).attr('data-test-item');

    let currentURL = window.location.href;
    let queryUrl = addQueryParam(currentURL, 'price', dataTestItem);

    window.location.href = queryUrl;
});

$(document).on('click', '[data-test="brand"]', function(e) {
    e.preventDefault();
    let dataTestItem = $(this).attr('data-test-item');
    
    let currentURL = window.location.href;
    let queryUrl = addQueryParam(currentURL, 'brand', dataTestItem);

    window.location.href = queryUrl;
});

$(document).on('click', '[data-test="price-order"]', function(e) {
    e.preventDefault();
    let dataTestItem = $(this).attr('data-test-item');
    
    let currentURL = window.location.href;
    let queryUrl = addQueryParam(currentURL, 'price_order', dataTestItem);

    window.location.href = queryUrl;
});

function addQueryParam(url, param, value) {
    const separator = url.includes('?') ? '&' : '?';
  
    if (url.includes(`${param}=`)) {
      const regex = new RegExp(`(${param}=)[^&]+`);
      return url.replace(regex, `$1${value}`);
    } else {

      return `${url}${separator}${param}=${value}`;
    }
}

