from dotenv import load_dotenv
import os
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create a City Table - DONE
# Add the state.id FK column to it - DONE
# Add entries to both the City and State tables - DONE
# Demo Querying the data - ON GOING



load_dotenv(".env")

user = os.getenv('HBNB_MYSQL_USER')
pwd = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
db = os.getenv('HBNB_MYSQL_DB')

class Base(DeclarativeBase):
    pass


class State(Base):
     __tablename__ = "State"

     id = Column(String(500), primary_key=True)
     name = Column(String(128))
     created_at = Column(DateTime)
     updated_at = Column(DateTime)

class City(Base):
     __tablename__ = "City"

     id = Column(String(500), primary_key=True)
     name = Column(String(128))
     created_at = Column(DateTime)
     updated_at = Column(DateTime)
     state_id = Column(String(500), ForeignKey("State.id"), nullable=False)



engine = create_engine(f'mysql://{user}:{pwd}@{host}/{db}')

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)


##############################################################################################################################

# Connect to the DB - DONE
# Create the user hbnb_dev_too - DONE
# Create DB hnbn_dev_db_too - DONE
# Grant all privileges to hbnb_dev_too on hnbn_dev_db_too - DONE
# Grant SELECT privilege to hbnb_dev_too on performance_schema - DONE

# connection = engine.connect()
# create_user = text("CREATE USER IF NOT EXISTS 'hbnb_dev_too'@'localhost' IDENTIFIED BY 'spatni';")
# create_db = text("CREATE DATABASE IF NOT EXISTS hbnb_dev_db_too;")
# grant_user = text("GRANT ALL PRIVILEGES ON hbnb_dev_db_too.* TO 'hbnb_dev_too'@'localhost';")
# grant_select = text("GRANT SELECT ON performance_schema.* TO 'hbnb_dev_too'@'localhost';")

# connection.execute(create_user)
# connection.execute(create_db)
# connection.execute(grant_user)
# connection.execute(grant_select)
# print("All queries have been executed")