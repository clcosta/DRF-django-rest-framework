from django.test import TestCase
from escola.models import Aluno, Professor, Turma
from django.db.utils import IntegrityError


class TestModelAluno(TestCase):
    def setUp(self):
        self.aluno = Aluno(
            nome="test", cpf="111.111.111-11", ano_escolar=Aluno.ANO_3_MEDIO
        )

    def test_dunder_str_method(self):
        expected = "test"
        result = str(self.aluno)
        self.assertEqual(expected, result)

    def test_nome_aluno(self):
        expected = "test"
        result = self.aluno.nome
        self.assertEqual(expected, result)

    def test_cpf_aluno(self):
        expected = "111.111.111-11"
        result = self.aluno.cpf
        self.assertEqual(expected, result)

    def test_ano_escolar(self):
        expected = Aluno.ANO_3_MEDIO
        result = self.aluno.ano_escolar
        self.assertEqual(expected, result)

    def test_cpf_unique(self):
        ## Save object with one cpf and try save another obj with the same cpf -> expected : IntegrityError (UNIQUE failure)
        try:
            self.aluno.save()
            aluno2 = Aluno.objects.create(
                nome=self.aluno.nome,
                cpf=self.aluno.cpf,
                ano_escolar=self.aluno.ano_escolar,
            )
        except IntegrityError as error:
            self.assertRaises(IntegrityError)


class TestModelProfessor(TestCase):
    def setUp(self):
        self.professor = Professor(
            nome="test professor",
            cpf="000.000.000-00",
            materia=Professor.MATEMATICA,
        )

    def test_dunder_str_method(self):
        expected = f"test professor ({self.professor.materia})"
        result = str(self.professor)
        self.assertEqual(expected, result)

    def test_nome_professor(self):
        expected = "test professor"
        result = self.professor.nome
        self.assertEqual(expected, result)

    def test_cpf_professor(self):
        expected = "000.000.000-00"
        result = self.professor.cpf
        self.assertEqual(expected, result)

    def test_materia_professor(self):
        expected = Professor.MATEMATICA
        result = self.professor.materia
        self.assertEqual(expected, result)

    def test_cpf_unique(self):
        ## Save object with one cpf and try save another obj with the same cpf -> expected : IntegrityError (UNIQUE failure)
        try:
            self.professor.save()
            professor2 = Professor.objects.create(
                nome=self.professor.nome,
                cpf=self.professor.cpf,
                materia=self.professor.materia,
            )
        except IntegrityError as error:
            self.assertRaises(IntegrityError)


class TestModelTurma(TestCase):
    def setUp(self):
        self.aluno1 = Aluno.objects.create(
            nome="aluno 1", cpf="111.111.111-11", ano_escolar=Aluno.ANO_3_MEDIO
        )
        self.aluno2 = Aluno.objects.create(
            nome="aluno 2", cpf="222.222.222-22", ano_escolar=Aluno.ANO_3_MEDIO
        )
        self.professor1 = Professor.objects.create(
            nome="professor 1",
            cpf="333.333.333-33",
            materia=Professor.MATEMATICA,
        )
        self.professor2 = Professor.objects.create(
            nome="professor2",
            cpf="444.444.444-44",
            materia=Professor.GEOGRAFIA,
        )
        self.turma = Turma.objects.create(nome="3° Ano Teste - Noite")
        self.turma.professores.add(self.professor1, self.professor2)
        self.turma.alunos.add(self.aluno1, self.aluno2)

    def test_nome_turma(self):
        expected = "3° Ano Teste - Noite"
        result = self.turma.nome
        self.assertEqual(expected, result)

    def test_dunder_str_method(self):
        expected = "3° Ano Teste - Noite (2 Alunos - 2 Professores)"
        result = str(self.turma)
        self.assertEqual(expected, result)

    def test_qtde_de_alunos(self):
        expected = 2
        result = self.turma.qtd_alunos
        self.assertEqual(expected, result)

    def test_qtde_de_professores(self):
        expected = 2
        result = self.turma.qtd_professores
        self.assertEqual(expected, result)

    def test_lista_alunos(self):
        expected = ["aluno 1", "aluno 2"]
        result = self.turma.lista_alunos
        self.assertEqual(expected, result)

    def test_lista_professores(self):
        expected = ["professor 1", "professor2"]
        result = self.turma.lista_professores
        self.assertEqual(expected, result)

    def test_lista_materias(self):
        expected = ["Matemática","Geografia"]
        result = self.turma.list_materias
        self.assertEqual(expected, result)

    def test_turma_nome_unique(self):
        try:
            turma2 = Turma.objects.create(
                nome=self.turma.nome,
            )
        except IntegrityError as error:
            self.assertRaises(IntegrityError)

    def test_access_alunos_by_turma(self):
        alunos = Aluno.objects.all()
        expected = alunos.order_by("id")
        result = self.turma.alunos.all().order_by("id")
        self.assertQuerysetEqual(expected, result)

    def test_access_professores_by_turma(self):
        professores = Professor.objects.all()
        expected = professores.order_by("id")
        result = self.turma.professores.all().order_by("id")
        self.assertQuerysetEqual(expected, result)
