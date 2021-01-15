package Repositories;

import Models.Bill;
import Models.Product;
import java.util.AbstractMap;
import java.util.List;

public interface Inventory {
    void resetStock(List<AbstractMap.SimpleEntry<Product, Integer>> productList);
    void checkInventory();
    void processBill(Bill bill);
}
