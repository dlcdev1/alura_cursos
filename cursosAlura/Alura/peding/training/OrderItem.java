package training;

import java.util.ArrayList;
import java.util.List;

public class OrderItem {

  private Integer quantity;
  private Double price;

  List<Product> product = new ArrayList<>();
  List<Order> order = new ArrayList<>();

  public List<Order> getOrder() {
    return order;
  }

  public OrderItem() {

  }

  public OrderItem(Integer quantity, Double price) {
    this.quantity = quantity;
    this.price = price;
  }

  public Integer getQuantity() {
    return quantity;
  }

  public void setQuantity(Integer quantity) {
    this.quantity = quantity;
  }

  public Double getPrice() {
    return price;
  }

  public void setPrice(Double price) {
    this.price = price;
  }

  public List<Product> getProduct() {
    return product;
  }

  public void subTotal(Double subTotal) {
    subTotal += price;
  }


}
