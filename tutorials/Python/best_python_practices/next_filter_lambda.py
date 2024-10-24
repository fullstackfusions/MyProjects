import os

next(filter(bool, map(lambda env_key: os.environ.get(env_key), ['some_value1', 'some_value2'])), None)
