from rest_framework import serializers
from .models import MediaCatalog, MediaUsuarios
 
class MediaCatalogSerializer(serializers.ModelSerializer):
    num_usuarios = serializers.IntegerField()
    avg_score = serializers.FloatField()

    class Meta:
        model = MediaCatalog
        fields = ('nombre','genero', 'tipo', 'num_usuarios', 'avg_score')