package GUI;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception{
        FXMLLoader mainLoader = new FXMLLoader();
        mainLoader.setLocation(getClass().getResource("ExecGui.fxml"));
        Parent executionWindow = mainLoader.load();

        ExecGuiController execCtrl = mainLoader.getController();

        primaryStage.setTitle("Program Execution Details");
        primaryStage.setScene(new Scene(executionWindow, 620, 600));
        primaryStage.show();

        FXMLLoader secondaryLoader = new FXMLLoader();
        secondaryLoader.setLocation(getClass().getResource("SelectGui.fxml"));
        Parent selectionWindow = secondaryLoader.load();

        SelectGuiController selectCtrl = secondaryLoader.getController();
        selectCtrl.setExecController(execCtrl);

        Stage secondaryStage = new Stage();
        secondaryStage.setTitle("Program List");
        secondaryStage.setScene(new Scene(selectionWindow, 500, 350));
        secondaryStage.show();


    }


    public static void main(String[] args) {
        launch(args);
    }
}
