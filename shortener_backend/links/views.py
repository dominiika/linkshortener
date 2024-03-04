from typing import List

from django.db.models import QuerySet
from django.shortcuts import redirect
from rest_framework import status, viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from links.models import Link
from links.serializers import LinkSerializer


class RedirectView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, shortened_url_path):
        try:
            link = Link.objects.get(shortened_url_path=shortened_url_path)
            link.display_number += 1
            link.save()
            return redirect(link.original_url)
        except Link.DoesNotExist:
            return Response(
                {"error": "Link not found"}, status=status.HTTP_404_NOT_FOUND
            )


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class: LinkSerializer = LinkSerializer
    queryset: QuerySet[Link] = Link.objects.all()
    # ordering: List = ["-id"]

    def create(self, request, *args, **kwargs) -> Response:
        original_url: str = request.data.get("original_url")

        link, created = Link.objects.get_or_create(original_url=original_url)
        serializer = self.serializer_class(link, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
