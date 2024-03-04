from typing import Dict

from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient, APITestCase


class TestLinkViewSet(APITestCase):
    client_class: APIClient = APIClient
    url: str = reverse("links-list")

    def test_creating_link(self):

        data: Dict = {"original_url": "https://test-url.com/"}

        response: Response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["original_url"], data["original_url"])
        self.assertEqual(response.data["display_number"], 0)
        self.assertNotEquals(response.data["shortened_url"], "")
        self.assertNotEquals(response.data["shortened_url_path"], "")

    def test_creating_link_fails_original_url_is_incorrect(self):

        data: Dict = {"original_url": "incorrect-url-structure"}

        response: Response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
