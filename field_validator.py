'''Here we are using field validator to validate 
the data whre the field validator is used to 
validate the data of single instance of the model'''


from pydantic import BaseModel, Field, field_validator, EmailStr, AnyUrl
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

    @field_validator('email') # here we are validating the email field
    @classmethod
    def validate_emails(cls, value):
        valid_domains = ["hdfc.com", "icici.com", "sbi.com"]
        if "@" in value:
            domain = value.split("@")[-1]
            if domain not in valid_domains:
                raise ValueError("Invalid email domain")
        return value

    @field_validator('name') # here we are validating the name field
    @classmethod
    def validate_name(cls, value):
        
        return value.upper()  

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
      "age": 31,
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
        "phone": "987-654-3210"
      }
}

# Validate and create a Pydantic model instance
try:
    patient1 = Patient(**patient_info)
    insert_patient_data(patient1)
except Exception as e:
    print(f"Validation Error: {e}")