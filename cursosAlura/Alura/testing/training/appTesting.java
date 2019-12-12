package training;

import java.util.Arrays;
import java.util.List;

public class appTesting {

  public static void main(String[] args) {

    List<Integer> myInts = Arrays.asList(5, 2, 10);
    printList(myInts);
    
    List<String> mystrs = Arrays.asList("Maria", "Alex", "Bob");
    printList(mystrs);
       
  }
  
  

  public static void printList(List<?> list) {
    for(Object obj : list) {
      System.out.println(obj.hashCode());
    }
  }
 
}
