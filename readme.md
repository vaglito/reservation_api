# API de reservas - Django Rest Framework


## Tecnologias
- Python
- Django
- Django Rest Framework
- SimpleJWT
- SQLite (por defecto)


---

## 🔧 Instalación

```bash
# Clona el proyecto
git clone https://github.com/vaglito/reservation_api.git
cd api-reservas

# Crea un entorno virtual
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

# Instala las dependencias
pip install -r requirements.txt

# Aplica las migraciones
python manage.py migrate

# Crea un superusuario (necesario para entrar al panel administrativo de la api)
python manage.py createsuperuser

# Ejecuta el servidor
python manage.py runserver
```

---

## endpoint

| endpoint | metodo     | Description                |
| :-------- | :------- | :------------------------- |
| `/api/users/register/` | `POST` | Registra nuevos usuarios |

### Cuerpo 
```json
{
  "username": "paula",
  "password": "admin1234",
  "password2": "admin1234",
  "email": "paula@example.com",
  "first_name": "Paula",
  "last_name": "Cornatero"
}
```

| endpoint | metodo     | Description                |
| :-------- | :------- | :------------------------- |
| `/api/users/login/` | `POST` | Logea un usuario |

### Cuerpo 
```json
{
  "username": "paula",
  "password": "admin1234"
}
```

### Repuesta

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MTc0NzMwMSwiaWF0IjoxNzUxNjYwOTAxLCJqdGkiOiIxN2Y3YmU2OTdlZjU0YTA4YTRiMzUzYjAyZTg1N2Y3ZiIsInVzZXJfaWQiOjF9._9y-ZqMysa4NuTIsqd6of-FzHY5ZqUxK3y_vpYCHLaQ",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUxNzQ3MzAxLCJpYXQiOjE3NTE2NjA5MDEsImp0aSI6ImIzMTU0YzMxYTNhNTQ3ZGFiZTNmNDEyYzBlY2Q1YTgwIiwidXNlcl9pZCI6MX0.op2D3QY-pdpzmjsR_4z1UM0-R9VhIYloZx4cfSIL5Wo"
}
```

| endpoint | metodo     | Description                |
| :-------- | :------- | :------------------------- |
| `/api/reservations/` | `CRUD` | Crea, actualiza, elimina, consulta reservas. (debe estar logeado) |

### Authorization headers
```json
{
    "headers" {
        "barear": {token} 
    }
}
```