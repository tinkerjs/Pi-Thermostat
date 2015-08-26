from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.utils import timezone
from django.core.urlresolvers import reverse
import datetime

from ThermoApp.models import HistoricData, RealtimeData, AutomationData, ForecastData

from ThermoApp.forms import UserInterface_Form

# Create your views here.
def UserInterface(request):
	# make the query here so we only do it once per call
	rtData = RealtimeData.objects.get(id=1)
	fcData = ForecastData.objects.get(id=1)
	hsData = HistoricData.objects.latest('hs_eventdatetime')
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		#create a form  instance and populate it with data from the request
		form = UserInterface_Form(request.POST)
        #check if its valid
		if form.is_valid():
			#process the data
			pDesiredTemp = form.cleaned_data['rt_destemp']
			pFanMode = form.cleaned_data['rt_fanmode']
			rtData.rt_destemp = pDesiredTemp
			rtData.rt_fanmode = pFanMode
			rtData.save()
			#print('Desired Temp: {} Forecast: {}'.format(pDesiredTemp, pFanMode))
			#redirect to a new url
			return HttpResponseRedirect('/thermostat/userinterface/')
	else:
		rawForecast = fcData.fc_4dforecast
		rt_currenttemp = rtData.rt_currenttemp
		form = UserInterface_Form(initial={'rt_currenttemp': rtData.rt_currenttemp,
										   'rt_humidity': rtData.rt_humidity,		
										   'rt_destemp': rtData.rt_destemp,
										   'rt_fanmode': rtData.rt_fanmode,
										   'fc_4dforecast': rawForecast,
										   'fc_outsidetemp': fcData.fc_outsidetemp,
										   'fc_outsidehumidity': fcData.fc_outsidehumidity
											})
        
        
		return render(request, 'ThermoApp/userinterface.html', {'form': form,
																'rt_currenttemp': rtData.rt_currenttemp,
																'rt_humidity': rtData.rt_humidity,
																'fc_4dforecast': rawForecast,
																'fc_outsidetemp': fcData.fc_outsidetemp,
																'fc_outsidehumidity': fcData.fc_outsidehumidity,
																'hs_eventdesc': hsData.hs_eventdesc,
																'hs_eventdt': hsData.hs_eventdatetime,
																'curr_time': timezone.now(),
																})



def index(request):
    context = {}
    return render(request, 'ThermoApp/index.html', context)
    
    
def historicinterface(request, hsduration=30):
    try: 
        listOfEvents = HistoricData.objects.all().filter(hs_startdatetime__gte=timezone.now() - datetime.timedelta(days=int(hsduration))) #get items older/greater than hsduration

    except HistoricData.DoesNotExist:
        raise Http404('Historic information does not exist for this record!')
    context = {'listOfEvents': listOfEvents}
    return render(request, 'ThermoApp/historicinterface.html', context)
    
def automationinterface(request):
    try: 
        automationData = AutomationData.objects.all()
    except AutomationData.DoesNotExist:
        raise Http404('Automation information does not exist!')
    context = {'automationData': automationData}
    return render(request, 'ThermoApp/automationinterface.html', context)
	
def developmentinterface(request):
    try: 
        pass
    except:
        raise Http404('Failed!')
    context = {}
    return render(request, 'ThermoApp/dev/javascript.html', context)


