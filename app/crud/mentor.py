from sqlalchemy.orm import Session
from models import Mentor
from schemas import MentorCreate


def create_mentor(db: Session, mentor: MentorCreate):
    db_mentor = Mentor(name=mentor.name, description=mentor.description)
    db.add(db_mentor)
    db.commit()
    db.refresh(db_mentor)
    return db_mentor


def get_mentor(db: Session, mentor_id: int):
    return db.query(Mentor).filter(Mentor.id == mentor_id).first()


def get_mentor_all(db: Session):
    return db.query(Mentor).all()
