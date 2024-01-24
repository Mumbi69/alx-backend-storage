#!/usr/bin/env python3
"""Writing strings to Redis"""

import redis
import uuid
from typing import Callable, Union


class Cache:
    def __init__(self):
        """initializes the main class"""
        self._redis = redis.Redis()
        self._redis.flushdb()


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


    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value
