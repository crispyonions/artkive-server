from random import choice
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.decorators import action
from artkiveapi.models import Image, Muser, Folder, Tag, ImageTag

class ImageView(ViewSet):
    """Image view"""

    def create(self, request):
        """Handle POST request for uploading an image
        Returns: Response -- JSON serialized image instance"""
        muser = Muser.objects.get(user=request.auth.user)
        folder = Folder.objects.get(pk=request.data["folder"])
        tags = []
        tag_ids = request.data.get("tags", [])
        for tag_id in tag_ids:
            tag = Tag.objects.get(pk=tag_id)
            tags.append(tag)

        image = Image.objects.create(
        img_url=request.data["img_url"],
        description=request.data["description"],
        muser=muser,
        folder=folder,
        )

        image.tags.set(tags)

        serializer = ImageSerializer(image)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def update(self, request, pk):
        """Handle PUT request for editing an image
        Returns: Response -- JSON serialized image instance"""
        image = Image.objects.get(id=pk)
        image.description = request.data["description"]
        image.img_url = request.data["img_url"]
        
        all_tags = []
        tags = request.data["tags"]
        for tag_id in tags:
            tag = Tag.objects.get(pk=tag_id)
            all_tags.append(tag)
        image.tags.set(all_tags)
        
        image.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle DELETE request for deleting an image
        Returns: Response -- Empty body with 204 status code"""
        image = Image.objects.get(pk=pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        """Handle GET request to retrieve images
        Returns: Response -- JSON serialized list of image instances"""
        images = Image.objects.all()
        folder_id = request.query_params.get('folder')
        if folder_id is not None:
            images=images.filter(folder_id=folder_id)
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """Handle GET request to retrieve a single image"""
        try:
            image = Image.objects.get(pk=pk)
            serializer = ImageSerializer(image)
            return Response(serializer.data)
        except Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


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
        fields = ('id', 'img_url', 'description', 'folder', 'tags')
        depth=1
