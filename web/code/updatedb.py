print('Starting, importing')
import django
django.setup()
from ThermoApp.models import RealtimeData as RTdata

print('Import complete')

d = RTdata(rt_currenttemp=22,rt_fanmode='C')
d.save()

print('Record save complete')