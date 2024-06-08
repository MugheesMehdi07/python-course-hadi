document.addEventListener('DOMContentLoaded', function() {
    fetch('http://localhost:8000/api/order/orders/')
    .then(response => response.json())
    .then(orders => {
        const orderList = document.getElementById('orderList');
        orders.forEach(order => {
            let li = document.createElement('li');
            li.textContent = `Order ID: ${order.id}, Product ID: ${order.product}, Quantity: ${order.quantity}`;
            orderList.appendChild(li);
        });
    })
    .catch(error => console.error('Error fetching orders:', error));
});
