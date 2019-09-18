from django.test import TestCase
from django.urls import reverse
from .models import Quote, Author

# Create your tests here.
class QuoteCreationTestCase(TestCase):

    def setUp(self):
        url = reverse("quotes")
        data = {
            "author": "",
            "quotation": "The good, the bad & the ugly."
        }

        self.response = self.client.post(url,data,format="json")

    def test_received_201_created_status_code(self):
        self.assertEqual(self.response.status_code, 201)
    
    def test_quote_was_created(self):
        self.assertEqual(Quote.objects.count(),1)

    def test_correct_quotation_was_set(self):
        self.assertEqual(Quote.objects.get().quotation, "The good, the bad & the ugly.")

    def test_simulating_failed_test_case(self):
        self.assertEqual(1,2)