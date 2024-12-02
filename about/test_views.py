from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateRequestForm


class TestAboutViews(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about = About(title="About title", content="About content")
        self.about.save()

    def test_render_about_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about_me'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About title", response.content)
        self.assertIn(b"About content", response.content)
        self.assertIsInstance(
            response.context['collaborate_request_form'], CollaborateRequestForm)

    def test_successful_collaborate_form_submission(self):
        """Test for submitting collaborate form on about me page"""
        post_data = {
            'name': 'test',
            'email': 'test@test.com',
            'message': 'This is a test message.',
        }
        response = self.client.post(reverse('about_me'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.',
            response.content
        )
