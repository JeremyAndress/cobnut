from typing import Union, Dict, List, Tuple, Optional
from connection import RedisConnection
from schemas.redis import RedisModel

class Cobnut():
    def __init__(
        self, *, redis_connection: Union[RedisModel, None] = None
    ):
        self.redis_connection = redis_connection
        self.store = self.create_store()


    def create_store(self):
        if self.redis_connection:
            store = self.redis_conn()
            return store


    def redis_conn(self):
        r = RedisConnection(
            host=self.redis_connection.host
        )
        r.test_connection()
        return r


    def set(self, *, key: str, data: Union[
        str, int, Dict, List, float, 
        bytes, Tuple
    ]):
        self.store.set(key=key, data=data)


    def get(self, *, key: str):
        return self.store.get(key=key)
    
    def clean_key(self, *, key: str):
        def decorator(func):
            def wrapper(*args,**kwargs):
                return func(*args,**kwargs)
            return wrapper
        return decorator

cobnut = Cobnut(redis_connection=RedisModel(host="localhost"))
