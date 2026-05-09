import warnings

# pylint: disable=wrong-import-position
warnings.warn(
    "fild-db is deprecated and will no longer be maintained. "
    "Migrate to surety-db: pip install surety-db. "
    "Replace 'from fild_db import ...' with 'from surety.db import ...'. "
    "See https://github.com/elenakulgavaya/surety-db for details.",
    DeprecationWarning,
    stacklevel=2,
)

from .types import mysql
from .client import MysqlDBClient, PostgresqlDBClient, SqliteDBClient
from .database import Database
