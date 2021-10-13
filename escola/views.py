from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer



class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas do BD"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Cursos do BD"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as Matriculas do BD"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
