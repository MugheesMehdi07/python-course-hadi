


document.addEventListener('DOMContentLoaded', function() {
    fetch('http://localhost:8000/api/user/users/')
    .then(response => response.json())
    .then(users => {
        const userList = document.getElementById('userList');
        users.forEach(user => {
            let li = document.createElement('li');
            li.textContent = user.name + ' - ' + user.email;
            userList.appendChild(li);
        });
    })
    .catch(error => console.error('Error fetching users:', error));
});
