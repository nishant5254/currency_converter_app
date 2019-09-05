from django import forms


CURRENCY_CHOICES = (
    ('AED','AED'),
    ('AFN', 'AFN'),
    ('AMD','AMD'),
    ('EUR','EUR'),
    ('USD', 'USD'),
    ('ALL','ALL'),
    ('INR','INR'),
)

class currencyform(forms.Form):
    amount=forms.FloatField()
    Homecurrency= forms.CharField(label='Homecurrency', widget=forms.Select(choices=CURRENCY_CHOICES))
    Targetcurrency= forms.CharField(label='Targetcurrency', widget=forms.Select(choices=CURRENCY_CHOICES))
