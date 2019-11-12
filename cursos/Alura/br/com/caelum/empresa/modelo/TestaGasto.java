package br.com.caelum.empresa.modelo;

import java.util.Calendar;
import java.util.GregorianCalendar;

import training.Funcionario;

public class TestaGasto {
  public static void main(String[] args) {
    Calendar dataNascimento = new GregorianCalendar(1989, 3, 14);
    Funcionario funcionarios = new Funcionario("Vinicius", 9, dataNascimento);
    Calendar hoje = Calendar.getInstance();

    Gasto gastos_kk = new Gasto(40, "Taxi", funcionarios, hoje, false);
    Gasto gastos1 = new Gasto(40, "Taxi", funcionarios, hoje, true);
    Gasto gastos2 = new Gasto(40, "Taxi", funcionarios, hoje, true);
    
    System.out.println(gastos_kk);
    System.out.println(gastos1);
    System.out.println(gastos2);
  }
}
