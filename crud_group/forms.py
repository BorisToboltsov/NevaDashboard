from django import forms

from dashboard.models import RegistrySendingTravelAgency, RegistryHotels, Group, GroupHotel


class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs['format'] = "%Y-%m-%d"
        super().__init__(**kwargs)


class TimeInput(forms.TimeInput):
    input_type = "time"


class AddGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['arrival_date_group', 'arrival_time_group', 'departure_date_group', 'departure_time_group', 'type_group',
                  'paid_status', 'registry_sending_travel_agency_id', "number_ru", 'color_group', 'paid_status',
                  'arrival', 'departure', 'comment', 'manager_id']
        # widgets = {
        #     'arrival_date': forms.DateInput(attrs={'class': 'btn btn-outline-secondary dateFrom top_date', 'type': 'date'}),
        #     'arrival_time': forms.TimeInput(
        #         attrs={'class': 'btn btn-outline-secondary dateFrom top_time'}),
        #     'departure_date': forms.DateInput(
        #         attrs={'class': 'btn btn-outline-secondary dateFrom top_date', 'type': 'date'}),
        #     'departure_time': forms.TimeInput(attrs={'class': 'btn btn-outline-secondary dateFrom top_time', 'type': 'time'}),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['arrival_date_group'].widget = DateInput()
        self.fields['arrival_date_group'].widget.attrs['class'] = 'btn btn-outline-secondary dateFrom top_date'
        self.fields['arrival_date_group'].widget.attrs['id'] = 'arrival_date_group'
        self.fields['arrival_time_group'].widget = TimeInput()
        self.fields['arrival_time_group'].widget.attrs['class'] = 'btn btn-outline-secondary dateFrom top_time'
        self.fields['arrival_time_group'].widget.attrs['type'] = 'time'
        self.fields['departure_date_group'].widget = DateInput()
        self.fields['departure_date_group'].widget.attrs['class'] = 'btn btn-outline-secondary dateFrom top_date'
        self.fields['departure_date_group'].widget.attrs['id'] = 'departure_date_group'
        self.fields['departure_time_group'].widget = TimeInput()
        self.fields['departure_time_group'].widget.attrs['class'] = 'btn btn-outline-secondary dateFrom top_time'
        self.fields['registry_sending_travel_agency_id'].empty_label = 'Клиент (агентство или ФИО)'
        self.fields['registry_sending_travel_agency_id'].widget.attrs['class'] = 'input-group-text form-control'
        self.fields['number_ru'].widget.attrs['class'] = 'input-group-text form-control'
        self.fields['color_group'].widget.attrs['class'] = 'input-group-text form-control'
        self.fields['paid_status'].widget.attrs['class'] = 'input-group-text form-control'
        self.fields['arrival'].widget.attrs['class'] = 'input-group-text form-control'
        self.fields['departure'].widget.attrs['class'] = 'input-group-text form-control'
        self.fields['comment'].widget.attrs['class'] = 'input-group-text form-control'
        self.fields['manager_id'].widget.attrs['class'] = 'input-group-text form-control'
        self.fields['type_group'].widget.attrs['class'] = 'input-group-text form-control'


    # hotel = forms.ModelChoiceField(queryset=RegistryHotels.objects.all())
    # hotel.widget.attrs['class'] = 'form-control'


class AddGroupHotelForm(forms.ModelForm):
    class Meta:
        model = GroupHotel
        fields = ["registry_hotels_id", "arrival_date_hotel", "departure_date_hotel"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["registry_hotels_id"].empty_label = 'Отель не выбран'
        self.fields['arrival_date_hotel'].widget = DateInput()
        self.fields['arrival_date_hotel'].widget.attrs['class'] = 'btn btn-outline-secondary dateFrom top_date'
        self.fields['arrival_date_hotel'].widget.attrs['id'] = 'arrival_date_hotel'
        self.fields['departure_date_hotel'].widget = DateInput()
        self.fields['departure_date_hotel'].widget.attrs['class'] = 'btn btn-outline-secondary dateFrom top_date'
        self.fields['departure_date_hotel'].widget.attrs['id'] = 'departure_date_hotel'
        self.fields['registry_hotels_id'].empty_label = 'Отель не выбран'
        self.fields['registry_hotels_id'].widget.attrs['class'] = 'input-group-text form-control'
