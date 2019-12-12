package br.com.alura;

import java.util.Iterator;
import java.util.Set;

public class TestaCursoComAluno {

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
    
    
    Set<Aluno> alunos = javaColecoes.getAlunos();
    Iterator<Aluno> iterador = alunos.iterator();
    
    while(iterador.hasNext()) {
      Aluno proximo = iterador.next();
      System.out.println(proximo);
    }
    
    for(Aluno a : javaColecoes.getAlunos()) {
      System.out.println(a);
    }
    
    System.out.println("Quebra de linha");
    System.out.println("Todos os alunos matriculados: ");
    javaColecoes.getAlunos().forEach(a -> {
      System.out.println(a);
    });
    
    System.out.println("O aluno " + a1 + " está matriculado? ");
    System.out.println(javaColecoes.estaMatriculado(a1));
    
    Aluno turini = new Aluno("Rodrigo Turini", 346782);
    System.out.println(javaColecoes.estaMatriculado(turini));
    
    System.out.println("O a1 é equals ao Turini?");
    System.out.println(a1.equals(turini));
    
    System.out.println(a1.hashCode() ==  turini.hashCode());

  }

}
