from sqlalchemy.orm import Session

from backend.adapters.output.db import get_db_session
from backend.ports.singleton_meta import SingletonMeta


class IndexerRepository(metaclass=SingletonMeta):
    """Repository for the indexer"""

    def __init__(self, db: Session = None):
        self.db = db if db else get_db_session()

    def index(self, data: dict):
        pass

    def search(self, query: str):
        pass
