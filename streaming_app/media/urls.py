from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="get_wave"),
    path("get-random/", views.get_random_media, name="get_random"),
    path("get-filtered-by/<str:field_name>/", views.get_media_filtered, name="get_filtered"),
    path("get-one/", views.get_one_media, name="get_one"),
    path("watched/<int:media_pk>/", views.change_to_watched, name="watched"),
    path("scored/<int:media_pk>/<int:score_value>/", views.score_media, name="scored"),
]