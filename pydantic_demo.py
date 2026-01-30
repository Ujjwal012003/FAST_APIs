from pydantic import BaseModel, EmailStr, AnyUrl, Field
import json
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    id: int
    name: Annotated[str, Field(max_length=50, title="Name", description="Name of the patient")]
    age: int
    linkedin_url: AnyUrl
    email: EmailStr
    gender: str
    weight_kg: float = Field(..., gt=0)
    height_cm: float = Field(..., gt=0)
    bmi: float
    allergies: Annotated[List[str], Field(default = None, min_length=1)]
    contact_number: Dict[str, str]
    married: Optional[bool] = None

def load_json(filename: str):
    with open(filename, "r") as f:
        return json.load(f)

def insert_patient_data(patient: Patient):
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Gender: {patient.gender}")
    print(f"Weight: {patient.weight_kg}")
    print(f"Height: {patient.height_cm}")
    print(f"BMI: {patient.bmi}")
    print(f"Allergies: {patient.allergies}")
    print(f"Contact Number: {patient.contact_number}")
    print(f"Married: {patient.married}")
    print(f"Email: {patient.email}")
    print(f"Linkedin URL: {patient.linkedin_url}")
    print("inserted")

data = load_json("patients.json")

# Extract the first patient from the list in the JSON
patient_dict = data["patients"][5]

# Validate and create a Pydantic model instance
patient1 = Patient(**patient_dict)

insert_patient_data(patient1)