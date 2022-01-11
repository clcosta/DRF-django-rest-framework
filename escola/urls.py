from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import AlunoViewSet, ProfessorViewSet, TurmaViewSet, IndexView

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet, basename='alunos')
router.register(r'professores', ProfessorViewSet, basename='professores')
router.register(r'turmas', TurmaViewSet, basename='turmas')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name="token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('', IndexView.as_view(), name="index"),
    path('api/', include((router.urls, "api")), name="api"),
]
