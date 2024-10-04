from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.eventin.views import (
    EventoViewSet,
    ParcicipanteViewSet,
    InscricaoViewSet,
    ListaInscricoesEvento,
    ListaInscricoesParticipante,
)


router = routers.DefaultRouter()
router.register("eventos", EventoViewSet, basename="Eventos")
router.register("participantes", ParcicipanteViewSet, basename="Parcicipantes")
router.register("inscricoes", InscricaoViewSet, basename="Inscrições")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path(
        "participantes/<int:pk>/inscricoes/",
        ListaInscricoesParticipante.as_view(),
        name="Participantes",
    ),
    path(
        "eventos/<int:pk>/inscricoes/",
        ListaInscricoesEvento.as_view(),
        name="Eventos",
    ),
]
