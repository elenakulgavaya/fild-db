import json

from fild_db.types.common import DBBaseJsonDict


class DBJsonDict(DBBaseJsonDict):
    def to_db(self):
        return json.dumps(self.value).encode('utf-8')
