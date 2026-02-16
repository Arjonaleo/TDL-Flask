from flask import Flask, request, jsonify, render_template, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
DATABASE = 'database.db'

# ========================================
# FUNCIONES DE BASE DE DATOS
# ========================================

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

# ========================================
# RUTA TEMPORAL PARA PROBAR
# ========================================

@app.route('/')
def index():
    """Página principal - temporal"""
    return "<h1>Sistema de Tareas - En construcción</h1>"

# ========================================
# EJECUTAR LA APLICACIÓN
# ========================================

if __name__ == '__main__':
    app.run(debug=True)