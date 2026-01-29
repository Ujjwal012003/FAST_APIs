from fastapi import FastAPI, HTTPException, Path, Query
import json
app = FastAPI()

def load_patients():
    with open("patients.json", 'r') as f:
        data = json.load(f)
        return data

@app.get("/")
def greet():
    return {"message": "Hello World"} 

@app.get("/about")
def about():
    return {"message": "About Page"}

@app.get("/view-patients")
def view():
    data = load_patients()
    return data

@app.get("/patient/{id}")    
def get_patient(id: int = Path(..., title="Patient ID", description="The ID of the patient to retrieve", ge=1, le=10)):
    data = load_patients()

    patients = data["patients"]
    for patient in patients:
        if patient["id"] == id:
            return patient

    raise HTTPException(status_code=404, detail="Patient not found")        
            
@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description = 'Sort on the basis of weight,height or bmi'),
order: str = Query('asc',description = 'Ascending or Descending')):
    valid_fields= ['weight_kg', 'height_cm', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field select from {valid_fields}")
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order")    

    data = load_patients()
    patients = data['patients']
    
    sort_order = True if order == 'desc' else False 

    sorted_patients = sorted(patients, key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_patients
    
    


