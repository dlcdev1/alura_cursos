package training;

import java.util.Arrays;
import java.util.List;

public class referencia {

  public static void main(String[] args) {

    List<String> nomes = Arrays.asList("Lucas", "Rodrigo", "Paulo");
    for(String nome : nomes) {
        System.out.println(nome);
    }
    
    System.out.println("\nLambda\n");
    
    nomes.forEach(nome -> System.out.println(nome));
    
    System.out.println("\nReferencia\n");
    nomes.forEach(System.out::println);
  }

}
