package training;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;


public class Order {

  private Date moment;
  private OrderStatus status;

  List<OrderItem> orderItem = new ArrayList<>();
  List<Client> client = new ArrayList<>();

  public List<Client> getClient() {
    return client;
  }

  public Order() {

  }

  public Order(Date moment, OrderStatus status) {
    this.moment = moment;
    this.status = status;
  }

  public Date getMoment() {
    return moment;
  }

  public void setMoment(Date moment) {
    this.moment = moment;
  }

  public OrderStatus getStatus() {
    return status;
  }

  public void setStatus(OrderStatus status) {
    this.status = status;
  }

  public List<OrderItem> getOrderItem() {
    return orderItem;
  }

  
  public void addItem(OrderItem item) {
    orderItem.add(item);
  }
  
  public void removeItem(OrderItem item) {
    orderItem.remove(item);
  }

  public void total(Double total) {
    for(OrderItem o : orderItem) {
      total = o.getQuantity() * o.getPrice();
    }
  }

}
