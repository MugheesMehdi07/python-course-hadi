document.addEventListener('DOMContentLoaded', function() {
    fetchProducts();
    document.getElementById('addProductForm').addEventListener('submit', addProduct);
});

function fetchProducts() {
    fetch('http://localhost:8000/api/product/products/')
    .then(response => response.json())
    .then(products => {
        const productList = document.getElementById('productList');
        productList.innerHTML = ''; // Clear list before displaying updated list
        products.forEach(product => {
            let li = document.createElement('li');
            li.textContent = `${product.name} - Price: $${product.price}`;
            let deleteButton = document.createElement('button');
            deleteButton.textContent = 'Delete';
            deleteButton.onclick = function() { deleteProduct(product.id); };
            let updateButton = document.createElement('button');
            updateButton.textContent = 'Update';
            updateButton.onclick = function() { showUpdateForm(product); };
            li.appendChild(deleteButton);
            li.appendChild(updateButton);
            productList.appendChild(li);
        });
    })
    .catch(error => console.error('Error fetching products:', error));
}

function addProduct(event) {
    event.preventDefault();
    let name = document.getElementById('addName').value;
    let price = document.getElementById('addPrice').value;
    fetch('http://localhost:8000/api/product/products/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({name: name, price: price})
    }).then(() => {
        fetchProducts(); // Refresh the product list
        document.getElementById('addName').value = ''; // Clear form
        document.getElementById('addPrice').value = '';
    });
}

function showUpdateForm(product) {
    document.getElementById('updateProductForm').style.display = 'block';
    document.getElementById('updateName').value = product.name;
    document.getElementById('updatePrice').value = product.price;
    window.currentProduct = product; // Store current product globally for update
}

function updateProduct() {
    let name = document.getElementById('updateName').value;
    let price = document.getElementById('updatePrice').value;
    fetch(`http://localhost:8000/api/product/products/${window.currentProduct.id}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({name: name, price: price})
    }).then(() => {
        fetchProducts(); // Refresh the product list
        document.getElementById('updateProductForm').style.display = 'none'; // Hide form
    });
}

function deleteProduct(id) {
    fetch(`http://localhost:8000/api/product/products/${id}/`, {
        method: 'DELETE'
    }).then(() => {
        fetchProducts(); // Refresh the product list
    });
}
