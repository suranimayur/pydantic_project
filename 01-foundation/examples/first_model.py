from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    name: str
    is_active: bool
    
    
input_data = {    "id": 1,
    "name": "John Doe","is_active": True}

user = User(**input_data)
print(user)
print(user.id)
print(user.name)















