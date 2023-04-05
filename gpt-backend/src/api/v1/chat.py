from typing import List, Optional

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.enums import SortOrder
from src.db.session import get_session
from src.repositories.chat import ChatRepository
from src.schemas.common import IGetResponseBase
from src.schemas.chat import IChatRead, IChatCreate, ChatBase

router = APIRouter()


@router.get(
    "/chats",
    response_description="List all chat instances",
    response_model=IGetResponseBase[List[IChatRead]],
    tags=["chats"],
)
async def chats(
        skip: int = Query(0, ge=0),
        limit: int = Query(50, ge=1),
        sort_field: Optional[str] = "created_at",
        sort_order: Optional[str] = SortOrder.DESC,
        session: AsyncSession = Depends(get_session),
) -> IGetResponseBase[List[IChatRead]]:
    chat_repo = ChatRepository(db=session)
    chats = await chat_repo.all(
        skip=skip, limit=limit, sort_field=sort_field, sort_order=sort_order
    )

    return IGetResponseBase[List[IChatRead]](data=chats)


@router.get(
    "/chats/{ref_id}",
    response_description="Get a single chat instance by ref_id",
    response_model=IGetResponseBase[IChatRead],
    tags=["chats"],
)
async def get_chat_by_ref_id(
        ref_id: str,
        session: AsyncSession = Depends(get_session),
) -> IGetResponseBase[IChatRead]:
    chat_repo = ChatRepository(db=session)
    chat = await chat_repo.get(ref_id=ref_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    return IGetResponseBase[IChatRead](data=chat)


@router.post(
    "/chats",
    response_description="Create a new chat",
    response_model=IChatRead,
    status_code=201,
    tags=["chats"],
)
async def create_chat(
        chat: IChatCreate,
        session: AsyncSession = Depends(get_session),
) -> IChatRead:
    """
    Create a new chat.
    """
    chat_repo = ChatRepository(db=session)
    new_chat = await chat_repo.create(obj_in=chat)
    return new_chat
