import json

from fild.sdk import Array, Bool

from fild_db.types.common import DBBaseJsonDict


class DbBool(Bool):
    def to_db(self):
        return int(self.value)

    def with_values(self, values):
        if isinstance(values, int):
            values = bool(values)

        self._value = values

        return self


class DBJsonDict(DBBaseJsonDict):
    def to_db(self):
        return json.dumps(self.value, separators=(',', ':'))


class DbJsonArray(Array):
    def to_db(self):
        return json.dumps(self.value, separators=(',', ':'))

    def with_values(self, values):
        if isinstance(values, str):
            values = json.loads(values)

        if values is not None:
            return super().with_values(values)

        return self
