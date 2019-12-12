package entities;

public class SavingsAccountPlus extends SavingAccount{
  
  @Override
  public void withdraw(double amount) {
    balance -= amount + 2.0;
  }
}
