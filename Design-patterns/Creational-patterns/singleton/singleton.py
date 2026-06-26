from threading import Lock

class Database:
    _instance = None
    _lock = Lock()

    def __init__(self):
        print("Connecting to Database")
        self.connection = "Database connection"
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = Database()
        return cls._instance
    
    def query(self,sql):
        print(f"Executing: {sql}")

#client
db1 = Database.get_instance()
db1.query("SELECT * FROM users")
db2 = Database.get_instance()
db2.query("SELECT * from products")