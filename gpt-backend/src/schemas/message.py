from uuid import UUID

from src.models.message import MessageBase


class IMessageCreate(MessageBase):
    pass


class IMessageRead(MessageBase):
    ref_id: UUID


class IMessageUpdate(MessageBase):
    pass
