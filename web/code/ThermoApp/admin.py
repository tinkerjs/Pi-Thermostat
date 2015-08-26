from django.contrib import admin
from ThermoApp.models import RealtimeData,HistoricData,AutomationData,ForecastData

# Register your models here.
class AutomationDataAdmin(admin.ModelAdmin):
    fieldsets = [
             ('Automation Records', {'fields': ['am_datetime',
                                                   'am_dayofweek',
                                                   'am_fanmode',
                                                   'am_temp',
                                                   'am_forecastdur',], 
                                       'classes': ['collapse']}),
                ]
    list_display = ('am_datetime','am_dayofweek','am_fanmode','am_temp','am_forecastdur')
    list_filter = ['am_datetime','am_dayofweek']
    search_fields = ['am_dayofweek']
    
    
                                        
admin.site.register(AutomationData,AutomationDataAdmin)
 
class HistoricDataAdmin(admin.ModelAdmin):
    fieldsets = [
                 ('Historic Records', {'fields': ['hs_eventid',
												  'hs_eventdesc',
                                                  'hs_eventdatetime',
                                                  'hs_currenttemp',
                                                  'hs_destemp',
                                                  'hs_humidity',
                                                  'hs_fanmode',
                                                  'hs_outsidetemp',
                                                  'hs_outsidehumidity',
                                                  'hs_forecast',
                                                  'hs_runtime',
                                                  'hs_uptime'], 
                                           'classes': ['']}),
                 ]
    list_display = ('hs_eventdesc','hs_eventdatetime','hs_currenttemp')
    list_filter = ['hs_eventdesc','hs_eventdatetime']
    search_fields = ['hs_eventdatetime']

admin.site.register(HistoricData,HistoricDataAdmin)

class RealtimeDataAdmin(admin.ModelAdmin):
    fieldsets = [
                 ('RealTime Records', {'fields': ['rt_datetime', 
                                                       'rt_currenttemp',
                                                       'rt_destemp',
                                                       'rt_humidity',
                                                       'rt_fanmode',
                                                       'rt_runtime',
                                                       'rt_uptime',
													   'rt_hWstatus',],
                                            'classes': ['collapse']}),
                ]
    list_display = ('rt_datetime','rt_currenttemp','rt_destemp','rt_fanmode','rt_uptime')
    

admin.site.register(RealtimeData,RealtimeDataAdmin)

class ForecastDataAdmin(admin.ModelAdmin):
    fieldsets = [
                 ('Forecast Records', {'fields': ['fc_datetime',
                                                  'fc_outsidetemp', 
                                                  'fc_outsidehumidity',
                                                  'fc_4dforecast',
                                                  'fc_plannerforecast'],
                                            'classes': ['collapse']}),
                ]
    list_display = ('fc_datetime','fc_outsidetemp','fc_outsidehumidity','fc_4dforecast','fc_plannerforecast')
    

admin.site.register(ForecastData,ForecastDataAdmin)
