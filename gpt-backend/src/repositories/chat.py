from src.models.chat import Chat
from src.repositories.sqlalchemy import BaseSQLAlchemyRepository
from src.schemas.chat import IChatCreate, IChatUpdate


class ChatRepository(BaseSQLAlchemyRepository[Chat, IChatCreate, IChatUpdate]):
    _model = Chat