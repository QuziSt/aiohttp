from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, func

from server import app


PG_DSN = 'postgres+asyncpg://postgres:postgres@127.0.0.1:5431/async_db'

engine = create_async_engine(PG_DSN)
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    
class UserPost(Base):
    __tablename__ = 'user_posts'
    
    id = Column(Integer, autoincrement=True, primary_key=True )
    creator = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    post_header = Column(String, nullable=False)
    post_text = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    

async def orm_context(app):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield 
    await engine.dispose()