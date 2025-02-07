document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const loginSection = document.getElementById('loginSection');
    const todoSection = document.getElementById('todoSection');
    const loginForm = document.getElementById('loginForm');
    const logoutBtn = document.getElementById('logoutBtn');
    const todoForm = document.getElementById('todoForm');
    const todoList = document.getElementById('todoList');
    const childrenList = document.getElementById('childrenList');
    const addChildBtn = document.getElementById('addChildBtn');
    const addChildForm = document.getElementById('addChildForm');
    const notification = document.getElementById('notification');

    // State Management
    let currentUser = null;
    let todos = [];
    let children = [];

    // Notification Function
    function showNotification(message, type = 'success') {
        notification.textContent = message;
        notification.className = `notification alert alert-${type}`;
        notification.style.display = 'block';
        setTimeout(() => {
            notification.style.display = 'none';
        }, 3000);
    }

    // Authentication Functions
    function handleLogin(e) {
        e.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // In reality, this would be an API call to Django backend
        fetch('/api/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password })
        })
        .then(response => response.json())
        .then(data => {
            currentUser = username;
            loginSection.classList.add('d-none');
            todoSection.classList.remove('d-none');
            logoutBtn.classList.remove('d-none');
            showNotification('Successfully logged in!');
            fetchTodos();
            fetchChildren();
        })
        .catch(error => {
            showNotification('Login failed!', 'danger');
        });
    }

    function handleLogout() {
        fetch('/api/logout/', {
            method: 'POST'
        })
        .then(() => {
            currentUser = null;
            todos = [];
            children = [];
            loginSection.classList.remove('d-none');
            todoSection.classList.add('d-none');
            logoutBtn.classList.add('d-none');
            showNotification('Successfully logged out!');
        });
    }

    // Todo Functions
    function createTodoElement(todo) {
        const div = document.createElement('div');
        div.className = 'card mb-2';
        div.innerHTML = `
            <div class="card-body">
                <h5 class="card-title">${todo.title}</h5>
                <p class="card-text">${todo.description}</p>
                ${todo.assignedChild ? `<small class="text-muted">Assigned to: ${todo.assignedChild}</small>` : ''}
                <div class="mt-2">
                    <button class="btn btn-sm btn-primary edit-todo" data-id="${todo.id}">Edit</button>
                    <button class="btn btn-sm btn-danger delete-todo" data-id="${todo.id}">Delete</button>
                </div>
            </div>
        `;
        return div;
    }

    function fetchTodos() {
        // In reality, this would be an API call to Django backend
        fetch('/api/todos/')
            .then(response => response.json())
            .then(data => {
                todos = data;
                renderTodos();
            });
    }

    function addTodo(e) {
        e.preventDefault();
        const title = document.getElementById('todoTitle').value;
        const description = document.getElementById('todoDescription').value;
        const assignedChild = document.getElementById('assignedChild').value;

        fetch('/api/todos/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title, description, assignedChild })
        })
        .then(response => response.json())
        .then(data => {
            todos.push(data);
            renderTodos();
            todoForm.reset();
            showNotification('Todo added successfully!');
        });
    }

    // Children Functions
    function createChildElement(child) {
        const div = document.createElement('div');
        div.className = 'card mb-2';
        div.innerHTML = `
            <div class="card-body d-flex justify-content-between align-items-center">
                <span>${child.name}</span>
                <button class="btn btn-sm btn-danger delete-child" data-id="${child.id}">Delete</button>
            </div>
        `;
        return div;
    }

    function fetchChildren() {
        fetch('/api/children/')
            .then(response => response.json())
            .then(data => {
                children = data;
                renderChildren();
                updateChildrenSelect();
            });
    }

    function addChild(e) {
        e.preventDefault();
        const name = document.getElementById('childName').value;

        fetch('/api/children/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name })
        })
        .then(response => response.json())
        .then(data => {
            children.push(data);
            renderChildren();
            updateChildrenSelect();
            bootstrap.Modal.getInstance(document.getElementById('addChildModal')).hide();
            addChildForm.reset();
            showNotification('Child added successfully!');
        });
    }

    // Render Functions
    function renderTodos() {
        todoList.innerHTML = '';
        todos.forEach(todo => {
            todoList.appendChild(createTodoElement(todo));
        });
    }

    function renderChildren() {
        childrenList.innerHTML = '';
        children.forEach(child => {
            childrenList.appendChild(createChildElement(child));
        });
    }

    function updateChildrenSelect() {
        const select = document.getElementById('assignedChild');
        select.innerHTML = '<option value="">Select a child</option>';
        children.forEach(child => {
            const option = document.createElement('option');
            option.value = child.id;
            option.textContent = child.name;
            select.appendChild(option);
        });
    }

    // Event Listeners
    loginForm.addEventListener('submit', handleLogin);
    logoutBtn.addEventListener('click', handleLogout);
    todoForm.addEventListener('submit', addTodo);
    addChildForm.addEventListener('submit', addChild);

    // Delete event listeners using event delegation
    todoList.addEventListener('click', e => {
        if (e.target.classList.contains('delete-todo')) {
            const todoId = e.target.dataset.id;
            fetch(`/api/todos/${todoId}/`, {
                method: 'DELETE'
            })
            .then(() => {
                todos = todos.filter(todo => todo.id !== todoId);
                renderTodos();
                showNotification('Todo deleted successfully!');
            });
        }
    });

    childrenList.addEventListener('click', e => {
        if (e.target.classList.contains('delete-child')) {
            const childId = e.target.dataset.id;
            fetch(`/api/children/${childId}/`, {
                method: 'DELETE'
            })
            .then(() => {
                children = children.filter(child => child.id !== childId);
                renderChildren();
                updateChildrenSelect();
                showNotification('Child removed successfully!');
            });
        }
    });
});