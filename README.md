# Healthcare Backend API

A Django REST Framework backend for managing patients, doctors, and their assignments, secured with JWT authentication.

---

## Tech Stack

- **Django** + **Django REST Framework**
- **PostgreSQL**
- **JWT** via `djangorestframework-simplejwt`

---

## Project Structure

```
healthcare/          ← Django project config
api/
  models.py         ← Patient, Doctor, PatientDoctorMapping
  serializers.py    ← Input validation + output formatting
  views.py          ← All API logic
  urls.py           ← API routes
requirements.txt
.env                ← Environment variables (never commit)
```

---

## Setup & Run

### 1. Clone & install dependencies

```bash
git clone <repo-url>
cd healthcare-backend
pip install -r requirements.txt
```

### 2. Configure environment variables

Create a `.env` file in the root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

### 3. Create the database

```bash
psql -U postgres -c "CREATE DATABASE healthcare_db;"
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start the server

```bash
python manage.py runserver
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| POST | `/api/auth/register/` | No | Register a new user |
| POST | `/api/auth/login/` | No | Login and get JWT token |

### Patients

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| POST | `/api/patients/` | Yes | Create a patient |
| GET | `/api/patients/` | Yes | Get all patients (by logged-in user) |
| GET | `/api/patients/<id>/` | Yes | Get a specific patient |
| PUT | `/api/patients/<id>/` | Yes | Update a patient |
| DELETE | `/api/patients/<id>/` | Yes | Delete a patient |

### Doctors

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| POST | `/api/doctors/` | Yes | Add a new doctor |
| GET | `/api/doctors/` | Yes | Get all doctors |
| GET | `/api/doctors/<id>/` | Yes | Get a specific doctor |
| PUT | `/api/doctors/<id>/` | Yes | Update a doctor |
| DELETE | `/api/doctors/<id>/` | Yes | Delete a doctor |

### Patient-Doctor Mappings

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| POST | `/api/mappings/` | Yes | Assign a doctor to a patient |
| GET | `/api/mappings/` | Yes | Get all mappings |
| GET | `/api/mappings/<patient_id>/` | Yes | Get all doctors for a patient |
| DELETE | `/api/mappings/<id>/delete/` | Yes | Remove a doctor from a patient |

---

## Request & Response Examples

### Register
```http
POST /api/auth/register/
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "secret123"
}
```
Response `201`:
```json
{ "message": "User registered successfully.", "user_id": 1 }
```

---

### Login
```http
POST /api/auth/login/
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "secret123"
}
```
Response `200`:
```json
{
  "access": "<JWT_ACCESS_TOKEN>",
  "refresh": "<JWT_REFRESH_TOKEN>"
}
```

---

### Create Patient
```http
POST /api/patients/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "name": "Jane Smith",
  "age": 30,
  "gender": "Female",
  "medical_history": "Diabetes Type 2"
}
```

---

### Create Doctor
```http
POST /api/doctors/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "name": "Dr. Mehta",
  "specialization": "Cardiology",
  "experience_years": 10
}
```

---

### Assign Doctor to Patient
```http
POST /api/mappings/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "patient": 1,
  "doctor": 1
}
```

---

## Using JWT Token

After login, include the access token in all protected requests:

```
Authorization: Bearer <your_access_token>
```

Tokens expire after **1 day**. Use the refresh token to get a new access token.

