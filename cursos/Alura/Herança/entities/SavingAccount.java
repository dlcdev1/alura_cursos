package entities;

public class SavingAccount extends Acco {

  private Double interestRate;

  public SavingAccount() {
    super();
  }

  public SavingAccount(Integer number, String holder, Double balance, Double interestRate) {
    super(number, holder, balance);
    this.interestRate = interestRate;
  }

  public Double getInterestRate() {
    return interestRate;
  }

  public void setInterestRate(Double interestRate) {
    this.interestRate = interestRate;
  }

  public void updateBalance() {
    balance += balance * interestRate;
  }

  @Override
  public void withdraw(double amount) {
    balance -= amount;
  }
}
