import json
import decimal
import datetime
from bson.objectid import ObjectId

class JsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.datetime):
            return o.isoformat()
        elif isinstance(o, datetime.date):
            return o.strftime('%d/%m/%Y')
        elif isinstance(o, datetime.timedelta):
            return (datetime.datetime.min + o).time().isoformat()
        elif isinstance(o, ObjectId):
            return str(o)

        super(JsonEncoder, self).default(o)
