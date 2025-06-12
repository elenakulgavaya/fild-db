import json

from fild.sdk import Dictionary
from fild_db.types.common import DBBaseJson


class DBJsonDict(DBBaseJson, Dictionary):
    def to_db(self):
        return json.dumps(self.value).encode('utf-8')
