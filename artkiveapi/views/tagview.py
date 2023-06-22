from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from artkiveapi.models import Tag

class TagView(ViewSet):

    def retrieve(self, request, pk):
        tags = Tag.objects.get(pk=pk)
        serializer = TagSerializer(tags)
        return Response(serializer.data)
    
    def list(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tag_name')


