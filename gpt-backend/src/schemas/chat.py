from uuid import UUID

from src.models.chat import ChatBase


class IChatCreate(ChatBase):
    pass


class IChatRead(ChatBase):
    ref_id: UUID
    id: int


class IChatUpdate(ChatBase):
    pass
