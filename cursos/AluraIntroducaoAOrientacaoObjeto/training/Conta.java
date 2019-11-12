package training;

public class Conta {

  double saldo;
  int agencia;
  int numero;
  String titular;

  void deposita(double valor) {
    saldo += valor;
  }
}
