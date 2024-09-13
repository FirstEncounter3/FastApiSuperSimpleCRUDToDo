from typing import Optional

from fastapi import Form
from pydantic import BaseModel

class ToDo(BaseModel):
    id: Optional[int] = None
    item: str

    @classmethod
    def as_form(
        cls, 
        item: str = Form(...)
    ):
        return cls(item=item)

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

class ToDoItems(BaseModel):
    todos: list[ToDoItem]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "todos": [
                        {
                            "item": "example schema 1"
                        },
                        {
                            "item": "example schema 2"
                        }
                    ]
                }
            ]
        }
    }