from django import forms


class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs['format'] = "%Y-%m-%d"
        super().__init__(**kwargs)


class DashboardDate(forms.Form):
    start_date = forms.DateField(label='start_date')
    end_date = forms.DateField(label='end_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].widget = DateInput()
        # self.fields['start_date'].widget.attrs['placeholder'] = '01-01-2022'
        # self.fields['end_date'].widget.attrs['placeholder'] = '02-01-2022'
        self.fields['end_date'].widget = DateInput()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'btn btn-outline-secondary dateBefore top_date'
