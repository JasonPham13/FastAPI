from sqlalchemy.orm.session import Session
from db.user_db import UserDb


def get_all_users(db: Session):
    return db.query(UserDb).all()


def get_by_username(db: Session, _username):
    query = db.query(UserDb).filter(UserDb.username==_username).first()
    return query


def add_user(db: Session, _username, _email, _role):
    new_user= UserDb(username=_username, email=_email, role=_role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def add_user_td(db: Session):
    add_user(db, "darth.vader", "darth.vader@gmail.com", "villian")
    add_user(db,"thor.odinson", "thor@gmail.com", "hero" )
    add_user(db, "jason.pham", "jason@gmail.com", "student")


def update_user(db: Session, _username, _email, _role):
    user_to_update = db.query(UserDb).filter(UserDb.username==_username).first()

    if _email != "" :
        user_to_update.email = _email

    if _role != "":
        user_to_update.role = _role

    db.commit()