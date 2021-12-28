from rest_framework import serializers
from .models import Aluno, Professor, Turma

class AlunoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Aluno
        fields = ('id','nome', 'ano_escolar')

class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = ('id','nome', 'materia')

class TurmaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Turma
        fields = ("nome", "lista_professores", "lista_alunos", "list_materias", "qtd_alunos","qtd_professores")