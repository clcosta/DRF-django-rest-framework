from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Aluno, Professor, Turma
from .serializer import AlunoSerializer, ProfessorSerializer, TurmaSerializer


class AlunoViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class ProfessorViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)

    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class TurmaViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)

    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer