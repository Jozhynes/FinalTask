from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base


username= 'root'
password= 'JozPat001//'
database= 'Project'

path= f"mysql+mysqldb://{username}:{password}@localhost/{database}"
data= create_engine(path)
Sessionlocal=sessionmaker(bind=data)
Base=declarative_base()