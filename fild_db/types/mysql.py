import json

from fild.sdk import Array, Bool, Dictionary

from fild_db.types.common import DBBaseJson


class DbBool(Bool):
    def to_db(self):
        return int(self.value)

    def with_values(self, values):
        if isinstance(values, int):
            values = bool(values)

        self._value = values

        return self


class DBJsonDict(DBBaseJson, Dictionary):
    def to_db(self):
        return json.dumps(self.value, separators=(',', ':'))


class DbJsonArray(DBBaseJson, Array):
    def to_db(self):
        return json.dumps(self.value, separators=(',', ':'))
