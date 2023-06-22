from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from artkiveapi.models import ImageTag

class ImageTagView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single image tag

        Returns:
            Response -- JSON serialized image tag
        """
        image_tag = ImageTag.objects.get(pk=pk)
        serializer = ImageTagSerializer(image_tag)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all image Tags

        Returns:
            Response -- JSON serialized list of image Tags
        """
        image_tags = ImageTag.objects.all()
        serializer = ImageTagSerializer(image_tags, many=True)
        return Response(serializer.data)

class ImageTagSerializer(serializers.ModelSerializer):
    """JSON serializer for image tags
    """
    class Meta:
        model = ImageTag
        fields = ('image', 'tag')
