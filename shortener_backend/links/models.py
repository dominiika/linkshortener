from django.conf import settings
from django.db import models

from links.link_generator import LinkGenerator


class Link(models.Model):
    original_url = models.URLField(max_length=500, null=False, blank=False)
    shortened_url = models.URLField(max_length=255, default="", unique=True)
    shortened_url_path = models.CharField(max_length=255, default="", unique=True)
    display_number = models.IntegerField(default=0)
    user_metadata = models.JSONField(default=dict)

    def __str__(self):
        return self.original_url

    def save(self, *args, **kwargs) -> None:
        link_generator: LinkGenerator = LinkGenerator(
            settings.DOMAIN_URL, settings.SHORTENED_URL_LENGTH
        )
        link_generator.run()

        while self.exists(link_generator.link_path):
            link_generator.run()

        self.shortened_url = link_generator.full_link
        self.shortened_url_path = link_generator.link_path

        super().save(*args, **kwargs)

    @staticmethod
    def exists(shortened_url_path: str) -> bool:
        return Link.objects.filter(shortened_url_path=shortened_url_path).exists()
