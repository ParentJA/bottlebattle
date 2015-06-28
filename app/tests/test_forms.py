__author__ = 'parentj@eab.com (Jason Parent)'

# Standard library imports...

# Third-party imports...

# Django imports...
from django.test import TestCase

# Local imports...
from ..forms import EventForm


class EventFormTest(TestCase):
    def test_form_has_required_fields(self):
        form = EventForm()

        self.assertIn('id="id_title"', form.as_p())