from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from backend.settings import get_settings

settings = get_settings()
Base = declarative_base()
engine = create_engine(settings.db_connection_string, connect_args={"options": "-c timezone=utc"})


def get_db_session() -> Session | None:
    """Create a new session with sqlalchemy and returns it.
    Args:
        None

    Returns:
        Session: The instance of a database Session.
    """
    try:
        SessionLocal = sessionmaker(bind=engine)
        return SessionLocal()
    except Exception as e:
        print(f"cannot connect to output database: {str(e)}")
        return None


def migrate():
    print("Migrating database...")
    Base.metadata.create_all(engine)


def reset():
    print("Resetting database...")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
