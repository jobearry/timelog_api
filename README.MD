# FastAPI Jobry

A simple FastAPI project.

## Setup

1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd fastapi_jobry
   ```

2. **Create and activate a virtual environment**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

Start the FastAPI server with:

```sh
uvicorn main:app --reload
```

- Open your browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- API docs available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Project Structure

```
fastapi_jobry/
├── main.py
├── requirements.txt
└── README.MD
```