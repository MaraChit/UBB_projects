import Repositories.Inventory;
import Repositories.MainLockInventory;
import Repositories.ProductLockInventory;
import Services.Service;

public class Main {
    public static void main(String[] args) {
        Inventory inventory = new MainLockInventory();
        //Inventory inventory = new ProductLockInventory();

        Service service = new Service(inventory);

        System.out.println(service.runOperations(10, 10000, 100000, 12));


        String arch = System.getProperty("os.arch");
        int availableThreads = Runtime.getRuntime().availableProcessors();

        System.out.println("Architecture: " + arch);
        System.out.println("Available threads: " + availableThreads + "\n");
    }
}
