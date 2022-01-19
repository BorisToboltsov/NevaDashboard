from django import forms


class DashboardDate(forms.Form):
    start_date = forms.DateField(label='end_date')
    end_date = forms.DateField(label='end_date')

    def __init__(self, *args, **kwargs):
        super(DashboardDate, self).__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs['placeholder'] = '01-01-2022'
        self.fields['end_date'].widget.attrs['placeholder'] = '02-01-2022'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'btn btn-outline-secondary dateBefore top_date'
