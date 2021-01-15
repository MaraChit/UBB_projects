package Models;

public class Product {

    private String name;
    private int price;

    //constructor
    public Product(String name, int price){
        this.name = name;
        this.price = price;
    }

    // getters and setters
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return name + " " + price;
    }
}
