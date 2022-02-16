from django import forms

from dashboard.models import RegistrySendingTravelAgency, RegistryHotels, Group


class AddGroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sending_travel_agency'].empty_label = 'Клиент (агентство или ФИО)'
        self.fields['hotel'].empty_label = 'Отель не выбран'

    class Meta:
        model = Group
        fields = ['arrival_date', 'departure_date', 'registry_sending_travel_agency_id']
        widgets = {
            'arrival_date': forms.DateInput(attrs={'class': 'btn btn-outline-secondary dateFrom top_date', 'type': 'date'}),
            'departure_date': forms.DateInput(
                attrs={'class': 'btn btn-outline-secondary dateFrom top_date', 'type': 'date'}),
        }

    sending_travel_agency = forms.ModelChoiceField(queryset=RegistrySendingTravelAgency.objects.all())
    sending_travel_agency.widget.attrs['class'] = 'form-control'

    hotel = forms.ModelChoiceField(queryset=RegistryHotels.objects.all())
    hotel.widget.attrs['class'] = 'form-control'

