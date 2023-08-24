from sqlalchemy.orm.decl_api import DeclarativeMeta
from database.db import SessionLocal, engine, Base, users


def get_user_by_username(username: str):

    with SessionLocal() as session:
        user = session.query(users).filter(users.username == username).first()
        if not user:
            return None
        return user

