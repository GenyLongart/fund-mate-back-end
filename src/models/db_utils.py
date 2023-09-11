from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from .base import db

@contextmanager
def session_scope():
    Session = sessionmaker(bind=db.engine)
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
