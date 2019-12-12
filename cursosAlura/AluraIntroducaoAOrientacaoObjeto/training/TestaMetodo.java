package training;

public class TestaMetodo {

  public static void main(String[] args) {
    Conta conta = new Conta();

    conta.saldo = 100;
    conta.deposita(200);
    System.out.println(conta.saldo);
  }

}
