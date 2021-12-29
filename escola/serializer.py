from rest_framework import serializers
from .models import Aluno, Professor, Turma


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = "__all__"


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"


class TurmaSerializer(serializers.ModelSerializer):

    alunos = AlunoSerializer(many=True, read_only=True)
    professores = ProfessorSerializer(many=True, read_only=True)

    class Meta:
        model = Turma
        fields = (
            "id",
            "nome",
            "qtd_alunos",
            "qtd_professores",
            "lista_materias",
            "alunos",
            "professores",
        )

    ## TODO: CRIAR UM JEITO DE CRIAR UMA TURMA PELA API

    def update(self, instance, validated_data):
        ## TODO: Criar método de verificar se o método está tentando atualizar os professores | alunos | turma
        ## TODO: Retornar instancia atualizada
        return super().update(instance ,validated_data)