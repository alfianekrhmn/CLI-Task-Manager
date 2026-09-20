# 📝 CLI Task Manager (Python & JSON)

A persistent Command-Line Interface (CLI) Task Manager built with Python. This application allows users to manage daily tasks using CRUD (Create, Read, Update, Delete) operations, with data stored persistently in a local JSON file.

## 🚀 Features

- **Persistent Data Storage**: Automatically save and load tasks using `task.json`.
- **View Tasks (Read)**: Display all recorded tasks with their IDs and completion statuses.
- **Add Tasks (Create)**: Add new tasks with auto-incremented IDs and a default status.
- **Update Tasks (Update)**: Modify task titles or mark tasks as completed.
- **Delete Tasks (Delete)**: Remove tasks from the task list.
- **CLI Interface**: Manage tasks through a simple command-line interface.

## 🛠️ Requirements

- Python 3.x installed on your system.
- Basic knowledge of running Python applications through the terminal.

## 📂 Project Structure

    cli-task-manager/
    │
    ├── main.py
    ├── task.json
    └── README.md

## 💻 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/alfianekrhmn/cli-task-manager.git
```

### 2. Navigate to the Project Directory

```bash
cd cli-task-manager
```

### 3. Run the Application

```bash
python main.py
```

## 🎮 Usage Guide

After running the application, select an option from the available menu:

| Option | Action | Description |
|--------|--------|-------------|
| 1 | View Tasks | Display all tasks and their completion statuses. |
| 2 | Add Task | Add a new task with a title. |
| 3 | Delete Task | Delete a task using its ID or index. |
| 4 | Update Task | Update a task title or mark it as completed. |
| 5 | Exit | Exit the application. |

## 💾 Data Storage

Task data is stored locally in a JSON file named `task.json`.

The application uses this file to maintain task data between executions, allowing users to access previously saved tasks after restarting the program.

## 📚 Concepts Practiced

This project was built to practice fundamental Python programming concepts, including:

- CRUD operations.
- File handling.
- JSON data processing.
- Functions and modular programming.
- Loops and conditional statements.
- User input validation.
- Persistent local data storage.

## 🔮 Future Improvements

Potential improvements for future versions:

- Add task priority levels.
- Add task deadlines.
- Implement task search functionality.
- Add task filtering by completion status.
- Improve input validation and error handling.

## 📄 License

This project is open source and available under the MIT License.