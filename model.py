from pydantic import BaseModel

class ToDo(BaseModel):
    id: int
    item: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "item": "example schema create todo"
                }
            ]
        }
    }

class ToDoItem(BaseModel):
    item: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "item": "example schema update todo"
                }
            ]
        }
    }