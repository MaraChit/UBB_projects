package GUI;

import Controller.Controller;
import Exceptions.MyException;
import Model.PrgState.PrgState;
import javafx.beans.property.SimpleStringProperty;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import javafx.util.Pair;

import java.net.URL;
import java.util.List;
import java.util.Objects;
import java.util.ResourceBundle;
import java.util.stream.Collectors;

public class ExecGuiController implements Initializable
{

    @FXML
    private Button oneStepExecButton;
    @FXML
    private TextField noPrgState;
    @FXML
    private TableView<Pair<String,String>> heapTbl;
    @FXML
    private TableColumn<Pair<String, String>, String> hAddress;
    @FXML
    private TableColumn<Pair<String, String>, String> hValue;
    @FXML
    private ListView<String> fileTbl;
    @FXML
    private TableView<Pair<String, String>> symbolTbl;
    @FXML
    private TableColumn<Pair<String, String>, String> symbolTblVariable;
    @FXML
    private TableColumn<Pair<String, String>, String> symbolTblValue;
    @FXML
    private ListView<String> outList;
    @FXML
    private ListView<Integer> prgStateId;
    @FXML
    private ListView<String> exeStack;

    private Controller ctrl;


    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        hAddress.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().getKey()));
        hValue.setCellValueFactory(p->new SimpleStringProperty(p.getValue().getValue()));

        symbolTblVariable.setCellValueFactory(p->new SimpleStringProperty(p.getValue().getKey()));
        symbolTblValue.setCellValueFactory(p->new SimpleStringProperty(p.getValue().getValue()));

        oneStepExecButton.setOnAction(actionEvent -> {
            if(ctrl == null) {
                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setTitle("ERROR");
                alert.setHeaderText("No program selected");
                alert.showAndWait();
            }else{
                executeOneStep();
                updatePrgNo();
                updatePrgId();
                updateFileTbl();
                updateOut();
                updateHeapTbl();

                exeStack.getItems().clear();
                symbolTbl.getItems().clear();

                if (ctrl.getIds().size()==1){
                    updateExeStk(ctrl.getPrgByIndex(0));
                    updateSymTbl(ctrl.getPrgByIndex(0));
                }

            }
        });

        prgStateId.setOnMouseClicked(actionEvent -> {
            PrgState selected = getSelectedPrg();
            if (selected != null) {
                updateExeStk(selected);
                updateSymTbl(selected);
            }else{
             exeStack.getItems().clear();
             symbolTbl.getItems().clear();
            }

        });


    }





    public void useController(Controller generatedController) {

        ctrl = generatedController;
        updatePrgId();
        updatePrgNo();

        if(ctrl.getIds().size()==1)
            updateExeStk(ctrl.getPrgByIndex(0));
        else
            exeStack.getItems().clear();

        symbolTbl.getItems().clear();
        outList.getItems().clear();
        heapTbl.getItems().clear();
        fileTbl.getItems().clear();

    }


    private void updateOut(){ outList.setItems(FXCollections.observableList(ctrl.getOut())); }

    private void updatePrgId(){
        prgStateId.setItems(FXCollections.observableList(ctrl.getIds()));
    }

    private void updatePrgNo(){ noPrgState.setText(String.valueOf(ctrl.getIds().size()));}

    private void updateFileTbl(){fileTbl.setItems(FXCollections.observableList(ctrl.getFileTblAsString()));}

    private void updateHeapTbl()
    {
        List<Pair<String,String>> listH = ctrl.getHeap().getContent().entrySet().stream().map(p -> new Pair<String,String>(Integer.toString(p.getKey()),p.getValue().toString())).collect(Collectors.toList());
        heapTbl.setItems(FXCollections.observableList(listH));
        heapTbl.refresh();
    }

    private void updateExeStk(PrgState selectedPrg){
        exeStack.setItems(FXCollections.observableList(selectedPrg.getStk().getContentStk().stream().map(Objects::toString).collect(Collectors.toList())));
    }

    private void updateSymTbl(PrgState selectedPrg)
    {
        List<Pair<String, String>> symbolTblList= selectedPrg.getSymTable().getContent().entrySet().stream().map(p->new Pair<String,String>(p.getKey(),p.getValue().toString())).collect(Collectors.toList());
        symbolTbl.setItems(FXCollections.observableList(symbolTblList));
    }

    private PrgState getSelectedPrg(){
        int index = prgStateId.getSelectionModel().getSelectedIndex();
        return ctrl.getPrgByIndex(index);
    }


    private void executeOneStep(){
        if(!ctrl.finishExec()) {
            try {
                ctrl.allStepsModifiedToBeOneStep();
            } catch (MyException | InterruptedException e) {
                e.printStackTrace();
            }
        }else
        {
            Alert alert = new Alert(Alert.AlertType.WARNING);
            alert.setTitle("Warning");
            alert.setHeaderText("Execution already finished");
            alert.showAndWait();
        }
    }



}