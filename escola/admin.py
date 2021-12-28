from django.contrib import admin
from .models import Aluno, Professor, Turma

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

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    
    list_display = ('id','nome')

    search_fields = ('id','nome')

    list_filter = ('nome',)

    list_display_links = ('nome',)