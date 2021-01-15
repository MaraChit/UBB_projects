package Repositories;

import Models.Bill;
import Models.Product;

import java.util.*;

public class ProductLockInventory implements Inventory {

    private Map<Product, Integer> currentStock;
    private int income;
    private List<Bill> processedBills;

    public ProductLockInventory(){
        this.currentStock = new HashMap<>();
        this.income = 0;
        this.processedBills = new ArrayList<>();
    }

    @Override
    public void resetStock(List<AbstractMap.SimpleEntry<Product, Integer>> productList) {
        this.currentStock = new HashMap<>();

        productList.forEach(product -> {
            currentStock.put(product.getKey(), product.getValue());
        });
    }

    @Override
    synchronized public void checkInventory() {
        int expectedSum = this.processedBills.stream()
                .map(Bill::getTotalSum)
                .reduce(0, Integer::sum);

        if (expectedSum != this.income) {
            System.out.println("INVENTORY CHECK FAILED - INCOME DOES NOT CORRESPOND WITH SALES OPERATIONS");
        }
    }

    @Override
    public void processBill(Bill bill) {
        // process bill & lock only modified products

        for (AbstractMap.SimpleEntry<Product, Integer> billProduct: bill.getProductList()) {
            currentStock.computeIfPresent(billProduct.getKey(), (inventoryProduct, quantity) -> {

                synchronized (quantity){
                    if (billProduct.getValue().compareTo(quantity) <= 0) {
                        return quantity - billProduct.getValue();
                    }
                    else {
                        System.out.println("Insufficient stock");
                        return quantity;
                    }
                }
            });
        }
        synchronized (this) {

            this.income = this.income + bill.getTotalSum();
            this.processedBills.add(bill);
        }
    }

    @Override
    public String toString() {
        return "ProductLockInventory{" +
                ", currentStock=" + currentStock +
                ", income=" + income +
                ", processedBills=" + processedBills +
                '}';
    }
}

