'''Here we are using model validator to validate 
the data whre the model validator is used to 
validate the data of multiple instance of the model'''


from pydantic import BaseModel, Field, field_validator, EmailStr, AnyUrl, model_validator
import json
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr
    linkedin_url: AnyUrl
    gender: str
    weight_kg: float
    height_cm: float
    bmi: float
    allergies: List[str]
    contact_number: Dict[str, str]
    married: Optional[bool] = None

    @model_validator(mode = 'after')# mode after means it will validate the data after the type checking performed by pydantic
    def emergency_contact(cls,model):
        if model.age >=60 and 'emergency' not in model.contact_number:
            raise ValueError("Emergency contact is required for patients above 60 years of age")
        return model



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

patient_info = {
      "id": 6,
      "name": "Pooja Patel",
      "age": 72,
      "email": "abc@sbi.com", # this email is invalid because the domain is not in the valid domains
      "linkedin_url": "https://www.linkedin.com/in/poojapatel",
      "gender": "Female",
      "weight_kg": 65,
      "height_cm": 165,
      "bmi": 23.9,
      "allergies": [
        "Peanut Allergy",
        "Dust Allergy"
      ],
      "contact_number": {
        "phone": "987-654-3210",
        "emergency": "123-456-7890"
      }
}

# Validate and create a Pydantic model instance
try:
    patient1 = Patient(**patient_info)
    insert_patient_data(patient1)
except Exception as e:
    print(f"Validation Error: {e}")