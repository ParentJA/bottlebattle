__author__ = 'parentj@eab.com (Jason Parent)'

# Django imports...
from django import forms

# Local imports...
from .models import Event


class BootstrapMixin(object):
    def __init__(self, use_bootstrap=True, *args, **kwargs):
        super(BootstrapMixin, self).__init__(*args, **kwargs)

        if use_bootstrap:
            for key in self.fields:
                self.fields[key].widget.attrs.update({
                    'class': 'form-control'
                })


class EventForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title',)
        widgets = {
            'title': forms.fields.TextInput(attrs={
                'placeholder': 'i.e. Beer Tasting'
            })
        }