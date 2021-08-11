from models.engine.db_storage import DBStorage
from models.state import State

x = DBStorage
print(x.save(x))
