import java.util.ArrayList;

public class Teste {

  public static void main(String[] args) {

   ArrayList lista = new ArrayList();
   ContaCorrente cc = new ContaCorrente(22, 11);
   lista.add(cc);
   
   ContaCorrente cc1 = new ContaCorrente(33, 322);
   lista.add(cc1);

   ContaCorrente cc2 = new ContaCorrente(44, 422);
   lista.add(cc2);
   
   System.out.println(lista.size());
   
   for(Object o : lista) {
     System.out.println(o);
   }
  }

}
