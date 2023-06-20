from django.http import HttpResponseNotFound
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.decorators import action
from artkiveapi.models import Image, Muser, ImageTag, ImageFolder
from random import choice

class ImageView(ViewSet):
    """Image view"""

    def create(self, request):
        """Handle POST request for uploading an image
        Returns: Response -- JSON serialized image instance"""
        muser = Muser.objects.get(user=request.auth.user)
        image_tags = ImageTag.objects.get(pk=request.data["image_tags"])
        image_folders = ImageFolder.objects.get(pk=request.data["image_folders"])

        image = Image.objects.create(
            img_url=request.data.get("img_url"),
            description=request.data.get("description"),
            muser=muser,
            image_folders=image_folders,
            image_tags=image_tags,
        )

        serializer = ImageSerializer(image)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT request for editing an image
        Returns: Response -- JSON serialized image instance"""
        try:
            image = Image.objects.get(id=pk)

            descriptions = request.data.get("description")
            image.description = descriptions

            image.save()

            serializer = ImageSerializer(image)
            return Response(serializer.data)
        except Image.DoesNotExist:
            return HttpResponseNotFound()

    def destroy(self, request, pk):
        """Handle DELETE request for deleting an image
        Returns: Response -- Empty body with 204 status code"""
        try:
            image = Image.objects.get(pk=pk)

            image.folders.clear()

            image.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except Image.DoesNotExist:
            return HttpResponseNotFound()

    def list(self, request):
        """Handle GET request to retrieve images
        Returns: Response -- JSON serialized list of image instances"""
        images = Image.objects.all()

        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def random(self, request):
        images = Image.objects.all()

        if images:
            random_image = choice(images)

            response = {
                'url': random_image.img_url
            }

            return Response(response)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class ImageSerializer(serializers.ModelSerializer):
    """JSON serializer for the images"""
    
    class Meta:
        model = Image
        fields = ('id', 'img_url', 'description', 'image_folders', 'image_tags')