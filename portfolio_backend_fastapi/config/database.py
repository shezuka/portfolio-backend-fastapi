import os
from typing import Union


class DatabaseConfig:
    DATABASE_URI: Union[str, None] = os.environ.get('DATABASE_URI', None)
