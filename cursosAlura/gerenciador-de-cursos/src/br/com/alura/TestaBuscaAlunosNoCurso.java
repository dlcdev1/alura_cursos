package br.com.alura;

public class TestaBuscaAlunosNoCurso {

  public static void main(String[] args) {

    Curso javaColecoes = new Curso("Dominando as coleções do Java", "Paulo Silveira");

    javaColecoes.adiciona(new Aula("Trabalhjando com ArrayList", 21));
    javaColecoes.adiciona(new Aula("Criando uma Aula", 20));
    javaColecoes.adiciona(new Aula("Modelando com coleções", 22));
    
    Aluno a1 = new Aluno("Rodrigo Turini", 346782);
    Aluno a2 = new Aluno("Ghilherme Silveira", 5617);
    Aluno a3 = new Aluno("Mauricio Aniche", 17645);
    
    javaColecoes.matricular(a1);
    javaColecoes.matricular(a2);
    javaColecoes.matricular(a3);
    
    System.out.println("Quem é o aluno com matricula 5617?");
    Aluno aluno = javaColecoes.buscaMatriculado(5617);
    System.out.println("aluno: " + aluno);
  }

}
