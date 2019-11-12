package application;

import java.util.HashMap;
import java.util.Map;

import entities.ProductMaps;

public class ProductMapsHashTree {
  
  public static void main(String[] args) {
    
    Map<ProductMaps, Double> cookies = new HashMap<>();
    
    ProductMaps p1 = new ProductMaps("Tv", 900.0);
    ProductMaps p2 = new ProductMaps("Notebook", 1200.0);
    ProductMaps p3 = new ProductMaps("Tablet", 400.0);
    
    cookies.put(p1, 10000.0);
    cookies.put(p2, 20000.0);
    cookies.put(p3, 15000.0);
    
    ProductMaps ps = new ProductMaps("Tv", 900.0);
    
    System.out.println("Contains 'ps' key: " + cookies.containsKey(ps));
    
    for(ProductMaps key : cookies.keySet()) {
      System.out.println(key + ": " + cookies.get(key));
    }
  }

}
