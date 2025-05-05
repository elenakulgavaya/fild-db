import json

from fild.sdk import Dictionary


class DBJsonDict(Dictionary):
    def to_db(self):
        return json.dumps(self.value).encode('utf-8')

    def with_values(self, values):
        if isinstance(values, str):
            values = json.loads(values)

        if values is not None:
            return super().with_values(values)

        return self
