# 📝 To-Do List App (Python)

A simple **Command-Line To-Do List Application** built using **Python** and **JSON**. This project allows users to manage their daily tasks by adding, viewing, searching, marking tasks as completed, and deleting tasks. All task data is stored permanently in a JSON file, so your tasks are available even after restarting the program.

---

## 🚀 Features

- ➕ Add a New Task
- 📋 View All Tasks
- 🔍 Search a Task by Name
- ✅ Mark a Task as Completed
- 🗑️ Delete a Task
- 💾 Automatically Save Tasks in a JSON File
- 📂 Automatically Load Saved Tasks on Startup
- ⚠️ Handles Missing or Empty JSON Files Using Exception Handling

---

## 🛠️ Technologies Used

- Python 3
- JSON
- File Handling
- Exception Handling (`try` / `except`)

---

## 📂 Project Structure

```
todo_project/
│
├── todo.py          # Main Python Program
├── todo.json        # Stores All Tasks
└── README.md        # Project Documentation
```

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Gauravdev28/todo_project.git
```

### 2. Navigate to the Project Folder

```bash
cd todo_project
```

### 3. Run the Application

```bash
python todo.py
```

---

## 📸 Application Menu

```
========== TO DO LIST ==========

1. Add Task
2. View Tasks
3. Search Task
4. Mark Task Completed
5. Delete Task
6. Exit
```

---

## 📄 Example JSON Data

```json
[
    {
        "task": "Learn Python",
        "status": "Pending"
    },
    {
        "task": "Complete DSA",
        "status": "Completed"
    }
]
```

---

## 📚 Concepts Used

This project helped me practice and improve my understanding of:

- Variables
- Lists
- Dictionaries
- Loops
- Conditional Statements
- Functions
- File Handling
- JSON (`json.load()` & `json.dump()`)
- Exception Handling
- CRUD Operations (Create, Read, Update, Delete)


---

## 🎯 Learning Outcomes

While building this project, I learned:

- Working with JSON files for data storage
- Reading and writing files in Python
- Using exception handling to prevent program crashes
- Managing data using lists and dictionaries
- Implementing CRUD operations
- Building menu-driven command-line applications
- Writing clean and organized Python code

---

## 👨‍💻 Author

**Gaurav Agarwal**

🎓 B.Tech AIML Student

🔗 GitHub: https://github.com/Gauravdev28

---

## ⭐ Support

If you found this project useful or learned something from it, please consider giving it a ⭐ on GitHub.

Your support is appreciated!
