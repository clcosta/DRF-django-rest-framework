from django.db import models


class Aluno(models.Model):

    ANO_9 = u"9° Ano"
    ANO_8 = u"8° Ano"
    ANO_7 = u"7° Ano"
    ANO_6 = u"6° Ano"
    ANO_5 = u"5° Ano"
    ANO_4 = u"4° Ano"
    ANO_3 = u"3° Ano"
    ANO_2 = u"2° Ano"
    ANO_1 = u"1° Ano"
    ANO_1_MEDIO = u"1° Ano Médio"
    ANO_2_MEDIO = u"2° Ano Médio"
    ANO_3_MEDIO = u"3° Ano Médio"

    ano_escolar_choices = (
        (ANO_9, f"{ANO_9}"),
        (ANO_8, f"{ANO_8}"),
        (ANO_7, f"{ANO_7}"),
        (ANO_6, f"{ANO_6}"),
        (ANO_5, f"{ANO_5}"),
        (ANO_4, f"{ANO_4}"),
        (ANO_3, f"{ANO_3}"),
        (ANO_2, f"{ANO_2}"),
        (ANO_1, f"{ANO_1}"),
        (ANO_1_MEDIO, f"{ANO_1_MEDIO}"),
        (ANO_2_MEDIO, f"{ANO_2_MEDIO}"),
        (ANO_3_MEDIO, f"{ANO_3_MEDIO}"),
    )

    nome = models.CharField(max_length=30, blank=False, null=False)
    cpf = models.CharField(max_length=14, blank=False, null=False, unique=True)

    ano_escolar = models.CharField(
        max_length=12,
        choices=ano_escolar_choices,
        default=ANO_1,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.nome


class Professor(models.Model):

    MATEMATICA = u"Matemática"
    PORTUGUES = u"Português"
    GEOGRAFIA = u"Geografia"
    SOCIOLOGIA = u"Sociologia"
    HISTORIA = u"História"
    FILOSOFIA = u"Folosofia"
    BIOLOGIA = u"Biologia"

    materias_choices = (
        (MATEMATICA, f"{MATEMATICA}"),
        (PORTUGUES, f"{PORTUGUES}"),
        (GEOGRAFIA, f"{GEOGRAFIA}"),
        (SOCIOLOGIA, f"{SOCIOLOGIA}"),
        (HISTORIA, f"{HISTORIA}"),
        (FILOSOFIA, f"{FILOSOFIA}"),
        (BIOLOGIA, f"{BIOLOGIA}"),
    )

    nome = models.CharField(max_length=40, blank=False, null=False)
    cpf = models.CharField(max_length=14, blank=False, null=False, unique=True)
    materia = models.CharField(max_length=50, blank=False, null=False, choices=materias_choices)

    def __str__(self):
        return self.nome + f' ({self.materia})'

    
    class Meta:
        verbose_name_plural = "Professores"

class Turma(models.Model):

    nome = models.CharField(max_length=25, blank=False, null=False, default="3° Ano A - Manhã")
    professor = models.ManyToManyField("Professor", related_name="professores")
    alunos = models.ManyToManyField("Aluno", related_name="alunos")

    @property
    def qtd_alunos(self):
        return len(self.alunos.all())
    
    @property
    def qtd_professores(self):
        return len(self.professor.all())

    @property
    def list_materias(self):
        professores = self.professor.all()
        materias = [professor.materia for professor in professores if professor.materia]
        return materias
    
    @property
    def lista_alunos(self):
        alunos = [aluno.nome for aluno in self.alunos.all()]
        return alunos
    
    @property
    def lista_professores(self):
        professores = [professor.nome for professor in self.professor.all()]
        return professores

    def __str__(self):
        return self.nome + f" ({self.qtd_alunos} Alunos - {self.qtd_professores} Professores)"

    class Meta:
        verbose_name_plural = "Turmas"