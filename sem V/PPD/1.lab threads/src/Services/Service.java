package Services;

import Models.Bill;
import Models.Product;
import Repositories.Inventory;
import Repositories.MyRunnable;

import java.util.AbstractMap;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class Service {
    private Inventory inventory;
    private List<Product> productList;

    public Service(Inventory inventory) {
        this.inventory = inventory;
        this.productList = new ArrayList<>();
    }

    private List<AbstractMap.SimpleEntry<Product, Integer>> generateProductList(int numberOfProducts, int initialQuantity) {

        List<AbstractMap.SimpleEntry<Product, Integer>> productList = new ArrayList<>();
        this.productList = new ArrayList<>();

        for (int index = 0; index < numberOfProducts; index++) {
            //generate random name and price
            String productName = Generator.generateRandomString();
            int productPrice = Generator.generateRandomInt(5, 100);

            Product product = new Product(productName, productPrice);
            productList.add(new AbstractMap.SimpleEntry<>(product, initialQuantity));
            this.productList.add(product);
        }

        return productList;  //prod+ initial quantity
    }

    private List<Bill> generateBillList(int numberOfProducts, int numberOfBills) {
        List<Bill> billList = new ArrayList<>();

        for (int index = 0; index < numberOfBills; index++){

            //generate random bill with random products from the list
            Collections.shuffle(this.productList);
            List<Product> products = this.productList.subList(0, numberOfProducts);

            //for each product, generate quantity
            List<AbstractMap.SimpleEntry<Product, Integer>> billProducts = products.stream()
                    .map(product -> new AbstractMap.SimpleEntry<>(product, Generator.generateRandomInt(5, 15)))
                    .collect(Collectors.toList());

            Bill bill = new Bill(billProducts);
            billList.add(bill);
        }

        return billList;

    }

    public double runOperations(int numberOfTests, int numberOfProducts, int initialQuantity, int threadCount){

        List<Thread> threads = new ArrayList<>();
        List<Long> runTimes = new ArrayList<>();

        for(int index = 0; index < numberOfTests; index++){
            //generate different a productList for each test
            inventory.resetStock(generateProductList(numberOfProducts, initialQuantity));

            for(int i = 0; i < threadCount; i++){
                //generate a different billList for each thread
                List<Bill> billList = generateBillList(100, 100);
                MyRunnable operationRunnable = new MyRunnable(inventory, billList);

                Thread thread = new Thread(operationRunnable);

                threads.add(thread);
                thread.start();
            }

            Long startTime = System.currentTimeMillis();


            for(Thread thread: threads){
                try {
                    thread.join();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            inventory.checkInventory();

            Long endTime = System.currentTimeMillis();

            Long runTime = (endTime - startTime);
            runTimes.add(runTime);
        }
        double average = runTimes.stream().reduce((long) 0.0, Long::sum) / (double) numberOfTests;
        return average;
    }
}
