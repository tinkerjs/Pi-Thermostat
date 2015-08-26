from django import forms
from django.forms import ModelForm
from ThermoApp.models import RealtimeData


#class UserInterface_Form(ModelForm):
#    class Meta:
#        model = RealtimeData
#        fields = [
#                    'rt_datetime',
#                    'rt_currenttemp',
#                    'rt_destemp',
#                    'rt_fanmode',
#                    ]

class UserInterface_Form(forms.Form):
	#rt_currenttemp = forms.DecimalField(label='Current Temperature', max_value=90, min_value=60, max_digits=4, decimal_places=2)
	rt_destemp = forms.DecimalField(label='Desired Temperature', max_value=90, min_value=60, max_digits=2, decimal_places=0)
	rt_fanmode = forms.ChoiceField(choices=RealtimeData.rt_fanmode_choices)
	#fc_4dforecast = forms.CharField(label='Forecast', max_length=500)