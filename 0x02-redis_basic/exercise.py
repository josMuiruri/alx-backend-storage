#!/usr/bin/env python3
import redis
import uuid
from typing import Union

class Cache:
    """
    Cache class to store data in Redis with randomly generated keys.

    Attributes:
        _redis (redis.Redis): Instance of Redis client.
    """
    

    def __init__(self):
        """Initialize the Cache class.
        This method creates an instance of the Redis client and flushes the  current db to remove all existing data.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored. It can be of type str, bytes, int, or float.

        Returns:
            str: The generated key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

