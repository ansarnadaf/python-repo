import threading

class SingletonMeta(type):
    """
    A thread-safe implementation of a Singleton Metaclass.
    """
    _instances = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        # Double-checked locking pattern for performance
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    # Super calls the type.__call__, which handles __new__ and __init__
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]

# Usage
class DatabaseConnector(metaclass=SingletonMeta):
    def __init__(self):
        self.connection_id = "12345"

class CacheConnector(DatabaseConnector):
    # This will have its own unique instance because of the 'cls' key in _instances
    pass
