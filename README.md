#  FastAPI Practice 

##  Features

*  Path Parameters
*  Query Parameters
*  POST API (Create data)
*  PUT API (Update data)
*  Request Body using Pydantic
*  Automatic Validation & Error Handling
*  Interactive API Docs using Swagger UI

---

##  Tech Stack

* Python
* FastAPI
* Uvicorn
* Pydantic

---

##  How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fastapi-practice.git
cd fastapi-practice
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate environment

```bash
.venv\Scripts\activate   # Windows
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn
```

### 5. Run the server

```bash
uvicorn main:app --reload
```

---

##  API Documentation

Once the server is running, open:

 http://127.0.0.1:8000/docs

This provides an interactive Swagger UI to test all APIs.

---

##  Example Endpoints

### GET with Path Parameter

```
/items/{item_id}
```

### GET with Query Parameter

```
/items/{item_id}?q=search
```

### POST Request

```
/items/
```

### PUT Request

```
/items/{item_id}
```

---

##  What I Learned

* Building APIs using FastAPI
* Using path and query parameters
* Handling request bodies with Pydantic
* Automatic validation and error handling
* Testing APIs using Swagger UI

---

##  Future Improvements

* Add PATCH and DELETE APIs
* Integrate database (SQLite/PostgreSQL)
* Implement full CRUD operations
* Add authentication

---


