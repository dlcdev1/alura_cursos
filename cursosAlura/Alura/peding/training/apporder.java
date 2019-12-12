package training;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class apporder {

  public static void main(String[] args) throws ParseException {
    
    Scanner sc = new Scanner(System.in);
    SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyy HH:mm:ss");
    
    System.out.println("Quantity number:");
    int quantityUser = sc.nextInt();
    
    for(int i = 0; i < quantityUser; i ++) {
      sc.nextLine();
      System.out.println("Name: ");
      String name = sc.nextLine();
      System.out.println("E-mail");
      String email = sc.nextLine();
      System.out.println("Birth date (DD/MM/YYYY)");
      Date birthDate = sdf.parse(sc.nextLine());
      
      Client client = new Client(name, email, birthDate );
  
    }
  }

}
