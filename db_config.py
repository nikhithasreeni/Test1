import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="system@123",  # replace with your MySQL password
        database="todo_db"
    )
