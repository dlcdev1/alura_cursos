package entities;

public class Acco {

  private Integer number;
  private String holder;
  protected Double balance; // modificador de acesso protect para dar visibilidade as classes
                            // extendidas.

  public Acco() {

  }

  public Acco(Integer number, String holder, Double balance) {
    this.number = number;
    this.holder = holder;
    this.balance = balance;
  }

  public Integer getNumber() {
    return number;
  }

  public void setNumber(Integer number) {
    this.number = number;
  }

  public String getHol() {
    return holder;
  }

  public void setHol(String hol) {
    this.holder = hol;
  }

  public Double getBalance() {
    return balance;
  }

  public void withdraw(double amount) {
    balance -= amount + 5.0;
  }

  public void deposit(double amount) {
    balance += amount;
  }

}
