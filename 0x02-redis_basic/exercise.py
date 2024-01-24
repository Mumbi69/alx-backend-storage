#!/usr/bin/env python3
"""Writing strings to Redis"""

import redis
import uuid
from typing import Callable, Union
from functools import wraps


class Cache:
    def __init__(self):
        """initializes the main class"""
        self._redis = redis.Redis()
        self._redis.flushdb()


    @staticmethod
    def count_calls(method: Callable) -> Callable:
        """
        takes a method as an argument, increments the count in
        Redis using the qualified name of the method, and then
        calls the original method.
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """
            takes a method as an argument, increments the count in
            Redis using the qualified name of the method, and then
            calls the original method.
           """
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper


    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """each time it is called, the count in Redis is incremented."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Represents the function store"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, None]:
        """function that creates a get method"""
        data = self._redis.get(key)
        if data is not None:
            if fn is not None:
                return fn(data)
            return data
        return None


    def get_str(self, key: str) -> Union[str, None]:
        """predefined conversion functions for strings and integers"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))


    def get_int(self, key: str) -> Union[int, None]:
        """predefined conversion functions for strings and integers"""
        return self.get(key, fn=int)


if __name__ == "__main__":
    cache = Cache()

    cache.store(b"first")
    print(cache.get(cache.store.__qualname__))

    cache.store(b"second")
    cache.store(b"third")
    print(cache.get(cache.store.__qualname__))
