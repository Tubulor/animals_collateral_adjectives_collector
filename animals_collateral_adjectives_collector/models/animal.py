from pydantic import BaseModel

class Animal(BaseModel):
    name: str
    data_url: str
    image_local_path: str = None
