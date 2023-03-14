import uuid
import datetime
from pydantic import BaseModel, validator

from .PropertyValueDataTypes import DateTime

class Event(BaseModel):
    summary: str
    description: str = None
    start: str

    @property
    def uid(self) -> str:
        return uuid.uuid3(self)
    
    @property
    def created(self) -> DateTime:
        return DateTime(time=datetime.datetime.now())
    
    @property
    def stamp(self) -> DateTime:
        return DateTime(time=datetime.datetime.now())
    
    def __init__(self, **data) -> None:
        super().__init__(**data)

    def __repr__(self) -> str:
        return f"""Event({self.summary=}, {self.uid=})"""

    def __str__(self) -> str:
        return (
            f"""BEGIN:VEVENT"""
            f"""TDSTAMP:{self.stamp}"""
            f"""UID:{self.uid}""" 
            f"""DTSTART:{self.start}"""
            f"""CREATED:{self.created}"""
            f"""SUMMARY:{self.summary}"""
            f"""DESCRIPTION:{self.description}"""
            f"""END:VEVENT"""
        )
