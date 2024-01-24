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
    def call_history(cls, method: Callable) -> Callable:
        """
        this function store the history of inputs and
        outputs for a particular function.
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """
            this function store the history of inputs and
            outputs for a particular function.
            """
            method_name = method.__qualname__

            input_key = f"{method_name}:inputs"
            self._redis.rpush(input_key, str(args))

            output = method(self, *args, **kwargs)

            output_key = f"{method_name}:outputs"
            self._redis.rpush(output_key, output)
            return output
        return wrapper


        @call_history
        def store(self, data: Union[str, bytes, int, float]) -> str:
            """each time it is called, the count in Redis is incremented."""
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

    s1 = cache.store("first")
    print(s1)
    s2 = cache.store("secont")
    print(s2)
    s3 = cache.store("third")
    print(s3)

    inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
    outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

    print("inputs: {}".format(inputs))
    print("outputs: {}".format(outputs))
