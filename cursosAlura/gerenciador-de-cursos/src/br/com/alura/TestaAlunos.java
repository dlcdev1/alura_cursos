package br.com.alura;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class TestaAlunos {

  public static void main(String[] args) {

    Collection<String> alunos = new HashSet<>();
    alunos.add("Rodrigo Turini");
    alunos.add("Roberto Souza");
    alunos.add("Nico Steppat");
    alunos.add("Sergio Lopes");
    alunos.add("Renan Saggio");
    alunos.add("Mauricio Aniche");
    alunos.add("Mauricio Aniche");
    
    
    boolean paulaEstaMatriculado = alunos.contains("Paulo Silveira");
    alunos.remove("Sergio Lopes");
    
    System.out.println(alunos.size());
    for (String aluno : alunos) {
      System.out.println(aluno);
    }
    
    alunos.forEach(aluno -> {
      System.out.println(aluno);
    });
    
    System.out.println(alunos);
     
   List<String> alunosEmLista = new ArrayList<>(alunos);
   

   Set<String> alunoE = new HashSet<>();
   alunoE.add("Paulo");
   alunoE.add("Alberto");
   alunoE.add("Pedro");
   alunoE.add("Nico");
   
   for (String aluno : alunoE) {
    System.out.println(aluno);
  }
   
  }

}
