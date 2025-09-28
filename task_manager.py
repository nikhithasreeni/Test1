from db_config import get_connection

class TaskManager:

    # Fetch all tasks
    def get_tasks(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title FROM tasks")
        tasks = cursor.fetchall()
        conn.close()
        return tasks

    # Add a task
    def add_task(self, title):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
        conn.commit()
        conn.close()
        self.generate_html()  # Auto-update HTML

    # Update a task
    def update_task(self, task_id, new_title):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET title=%s WHERE id=%s", (new_title, task_id))
        conn.commit()
        conn.close()
        self.generate_html()  # Auto-update HTML

    # Delete a task
    def delete_task(self, task_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
        conn.commit()
        conn.close()
        self.generate_html()  # Auto-update HTML

    # Generate HTML from tasks
    def generate_html(self):
        tasks = self.get_tasks()
        html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>To-Do List</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
    <h1>My To-Do List</h1>
"""

        for task in tasks:
            html_content += f"""
    <div class="task">
        <span>{task[0]}. {task[1]}</span>
        <div class="buttons">
            <button>Update</button>
            <button>Delete</button>
        </div>
    </div>
"""

        html_content += """
</div>
</body>
</html>
"""
        with open("index.html", "w") as f:
            f.write(html_content)
        print("index.html generated successfully!")
