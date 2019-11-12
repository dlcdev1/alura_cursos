package application;


import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

import entities.ImportedProduct;
import entities.Product;
import entities.UsedProduct;

public class AppProduct {

  public static void main(String[] args) throws ParseException {
  
    Locale.setDefault(Locale.US);
    Scanner sc = new Scanner(System.in);
    
    SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
    
    List<Product> list = new ArrayList<>();
    String name;
    double price;
 
    System.out.print("Enter the number of product: ");
    int numberProduct = sc.nextInt();
    
    for(int i = 0; i < numberProduct; i++) {
      
      System.out.println("Product #" + (i+1) + " data:");
      System.out.println("Common, used imported (c/u/i)");
      char ch = sc.next().charAt(0);
      sc.nextLine();
      if(ch == 'c') {
        System.out.print("Name: ");
        name = sc.nextLine();
        System.out.print("Price: ");
        price = sc.nextDouble();        
        list.add(new Product(name, price));
        
      }
      if(ch == 'u') {
        System.out.print("Name: ");
        name = sc.nextLine();
        System.out.print("Price: ");
        price = sc.nextDouble();
        sc.nextLine();
        System.out.print("Monufacture date (DD/MM/YYYY): ");
        Date date = sdf.parse(sc.next());
        list.add(new UsedProduct(name, price, date));
      }
      if(ch == 'i') {
        System.out.print("Name: ");
        name = sc.nextLine();
        System.out.print("Price: ");
        price = sc.nextDouble();
        System.out.print("Customs fee: ");
        double customsFee = sc.nextDouble();
        list.add(new ImportedProduct(name, price, customsFee));
      }
      
    }
    System.out.println();
    System.out.println("PRICE TAGS:");
    for(Product prod : list) {
      System.out.println(prod.priceTag());
    }

  }

}
