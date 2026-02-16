from flask import Flask, request, jsonify, render_template, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
DATABASE = 'database.db'


def get_db():
    """Conecta a la base de datos SQLite"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Permite acceder a columnas por nombre
    return conn

def init_db():
    """Inicializa las tablas de la base de datos"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Tabla de usuarios
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    
    # Tabla de categorías
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            color TEXT NOT NULL
        )
    """)
    
    # Tabla de tareas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            user_id INTEGER NOT NULL,
            category_id INTEGER,
            completed BOOLEAN DEFAULT 0,
            created_at TEXT NOT NULL,
            due_date TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (category_id) REFERENCES categories (id)
        )
    """)
    
    # Insertar un usuario por defecto
    cursor.execute("SELECT COUNT(*) as count FROM users")
    if cursor.fetchone()['count'] == 0:
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            ('Usuario Demo', 'demo@todo.com', 'demo123')
        )
    
    # Insertar categorías por defecto
    cursor.execute("SELECT COUNT(*) as count FROM categories")
    if cursor.fetchone()['count'] == 0:
        categorias_default = [
            ('Trabajo', '#FF6B6B'),
            ('Personal', '#4ECDC4'),
            ('Estudio', '#45B7D1'),
            ('Hogar', '#FFA07A')
        ]
        cursor.executemany(
            "INSERT INTO categories (name, color) VALUES (?, ?)",
            categorias_default
        )
    
    conn.commit()
    conn.close()

# Inicializar la base de datos al arrancar
init_db()





@app.route('/')
def index():
    """Página principal - Dashboard con estadísticas"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Contar total de tareas
    cursor.execute("SELECT COUNT(*) as count FROM tasks")
    total_tasks = cursor.fetchone()['count']
    
    # Contar tareas completadas
    cursor.execute("SELECT COUNT(*) as count FROM tasks WHERE completed = 1")
    completed_tasks = cursor.fetchone()['count']
    
    # Calcular pendientes
    pending_tasks = total_tasks - completed_tasks
    
    conn.close()
    
    return render_template('index.html', 
                         total_tasks=total_tasks,
                         completed_tasks=completed_tasks,
                         pending_tasks=pending_tasks)

@app.route('/tasks')
def tasks_page():
    """Página que muestra todas las tareas"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Obtener todas las tareas con información de categoría
    cursor.execute("""
        SELECT tasks.*, categories.name as category_name, categories.color as category_color
        FROM tasks
        LEFT JOIN categories ON tasks.category_id = categories.id
        ORDER BY tasks.created_at DESC
    """)
    tasks = cursor.fetchall()
    
    conn.close()
    
    return render_template('tasks.html', tasks=tasks)

@app.route('/task/create')
def create_task_form():
    """Muestra el formulario para crear una tarea"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    
    conn.close()
    
    return render_template('create_task.html', categories=categories)

@app.route('/categories')
def categories_page():
    """Página de categorías - temporal"""
    return "<h1>Categorías - próximamente</h1>"


# CRUD - CREAR TAREAS


@app.route('/task/create', methods=['POST'])
def create_task():
    """Crea una nueva tarea en la base de datos"""
    title = request.form['title']
    description = request.form.get('description', '')  # Opcional
    category_id = request.form.get('category_id') or None
    due_date = request.form.get('due_date') or None
    
    # Por ahora, user_id será 1 (usuario demo)
    user_id = 1
    
    # Fecha de creación
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO tasks (title, description, user_id, category_id, created_at, due_date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (title, description, user_id, category_id, created_at, due_date))
    
    conn.commit()
    conn.close()
    
    return redirect(url_for('tasks_page'))


# MARCAR TAREA COMO COMPLETADA


@app.route('/task/toggle/<int:id>')
def toggle_task(id):
    """Marca o desmarca una tarea como completada"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Obtener el estado actual
    cursor.execute("SELECT completed FROM tasks WHERE id = ?", (id,))
    task = cursor.fetchone()
    
    if task:
        # Invertir el estado
        new_status = 0 if task['completed'] else 1
        
        cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (new_status, id))
        
        conn.commit()
    
    conn.close()
    
    return redirect(url_for('tasks_page'))

# Rutas temporales (se completarán en el día 4)
@app.route('/task/edit/<int:id>')
def edit_task_form(id):
    return "<h1>Editar tarea - próximamente</h1>"

@app.route('/task/delete/<int:id>')
def delete_task(id):
    return "<h1>Eliminar tarea - próximamente</h1>"

if __name__ == '__main__':
    app.run(debug=True)