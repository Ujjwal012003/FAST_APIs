# FastAPI Patient Management System

A robust REST API built with FastAPI to manage and sort patient records.

## Features
- **View All Patients**: Retrieve a list of all patients from the system.
- **Patient Lookup**: Get detailed info for a specific patient by ID (includes validation).
- **Advanced Sorting**: Sort patients by Weight, Height, or BMI in Ascending/Descending order.
- **Error Handling**: Proper HTTP 404/400 validation errors.

## Tech Stack
- Python 3.x
- FastAPI
- Uvicorn

## How to Run

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Server**
   ```bash
   uvicorn main:app --reload
   ```

3. **Open OpenAPI Documentation**
   Go to `http://127.0.0.1:8000/docs` to test the API interactively.
