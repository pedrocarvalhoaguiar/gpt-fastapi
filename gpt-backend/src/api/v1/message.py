import logging
from typing import List, Optional

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.enums import SortOrder
from src.db.session import get_session
from src.repositories.message import MessageRepository
from src.schemas.common import IGetResponseBase
from src.schemas.message import IMessageRead, IMessageCreate, MessageBase
import openai
from fastapi.responses import JSONResponse
from fastapi import Body

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    "/messages",
    response_description="List all messages instances",
    response_model=IGetResponseBase[List[IMessageRead]],
    tags=["messages"],
)
async def messages(
        skip: int = Query(0, ge=0),
        limit: int = Query(50, ge=1),
        sort_field: Optional[str] = "created_at",
        sort_order: Optional[str] = SortOrder.DESC,
        session: AsyncSession = Depends(get_session),
) -> IGetResponseBase[List[IMessageRead]]:
    message_repo = MessageRepository(db=session)
    messages = await message_repo.all(
        skip=skip, limit=limit, sort_field=sort_field, sort_order=sort_order
    )

    return IGetResponseBase[List[IMessageRead]](data=messages)


@router.get(
    "/messages/{chat_id}",
    response_description="Get a single chat instance by ref_id",
    response_model=IGetResponseBase[List[IMessageRead]],
    tags=["messages"],
)
async def get_message_by_chat_id(
        chat_id: int,
        session: AsyncSession = Depends(get_session),
) -> IGetResponseBase[List[IMessageRead]]:
    message_repo = MessageRepository(db=session)
    messages = await message_repo.f(chat=chat_id)
    if not messages:
        raise HTTPException(status_code=404, detail="Messages not found")

    return IGetResponseBase[List[IMessageRead]](data=messages)


@router.post(
    "/messages",
    response_description="Create a new message",
    response_model=IMessageRead,
    status_code=201,
    tags=["messages"],
)
async def create_message(
        message: IMessageCreate,
        session: AsyncSession = Depends(get_session),
) -> IMessageRead:
    """
    Create a new message.
    """
    message_repo = MessageRepository(db=session)
    new_message = await message_repo.create(obj_in=message)
    return new_message


@router.post("/gpt-answer")
async def get_gpt_answer(input_text: str = Body(..., embed=True)):
    return JSONResponse(content={'answer': input_text}, status_code=200)
    # try:
    #     logger.info(input_text)
    #     openai.api_key = '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'
    #     response = openai.Completion.create(
    #         engine="gpt-3.5-turbo", prompt=input_text, max_tokens=100
    #     )
    #     answer = response.choices[0].text.strip()
    #     return JSONResponse(content={"answer": answer})
    # except openai.error.RateLimitError as e:
    #     # Handle rate limit error, e.g. wait or log
    #     logger.info(f"OpenAI API request exceeded rate limit: {e}")
    #     return JSONResponse(content={"answer": 'Api key reached limit'}, status_code=400)
