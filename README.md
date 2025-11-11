
# CLI TODO  

A simple command‑line to‑do list application written in Python.

## 🧰 Features  
- Manage your to‑do items from the command line in a lightweight way.  
- Add tasks, list tasks, mark them complete (or delete) — minimal overhead, maximum productivity.  
- No GUI, no web‑server: just you, the terminal, and your tasks.

## 💡 Getting Started  

### Requirements  
- Python 3.x (tested on Python 3.x)  
- Basic familiarity with the command line.

### Installation  
1. Clone the repository  
   ```bash
   git clone https://github.com/Neraxd/cli_todo.git
   cd cli_todo
   ```  
2. (Optional) Create and activate a virtual environment:  
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```  
3. Install dependencies (if any).  
   _Note: At present no external libraries are required._  
   ```bash
   pip install -r requirements.txt   # if you add dependencies
   ```
4. Run the application  
   ```bash
   python todo_app.py
   ```

## 🚀 Usage  
Once you launch `todo_app.py`, you’ll be prompted (or you’ll use command‑line options) to perform tasks like:  
- **Add** a new to‑do item  
- **List** all current to‑do items  
- **Mark** an item as completed / **delete** an item  
- (Potentially) **filter** or **sort** tasks by date or status  

> _Example session:_  
> ```bash
> $ python todo_app.py
> Welcome to CLI TODO!
> 1) Add a task
> 2) List tasks
> 3) Mark task done / Delete task
> Choose an option: 2
> 1. [ ] Buy groceries
> 2. [x] Finish project write‑up
> Choose an option: 1
> Task “Buy groceries” marked done.
> ```

## 🛠 Planned Improvements  
Here are some ideas to extend the tool (and contributions are very welcome):  
- Persist tasks to a file (JSON, YAML or SQLite) so they survive after the program exits.  
- Add support for priorities, due‑dates, tags, and filtering.  
- Implement command‑line flags (e.g., `todo add "Call mom"`, `todo list --pending`).  
- Improve UI/UX: nicer formatting, colors, interactive prompts.  
- Package it as an installable Python module (via `pip install cli_todo`).  

## 📬 Contact  
Created by [@Neraxd](https://github.com/Neraxd). Thank you for using CLI TODO — happy task managing!
