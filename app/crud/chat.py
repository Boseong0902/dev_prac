from sqlalchemy.orm import Session
from models import Chat
from schemas import ChatCreate


def create_chat(db: Session, is_user: bool, chatroom_id: int, content: str):
    db_chat = Chat(is_user=is_user, chatroom_id=chatroom_id, content=content)
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat


def get_all_chat(db: Session, chatroom_id: int):
    chat_list = [
        chat.content
        for chat in db.query(Chat).filter(Chat.chatroom_id == chatroom_id).all()
    ]

    chat_list = "\n".join(chat_list)
    return chat_list
