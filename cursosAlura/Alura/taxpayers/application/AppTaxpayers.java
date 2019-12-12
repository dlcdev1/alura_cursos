package application;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

import entities.Legal;
import entities.PhysicalPerson;
import entities.Taxpayers;

public class AppTaxpayers {

  public static void main(String[] args) {
    Locale.setDefault(Locale.US);
    Scanner sc = new Scanner(System.in);

    List<Taxpayers> list = new ArrayList<>();
    String name;
    double income;
    // FIXME algum bug conhecido que precisar ser corrigido
    // XXX alguma coisa que presicamos refatorar
    System.out.print("Enter the numbrer of tax payeres: ");
    int numberPayeres = sc.nextInt();
    sc.nextLine();

    for (int i = 0; i < numberPayeres; i++) {
      System.out.println("Tax payer #" + (i + 1) + " data:");
      System.out.print("Individual or company (i/c)? ");
      char ch = sc.next().charAt(0);
      sc.nextLine();

      if (ch == 'i') {
        System.out.print("Name: ");
        name = sc.nextLine();
        System.out.print("Anual income: ");
        income = sc.nextDouble();
        System.out.print("Health expenditures: ");
        double healthRate = sc.nextDouble();
        list.add(new PhysicalPerson(name, income, healthRate));
      } else if (ch == 'c') {
        System.out.print("Name: ");
        name = sc.nextLine();
        System.out.print("Anual income: ");
        income = sc.nextDouble();
        System.out.print("Number of employees");
        int numberEmployees = sc.nextInt();
        list.add(new Legal(name, income, numberEmployees));
      }

    }

    System.out.println();
    System.out.println("TAXES PAID: ");
    double sum = 0.0;
    for (Taxpayers tax : list) {

      System.out.println(tax.getName() + " $ " + tax.tax());
      sum += tax.tax();
    }

    System.out.println();
    System.out.println("TOTAL TAXES: $ " + String.format("%.2f", sum));


  }

}
