from pydantic import BaseConfig
from sqlmodel import Field, SQLModel

from src.models.base import BaseModel


class MessageBase(SQLModel):
    text: str = Field(...)
    type: str = Field(...)

    class Config(BaseConfig):
        json_encoder = {
            datetime: lambda dt: dt.replace(tzinfo=timezone.utc).isoformat(),
        }
        schema_extra = {
            "example": {
                "id": 1,
                "ref_id": "1234-43143-3134-13423",
                "created_at": "2004-09-16T23:59:58.75",
            }
        }


class Message(BaseModel, MessageBase, table=True):
    pass
