import time
import datetime

from typing import Optional

from pydantic import BaseModel, validator


class DateTime(BaseModel):
    time: datetime.datetime

    @validator('time', pre=True)
    def time_validator(cls, v):
        match v:
            case datetime.datetime():
                return v
            case int() | float():
                return datetime.datetime.fromtimestamp(v)
            case str():
                return datetime.datetime.fromisoformat(v)
            case _:
                raise ValueError(f"Invalid type for {v=}")
    



class Duration(BaseModel):
    start: DateTime
    end: DateTime