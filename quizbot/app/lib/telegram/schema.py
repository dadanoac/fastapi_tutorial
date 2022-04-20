from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# -----------------------------------------------------------------------------
# enums
# -----------------------------------------------------------------------------
class ChatType(str, Enum):
    private = "private"
    group = "group:"
    supergroup = "supergroup"
    channel = "channel"


# -----------------------------------------------------------------------------
# models
# -----------------------------------------------------------------------------
class User(BaseModel):
    id: str
    is_bot: bool
    first_name: str
    last_name: str
    username: Optional[str] = "NA"
    language_code: str


class Chat(BaseModel):
    id: int
    type: ChatType
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]


class Message(BaseModel):
    message_id: int
    from_: Optional[User] = Field(
        None,
        title="Sender",
        description="Sender, empty for messages sent to channels",
        alias="from",
    )
    chat: Chat
    date: datetime
    text: Optional[str] = Field(None, max_length=4096)


class Update(BaseModel):
    update_id: int
    message: Optional[Message]
