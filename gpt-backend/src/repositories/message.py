from src.models.message import Message
from src.repositories.sqlalchemy import BaseSQLAlchemyRepository
from src.schemas.message import IMessageCreate, IMessageUpdate


class MessageRepository(BaseSQLAlchemyRepository[Message, IMessageCreate, IMessageUpdate]):
    _model = Message
