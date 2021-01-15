package Repositories;
import Models.Bill;
import java.util.List;
import java.util.Random;

public class MyRunnable implements Runnable {

    private static final Random random = new Random();
    private Inventory inventory;
    private List<Bill> billList;

    public MyRunnable(Inventory inventory, List<Bill> billList) {
        this.inventory = inventory;
        this.billList = billList;
    }

    @Override
    public void run() {
        try {
            billList.forEach(bill -> inventory.processBill(bill));

            if(random.ints(200, 800).limit(1).sum() < 500) {
                inventory.checkInventory();
            }
        }
        catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}