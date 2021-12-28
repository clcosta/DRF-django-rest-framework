from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from escola.views import AlunoViewSet, ProfessorViewSet, TurmaViewSet

router = routers.DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'professores', ProfessorViewSet)
router.register(r'turmas', TurmaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
