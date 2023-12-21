from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:6Cq3HJPUvcz6P&W^X@124.223.179.142:5333/postgres"

Base = declarative_base()
engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine
DBSession = scoped_session(sessionmaker(bind=engine))
