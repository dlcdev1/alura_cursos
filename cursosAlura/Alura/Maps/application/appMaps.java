package application;

import java.util.Map;
import java.util.TreeMap;

public class appMaps {

  public static void main(String[] args) {
    
    Map<String, String> cookies = new TreeMap<>();
    
    cookies.put("usernamne", "Maria");
    cookies.put("email", "maria@gmail.com");
    cookies.put("phone", "99771133");
    
    cookies.remove("email");
    cookies.put("phone", "997771133");
    
    System.out.println("ALL COOKIES:");
    
    for(String key : cookies.keySet()) {
      System.out.println(key + ": " + cookies.get(key));
    }
  }

}
