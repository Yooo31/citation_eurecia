from citation import *
from eurecia import *

import datetime

while (1) :
  now = datetime.datetime.now()
  actualHour = now.hour
  actualMinute = now.minute

  if (actualHour == 8 and actualMinute == 30):
    print(actualHour, actualMinute)

    citation = getCitation()
    print(citation)

    start(citation)
    print('Mood is send !')