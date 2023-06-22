from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from artkiveapi.models import Folder, ImageFolder

class ImageFolderView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single image folder

        Returns:
            Response -- JSON serialized image folder
        """
        image_folder = ImageFolder.objects.get(pk=pk)
        serializer = ImageFolderSerializer(image_folder)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all image folders

        Returns:
            Response -- JSON serialized list of image folders
        """
        image_folder = ImageFolder.objects.all()
        serializer = ImageFolderSerializer(image_folder, many=True)
        return Response(serializer.data)

class ImageFolderSerializer(serializers.ModelSerializer):
    """JSON serializer for image folders
    """
    class Meta:
        model = ImageFolder
        fields = ('image', 'folder')
