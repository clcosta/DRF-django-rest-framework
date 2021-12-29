from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import AlunoViewSet, ProfessorViewSet, TurmaViewSet

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet, basename='alunos')
router.register(r'professores', ProfessorViewSet, basename='professores')
router.register(r'turmas', TurmaViewSet, basename='turmas')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls)),
]
