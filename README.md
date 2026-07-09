# Task Manager — TDL Flask App

> A full-stack task management web application built with Python and Flask, featuring complete CRUD functionality for personal productivity.



---

##  Live Demo

<!-- ✏️ Si haces deploy en Railway o Render, pon aquí el link: -->
<!-- [🚀 Ver demo en vivo](https://tu-app.railway.app) -->

> Deploy pendiente — ver instrucciones de instalación abajo.

---

##  Features

-  Create new tasks with title and description
-  Edit existing tasks inline
-  Mark tasks as complete / incomplete
-  Delete tasks
-  Server-side rendered templates with Jinja2
<!-- ✏️ Agrega features adicionales si las tienes, por ejemplo:
  - 🔐 User authentication (login/register)
  - 📅 Due date and priority system
  - 🗂️ Task categories or labels
-->

---

##  Tech Stack

| Layer       | Technology               |
|------------|--------------------------|
| Backend     | Python 3 · Flask         |
| Templating  | Jinja2 (HTML5)           |
| Styling     | CSS3                     |
| Database    | SQLite / SQLAlchemy      |
| Versioning  | Git / GitHub             |

<!-- ✏️ Si usas MySQL en lugar de SQLite, actualiza la fila de Database arriba -->

---

##  Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Arjonaleo/TDL-Flask.git
cd TDL-Flask

# 2. Create and activate a virtual environment
python -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the development server
flask run
```

The app will be available at `http://127.0.0.1:5000`

---

##  Project Structure

```
TDL-Flask/
├── app.py              # Main Flask application and routes
├── requirements.txt    # Python dependencies
├── templates/          # Jinja2 HTML templates
│   ├── base.html
│   ├── index.html
│   └── edit.html
└── static/             # CSS and static assets
    └── style.css
```

<!-- ✏️ Ajusta esta estructura si la tuya es diferente -->

---

##  Routes

| Method | Route          | Description              |
|--------|---------------|--------------------------|
| GET    | `/`           | Display all tasks        |
| POST   | `/add`        | Create a new task        |
| GET    | `/edit/<id>`  | Load edit form for task  |
| POST   | `/update/<id>`| Save changes to a task   |
| GET    | `/delete/<id>`| Delete a task            |

<!-- ✏️ Ajusta estas rutas según las que realmente implementaste -->

---

##  What I learned

- Building RESTful routes with Flask's routing system
- Working with Jinja2 templating for server-side rendering
- Handling HTTP methods (GET/POST) for form submission
- Managing a simple relational data model with SQLite
- Structuring a Flask project with separation of concerns

---

##  Author

**Leonardo Arjona Ramírez**

- GitHub: [@Arjonaleo](https://github.com/Arjonaleo)
- LinkedIn: [linkedin.com/in/leonardo-arjona](https://linkedin.com/in/leonardo-arjona)

<!-- ✏️ Actualiza el link de LinkedIn cuando lo tengas listo -->

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
