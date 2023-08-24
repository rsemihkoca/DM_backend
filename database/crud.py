from sqlalchemy.orm.decl_api import DeclarativeMeta
from database.db import SessionLocal, engine, Base, Users
from sqlalchemy.sql import table, column, select, update, insert
from database.schemes import UserCreateForm
def get_user_by_username(username: str):

    with SessionLocal() as session:
        try:
            user = session.query(Users).filter(Users.username == username).first()
            if not user:
                return None
            return user
        except Exception as e:
            print(e)
            return None

def create_user(user: UserCreateForm):

    with SessionLocal() as session:

        try:

            NewUser = Users(**user.dict())
            session.add(NewUser)
            session.commit()
            session.refresh(NewUser)

            return NewUser
        except Exception as e:
            print(e)
            return None
