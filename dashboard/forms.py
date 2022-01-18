from django import forms


class DashboardDate(forms.Form):
    start_date = forms.DateField(label='start_date')
    end_date = forms.DateField(label='end_date')
