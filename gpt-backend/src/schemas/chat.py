from uuid import UUID

from src.models.chat import ChatBase


class IChatCreate(ChatBase):
    pass


class IChatRead(ChatBase):
    ref_id: UUID


class IChatUpdate(ChatBase):
    pass
