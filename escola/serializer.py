from rest_framework import serializers
from .models import Aluno, Professor

class AlunoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Aluno
        fields = ('id','nome', 'ano_escolar')

class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = ('id','nome', 'materia')