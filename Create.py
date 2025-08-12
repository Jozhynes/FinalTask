from models import Base
from connections import data
Base.metadata.create_all(bind=data)