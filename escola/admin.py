from django.contrib import admin
from .models import Aluno, Professor

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display =  ('id','nome','cpf','ano_escolar')
    search_fields = ('nome','cpf')

    class Meta:
        verbose_name_plural = "Alunos"

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id','nome','cpf', 'materia')

    search_fields = ('nome','cpf')
