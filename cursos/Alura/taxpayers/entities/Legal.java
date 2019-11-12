package entities;

public class Legal extends Taxpayers {

  private Integer numberEmployees;

  public Legal() {
    super();
  }

  public Legal(String name, Double income, Integer numberEmployees) {
    super(name, income);
    this.numberEmployees = numberEmployees;
  }

  public Integer getNumberEmployees() {
    return numberEmployees;
  }

  public void setNumberEmployees(Integer numberEmployees) {
    this.numberEmployees = numberEmployees;
  }

  @Override
  public Double tax() {
    if (numberEmployees > 10) {
      return getIncome() * 14 / 100;
    } else {
      return getIncome() * 16 / 100;
    }
  }

}
