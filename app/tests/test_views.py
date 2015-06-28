__author__ = 'parentj@eab.com (Jason Parent)'

# Third-party imports...
from mock import Mock, patch

# Django imports...
from django.test import RequestFactory, TestCase

# Local imports...
from ..views import event_view, home_view, new_event_view


class HomeViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_home_view_renders_home_template(self):
        request = self.factory.get('/app/')
        request.user = Mock()
        request.user.return_value.is_authenticated.return_value = True

        with self.assertTemplateUsed(template_name='app/home.html'):
            home_view(request)


class EventViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_event_view_renders_event_template(self):
        request = self.factory.get('/app/event/')
        request.user = Mock()
        request.user.return_value.is_authenticated.return_value = True

        with self.assertTemplateUsed(template_name='app/event.html'):
            event_view(request)


class NewEventViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_new_event_view_renders_new_event_template(self):
        request = self.factory.get('/app/event/new/')
        request.user = Mock()
        request.user.return_value.is_authenticated.return_value = True

        with self.assertTemplateUsed(template_name='app/new_event.html'):
            new_event_view(request)

    @patch('app.views.EventForm')
    def test_passes_post_data_to_event_form(self, mock_event_form):
        mock_event_form.return_value.is_valid.return_value = False

        request = self.factory.post('/app/event/new/')
        request.user = Mock()

        new_event_view(request)

        mock_event_form.assert_any_call(data=request.POST)

    @patch('app.views.EventForm')
    def test_does_not_save_form_for_invalid_data(self, mock_event_form):
        mock_form = mock_event_form.return_value
        mock_form.is_valid.return_value = False
        mock_form.save.return_value = None

        request = self.factory.post('/app/event/new/')
        request.user = Mock()
    
        new_event_view(request)
    
        self.assertFalse(mock_form.save.called)
    
    @patch('app.views.EventForm')
    def test_saves_form_for_valid_data(self, mock_event_form):
        mock_form = mock_event_form.return_value
        mock_form.is_valid.return_value = True
        mock_form.save.return_value = None

        request = self.factory.post('/app/event/new/', {'title': 'Beer Tasting'})
        request.user = Mock()

        new_event_view(request)

        self.assertTrue(mock_form.save.called)

    @patch('app.views.EventForm')
    @patch('app.views.render')
    def test_renders_profile_edit_template_for_invalid_data(self, mock_render, mock_event_form):
        mock_event_form.return_value.is_valid.return_value = False

        request = self.factory.post('/app/event/new/')
        request.user = Mock()
        response = new_event_view(request)

        self.assertEqual(response, mock_render.return_value)

        mock_render.assert_called_once_with(request, 'app/new_event.html', {
            'form': mock_event_form.return_value
        })

    # @patch('app.views.EventForm')
    # @patch('app.views.redirect')
    # def test_redirects_profile_for_valid_data(self, mock_redirect, mock_event_form):
    #     mock_form = mock_event_form.return_value
    #     mock_form.is_valid.return_value = True
    #     mock_form.save.return_value = None
    #
    #     request = self.factory.post('/app/event/new/', {'title': 'Beer Tasting'})
    #     request.user = Mock()
    #     response = new_event_view(request)
    #
    #     self.assertTrue(mock_redirect.called)
    #     self.assertEqual(response, mock_redirect.return_value)