from django.test import TestCase

from links.models import Link


class TestCompetitionModel(TestCase):
    def test_str(self):
        original_url: str = "https://some-url.com/"

        link: Link = Link.objects.create(original_url=original_url)

        self.assertEqual(original_url, str(link))

    def test_link_saves_correctly(self):
        original_url: str = "https://some-url.com/"

        link: Link = Link.objects.create(original_url=original_url)

        self.assertEqual(link.original_url, original_url)
        self.assertNotEquals(link.shortened_url, "")
        self.assertNotEquals(link.shortened_url_path, "")

    def test_exists(self):
        original_url: str = "https://some-url.com/"

        link: Link = Link.objects.create(original_url=original_url)

        self.assertTrue(link.exists(shortened_url_path=link.shortened_url_path))

    def test_does_not_exist(self):
        original_url: str = "https://some-url.com/"

        link: Link = Link.objects.create(original_url=original_url)

        self.assertFalse(link.exists(shortened_url_path="AnsWqssa"))
