from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.database.config import settings


class Dbcontorl:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factroy = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocomit=False,
            engine_on_commit=False,
        )

db_control = Dbcontorl(
    url = settings.db_url,
    echo= settings.db_echo
)