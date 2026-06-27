## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Chetanyadavannavar/django-todo-app.git
```

### 2. Move to the Project Folder

```bash
cd django-todo-app
```

### 3. Create a Virtual Environment

```bash
python -m venv myenv
```

### 4. Activate the Virtual Environment

**Windows**

```bash
myenv\Scripts\activate
```

**Linux / macOS**

```bash
source myenv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

> **If `requirements.txt` is not available, generate it using:**
>
> ```bash
> pip freeze > requirements.txt
> ```

### 6. Apply Migrations

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
