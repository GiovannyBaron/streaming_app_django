from django.db.models import Avg, F, IntegerField
from django.db.models.functions import Coalesce

from .models import MediaCatalog, MediaUsuarios, MediaUsuariosCount


def join_media_and_count():
    return MediaCatalog.objects.annotate(
            num_usuarios=Coalesce(F('mediausuarioscount__num_usuarios'), 0, output_field=IntegerField()),
            avg_score=F('mediausuarioscount__avg_score'))


def save_data_on_MediaUsuarios(media_instance:MediaCatalog) -> bool:
    media_count_instance, created = MediaUsuariosCount.objects.get_or_create(
        media=media_instance,
        defaults={'num_usuarios': 0, 'avg_score': None}
    )
    
    filtered_media = MediaUsuarios.objects.filter(media_id=media_instance.pk)
    media_count_instance.num_usuarios = filtered_media.count()
    media_count_instance.avg_score = filtered_media.aggregate(Avg('puntaje'))['puntaje__avg']

    return media_count_instance.save()