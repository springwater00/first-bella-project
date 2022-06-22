from datetime import date, datetime, timezone, tzinfo, timedelta
from pytz_deprecation_shim import UTC
import time


# output = datetime.datetime(2007, 12, 6, 15, 29, 43, 79060, timezone=UTC)

output = today()
# timedelta(hours=8)
# output = datetime(UTC())
# output = datetime.tzinfo(UTC)

# output = datetime.datetime.utcnow()
print(output)
# print(datetime(1989,1,23,0,0,0,0, UTC(8)))
# print(datetime.now(tz=UTC 8))
# print(datetime.now().astimezone[UTC: 8])
# print(today())
# # time = date(datetime(2022,6,21).astimezone(UTC,8))
# print(time)