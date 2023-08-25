from django.db.models.functions import Random
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from typing import Literal, Union

import json

from user.models import User
from .functions import join_media_and_count, save_data_on_MediaUsuarios
from .models import MediaCatalog, MediaUsuarios, MediaUsuariosCount
from .serializer import MediaCatalogSerializer


@api_view(['GET'])
def index(request: Request) -> dict[str, str]:
    message = 'Está en la vista Media. Utilice alguno de los \
                    siguientes endpoints: \
                        - get-random \
                        - get-filtered-by \
                        - get-one \
                        - watched \
                        - scored'

    return Response({'mensaje': message})


@api_view(['GET'])
def get_random_media(request: Request) -> dict:
    random_media =join_media_and_count().order_by(Random()).first()
    serializer = MediaCatalogSerializer(random_media)

    return Response(serializer.data)


@api_view(['GET'])
def get_media_filtered(request: Request,
                       field_name: Literal['nombre', 'genero', 'tipo']) -> Union[list[dict], dict[str, str]]:
    try:
        media_filtered = join_media_and_count().order_by(field_name)
        serializer = MediaCatalogSerializer(media_filtered, many=True)

        return Response(serializer.data)

    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except MediaCatalog.DoesNotExist:
        return Response({"detail": "Media no encontrada"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def get_one_media(request: Request) -> list[dict]:
    try:
        media = join_media_and_count().filter(**request.data)
        serializer = MediaCatalogSerializer(media, many=True)

        return Response(serializer.data)

    except MediaCatalog.DoesNotExist:
        return Response({"detail": "Media no encontrada"}, status=status.HTTP_404_NOT_FOUND)


@login_required
@api_view(['POST'])
def change_to_watched(request: Request, media_pk: int) -> str:
    try:
        user_pk = request.user.pk
        if MediaUsuarios.objects.filter(media_id=media_pk, usuario_id=user_pk).exists():
            return Response('Este usuario ya registró como vista esta película')

        media_instance = get_object_or_404(MediaCatalog, pk=media_pk)

        media_user_relationship = MediaUsuarios(
            media=media_instance,
            usuario=get_object_or_404(User, pk=user_pk),
            puntaje=None
        )
        media_user_relationship.save()

        result = save_data_on_MediaUsuarios(media_instance)

        return Response('Se registró correctamente')

    except MediaCatalog.DoesNotExist:
        return Response({"detail": "Media no encontrada"}, status=status.HTTP_404_NOT_FOUND)


@login_required
@api_view(['POST'])
def score_media(request: Request, media_pk: int, score_value: int) -> str:
    try:
        user_pk = request.user.pk
        media_instance = get_object_or_404(MediaCatalog, pk=media_pk)
        media_user_relationship = MediaUsuarios.objects.get(
            media_id=media_pk, usuario_id=user_pk)
        media_user_relationship.puntaje = score_value
        media_user_relationship.save()

        result = save_data_on_MediaUsuarios(media_instance)

        return Response('El usuario puntuó la película')

    except MediaUsuarios.DoesNotExist:
        return Response({"detail": "El usuario debe ver la película para poder puntuarla"}, status=status.HTTP_404_NOT_FOUND)
