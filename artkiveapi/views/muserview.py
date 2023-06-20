from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from artkiveapi.models import Muser

class MuserView(ViewSet):
    def list(self, request):
        muser = Muser.objects.get(user=request.auth.user)
        serializer = MuserSerializer(muser, many=False)
        return Response(serializer.data)

class MuserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Muser
        fields = ('id', 'user', 'bio', 'username')
