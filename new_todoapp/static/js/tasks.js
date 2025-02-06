document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.delete-task').forEach(btn => {
        btn.addEventListener('click', async (e) => {
            if (confirm('Are you sure you want to delete this task?')) {
                const response = await fetch(`/tasks/delete/${e.target.dataset.taskId}/`, {
                    method: 'POST',
                    headers: {'X-CSRFToken': getCookie('csrftoken')}
                });
                
                if (response.ok) {
                    e.target.closest('.task-item').remove();
                    showNotification('Task deleted successfully');
                }
            }
        });
    });
});

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

function showNotification(message, type='success') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} notification shadow`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    setTimeout(() => notification.remove(), 3000);
}

function addChild() {
    const childrenContainer = document.getElementById('children-container');
    const newChild = document.createElement('div');
    newChild.className = 'mb-3 child-entry';
    newChild.innerHTML = `
        <input type="text" class="form-control" name="child_name" required 
               placeholder="Child's name">
        <button type="button" class="btn btn-danger btn-sm mt-2" 
                onclick="this.parentElement.remove()">Remove</button>
    `;
    childrenContainer.appendChild(newChild);
}