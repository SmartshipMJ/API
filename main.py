from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/employees")
def read_employees(name: str):
    return {"message" : f"{name}님, 환영합니다"}

@app.get("/employees/{employee_id}")
def read_employee(employee_id: int):
    return {"employee_id": employee_id}