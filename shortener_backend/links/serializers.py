from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from rest_framework import serializers

from links.models import Link


class LinkSerializer(serializers.ModelSerializer):
    original_url = serializers.URLField(allow_null=False, required=True)
    shortened_url = serializers.ReadOnlyField()
    shortened_url_path = serializers.ReadOnlyField()
    display_number = serializers.ReadOnlyField()

    class Meta:
        model = Link
        fields = (
            "id",
            "original_url",
            "shortened_url",
            "shortened_url_path",
            "display_number",
            "user_metadata",
        )

    def validate_original_url(self, value: str) -> str:
        validator: URLValidator = URLValidator()
        try:
            validator(value)
        except ValidationError:
            raise serializers.ValidationError("Invalid URL structure")
        return value
