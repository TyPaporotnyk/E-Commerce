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
        $("#add-to-cart-button").css("background-color", "rgb(239, 62, 62)");
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

$(document).on('change', '#sort', async function(e) {
    console.log('Changed sort');
});

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

// let priceFilters = document.querySelectorAll("#price-filter > li")
// priceFilters.forEach(priceFilter => {
//     priceFilter.addEventListener("click", function() {
//         html = priceFilter.
//     })
// })

