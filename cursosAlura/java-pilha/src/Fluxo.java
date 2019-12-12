public class Fluxo {

  public static void main(String[] args) {
    System.out.println("Ini do main");
    try { //lança um excexão
      metodo1();      
    } catch(ArithmeticException | NullPointerException | MinhaExcecao ex) { // captura a excexão
      String msg = ex.getMessage();
      System.out.println("Excption " + msg);
      ex.printStackTrace();
    }
  }

  private static void metodo1() {
    System.out.println("Ini do metodo1");
    try {
      metodo2();
    } catch (ArithmeticException ex) {
      System.out.println("ArithmeticExeption");
    }
    System.out.println("Fim do metodo1");
  }

  private static void metodo2() {
    System.out.println("Ini do metodo2");
    throw new MinhaExcecao("Deu muito errado");
    
//    System.out.println("Fim do metodo2");
  }
}