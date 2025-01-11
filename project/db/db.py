from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import ASYNC_DB_URL

# Создание асинхронного движка для связи с БД
async_engine = create_async_engine(url=ASYNC_DB_URL, future=True, echo=False)

# Создание асинхронной сессии
async_session = async_sessionmaker(bind=async_engine, autoflush=False,
                                   autocommit=False, expire_on_commit=False)


# Родительский класс для создания таблиц
class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
