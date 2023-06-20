from django.http import HttpResponseNotFound
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status, serializers
from artkiveapi.models import Folder, Muser

class FolderView(ViewSet):
    """Folder view"""

    def create(self, request):
        """Handle POST request for creating a folder
        Returns: Response -- JSON serialized folder instance"""
        muser = Muser.objects.get(user=request.auth.user)
        folder = Folder.objects.create(
            folder_name=request.data["folder_name"],
            creator=muser
        )
        serializer = FolderSerializer(folder)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def list(self, request):
        """Handle GET request to retrieve folders
        Returns: Response -- JSON serialized list of folder instances"""
        muser = Muser.objects.get(user=request.auth.user)
        folders = Folder.objects.filter(creator=muser)  # Filter folders by creator

        serializer = FolderSerializer(folders, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT request for editing a folder
        Returns: Response -- JSON serialized folder instance"""
        try:
            folder = Folder.objects.get(pk=pk)
            muser = Muser.objects.get(user=request.auth.user)

            folder_name = request.data.get("folder_name")
            folder.folder_name = folder_name
            folder.creator = muser

            folder.save()

            serializer = FolderSerializer(folder)
            return Response(serializer.data)
        except Folder.DoesNotExist:
            return HttpResponseNotFound()

    def destroy(self, request, pk):
        """Handle DELETE request for deleting a folder
        Returns: Response -- Empty body with 204 status code"""
        try:
            folder = Folder.objects.get(pk=pk)
            folder.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Folder.DoesNotExist:
            return HttpResponseNotFound()



class FolderSerializer(serializers.ModelSerializer):
    """JSON serializer for the folders"""

    class Meta:
        model = Folder
        fields = ('id', 'creator', 'folder_name')
