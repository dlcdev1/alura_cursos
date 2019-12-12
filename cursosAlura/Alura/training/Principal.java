package training;

import java.util.Calendar;
import java.util.GregorianCalendar;

public class Principal {
  public static void main(String[] args) {
    Calendar dataNascimento = new GregorianCalendar(1985, 3, 18);
    Funcionario funcionarios = new Funcionario("Jose", 25, dataNascimento );
    System.out.println(funcionarios);
  }
}
