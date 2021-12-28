from django.test import TestCase
from escola.models import Aluno, Professor
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
            cpf= "000.000.000-00",
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