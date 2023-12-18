from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from example.model.models import Base

DATABASE_URL = "postgresql://postgres:6Cq3HJPUvcz6P&W^X@124.223.179.142:5333/postgres"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

