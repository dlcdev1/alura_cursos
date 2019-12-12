package entities;

public class PhysicalPerson extends Taxpayers {

  private Double healthRate;

  public PhysicalPerson() {
    super();
  }

  public PhysicalPerson(String name, Double income, Double healthRate) {
    super(name, income);
    this.healthRate = healthRate;
  }

  public Double getHealthRate() {
    return healthRate;
  }

  public void setHealthRate(Double healthRate) {
    this.healthRate = healthRate;
  }

  @Override
  public Double tax() {
    if(getIncome() < 20000.0) {
      return getIncome() * 0.15 - healthRate * 0.5;
    } else {
      return getIncome() * 0.25 - healthRate * 0.5;
    }
  }


}
