package application;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class ReadingFiles {

  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);
    
    System.out.println("Enter file full path: ");
    String path = sc.nextLine();
    
    
    try (BufferedReader br = new BufferedReader(new FileReader(path))){
      
      
      
      
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }
        
    sc.close();
  }

}
