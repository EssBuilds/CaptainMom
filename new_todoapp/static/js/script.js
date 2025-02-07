// Task Management Logic
document.addEventListener("DOMContentLoaded", () => {
    const taskForm = document.getElementById("task-form");
    const taskList = document.getElementById("task-list");
  
    // Array to store tasks (temporary storage)
    let tasks = [];
  
    // Handle Form Submission
    taskForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const taskName = document.getElementById("task-name").value.trim();
      if (taskName) {
        addTask(taskName);
        taskForm.reset();
      }
    });
  
    // Add Task to the List
    function addTask(name) {
      const task = { id: Date.now(), name };
      tasks.push(task);
      renderTasks();
      notifyUser(`${name} has been added!`);
    }
  
    // Render Tasks
    function renderTasks() {
      taskList.innerHTML = "";
      tasks.forEach((task) => {
        const li = document.createElement("li");
        li.className = "list-group-item d-flex justify-content-between align-items-center";
        li.innerHTML = `
          ${task.name}
          <button class="btn btn-danger btn-sm delete-btn" data-id="${task.id}">Delete</button>
        `;
        taskList.appendChild(li);
  
        // Delete Task
        li.querySelector(".delete-btn").addEventListener("click", () => {
          deleteTask(task.id);
        });
      });
    }
  
    // Delete Task
    function deleteTask(id) {
      tasks = tasks.filter((task) => task.id !== id);
      renderTasks();
      notifyUser("Task deleted successfully!");
    }
  
    // Notify User
    function notifyUser(message) {
      alert(message); // Replace with a better notification system in production
    }
  });