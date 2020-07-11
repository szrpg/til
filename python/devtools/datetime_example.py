# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, timezone


# ISO format
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
print(now)

# Unix time
now = datetime.now().timestamp()
print(f'timezone default: {now}')

now = datetime.utcnow().timestamp()
print(f'timezone UTC: {now}')
