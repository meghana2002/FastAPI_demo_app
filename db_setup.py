from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os
load_dotenv()

conn = os.getenv("CONNSTR")

engine = create_engine(conn)

