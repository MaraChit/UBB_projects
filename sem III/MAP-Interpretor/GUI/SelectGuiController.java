package GUI;

import Controller.Controller;
import Exceptions.MyException;
import Model.Expr.*;
import Model.PrgState.*;
import Model.Stm.*;
import Model.Type.*;
import Model.Values.BoolValue;
import Model.Values.IntValue;
import Model.Values.StringValue;
import Model.Values.Value;
import Repository.IRepository;
import Repository.Repository;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;

import java.lang.reflect.AnnotatedTypeVariable;
import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.ResourceBundle;
import java.util.stream.Collectors;

public class SelectGuiController implements Initializable {
    @FXML
    private ListView<String> programList;
    @FXML
    private Button executeButton;

    private ExecGuiController execController;

    private List<IStmt> statementList;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        try {
            addStatements();
        } catch (MyException e) {
            System.out.println(e.getMessage());
        }

        programList.setItems(FXCollections.observableList(transformIntoString()));

        executeButton.setOnAction(actionEvent -> {
            int index = programList.getSelectionModel().getSelectedIndex();

            if (index < 0)
            {
                Alert alert = new Alert(Alert.AlertType.WARNING);
                alert.setTitle("Warning message");
                alert.setHeaderText("No program selected");
                alert.showAndWait();
            }
            else{
                execController.useController(generateController(index));
            }
        });
    }

    private void addStatements() throws MyException {
        statementList = new ArrayList<IStmt>();

        IStmt ex1 = new CompStmt(new VarDeclStmt("v", new IntType()),
                new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(2))), new PrintStmt(new VarExp("v"))));

        ex1.typecheck(new MyDictionary<String, Type>());
        statementList.add(ex1);

        IStmt ex2 = new CompStmt(new VarDeclStmt("a", new IntType()),
                new CompStmt(new VarDeclStmt("b", new IntType()),
                        new CompStmt(new AssignStmt("a", new ArithExp('+', new ValueExp(new IntValue(2)), new
                                ArithExp('*', new ValueExp(new IntValue(3)), new ValueExp(new IntValue(5))))),
                                new CompStmt(new AssignStmt("b", new ArithExp('+', new VarExp("a"), new
                                        ValueExp(new IntValue(1)))), new PrintStmt(new VarExp("b"))))));

        ex2.typecheck(new MyDictionary<String, Type>());
        statementList.add(ex2);

        IStmt ex3 = new CompStmt(new VarDeclStmt("a", new BoolType()), new CompStmt(new VarDeclStmt("v", new IntType()),
                new CompStmt(new AssignStmt("a", new ValueExp(new BoolValue(true))), new CompStmt(new IfStmt(new VarExp("a"),
                        new AssignStmt("v", new ValueExp(new IntValue(2))), new AssignStmt("v", new ValueExp(new IntValue(3)))),
                        new PrintStmt(new VarExp("v"))))));

        ex3.typecheck(new MyDictionary<String, Type>());
        statementList.add(ex3);

        IStmt ex4 = new IfStmt(new RelExp(new ValueExp(new IntValue(40)), new ValueExp(new IntValue(30)),
                "=="),new PrintStmt(new ValueExp(new StringValue("ana"))),
                new PrintStmt(new ValueExp(new StringValue("ion"))));

        ex4.typecheck(new MyDictionary<String, Type>());
        statementList.add(ex4);

        IStmt ex5 = new CompStmt(new VarDeclStmt("varf", new StringType()),
                new CompStmt(new AssignStmt("varf", new ValueExp(new StringValue("test.in"))),
                        new CompStmt(new openRFile(new VarExp("varf")),
                                new CompStmt(new VarDeclStmt("varc", new IntType()),
                                        new CompStmt(new readRFile(new VarExp("varf"), "varc"),
                                                new CompStmt(new PrintStmt(new VarExp("varc")),
                                                        new CompStmt(new readRFile(new VarExp("varf"), "varc"),
                                                                new CompStmt(new PrintStmt(new VarExp("varc")),
                                                                        new closeRFile(new VarExp("varf"))))))))));
        ex5.typecheck(new MyDictionary<String, Type>());
        statementList.add(ex5);

        IStmt ex6 = new CompStmt(new VarDeclStmt("v", new RefType(new IntType())),
                new CompStmt(new newH("v", new ValueExp(new IntValue(20))),
                        new CompStmt(new VarDeclStmt("a", new RefType(new RefType(new IntType()))),
                                new CompStmt(new newH("a", new VarExp("v")),
                                        new CompStmt(new PrintStmt(new VarExp("v")),new PrintStmt(new VarExp("a")))))));

        ex6.typecheck(new MyDictionary<String, Type>());
        statementList.add(ex6);

        IStmt ex7 = new CompStmt(new VarDeclStmt("v", new RefType(new IntType())),
                new CompStmt(new newH("v", new ValueExp(new IntValue(20))),
                        new CompStmt(new VarDeclStmt("a", new RefType(new RefType(new IntType()))),
                                new CompStmt(new newH("a", new VarExp("v")),
                                        new CompStmt(new PrintStmt(new rH(new VarExp("v"))),
                                                new PrintStmt(new ArithExp('+',new rH(new rH(new VarExp("a"))),new ValueExp(new IntValue(5)))))))));

        ex7.typecheck(new MyDictionary<String, Type>());
        statementList.add(ex7);

        IStmt ex8 = new CompStmt(new VarDeclStmt("v", new RefType(new IntType())),
                new CompStmt(new newH("v", new ValueExp(new IntValue(20))),
                        new CompStmt(new PrintStmt(new rH(new VarExp("v"))),
                                new CompStmt(new wH("v", new ValueExp(new IntValue(30))),
                                        new PrintStmt(new ArithExp('+', new rH(new VarExp("v")),new ValueExp(new IntValue(5))))))));

        ex8.typecheck(new MyDictionary<String, Type>());
        statementList.add(ex8);

        IStmt ex9 = new CompStmt(new VarDeclStmt("v",new RefType(new IntType())),
                new CompStmt(new newH("v", new ValueExp(new IntValue(20))),
                        new CompStmt(new VarDeclStmt("a", new RefType(new RefType(new IntType()))),
                                new CompStmt(new newH("a",new VarExp("v")),
                                        new CompStmt(new newH("v", new ValueExp(new IntValue(30))),
                                                new PrintStmt(new rH(new rH(new VarExp("a")))))))));

        ex9.typecheck(new MyDictionary<String, Type>());
        statementList.add(ex9);

        IStmt ex10 = new CompStmt(new VarDeclStmt("v", new IntType()),
                new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(4))),
                        new CompStmt(new WhileStmt(new RelExp(new VarExp("v"),new ValueExp(new IntValue(0)),">"),
                                new CompStmt(new PrintStmt(new VarExp("v")), new AssignStmt("v",new ArithExp('-', new VarExp("v"), new ValueExp(new IntValue(1)))))),
                                new PrintStmt(new VarExp("v")))));

        ex10.typecheck(new MyDictionary<String, Type>());
        statementList.add(ex10);

        IStmt inFork=new CompStmt(new wH("a",new ValueExp(new IntValue(30))),
                new CompStmt(new AssignStmt("v",new ValueExp(new IntValue(32))),
                        new CompStmt(new PrintStmt(new VarExp("v")), new PrintStmt(new rH(new VarExp("a"))))));

        IStmt ex11 = new CompStmt(new VarDeclStmt("v",new IntType()),
                new CompStmt(new VarDeclStmt("a", new RefType(new IntType())),
                        new CompStmt(new AssignStmt("v",new ValueExp(new IntValue(10))),
                                new CompStmt(new newH("a",new ValueExp(new IntValue(22))),
                                        new CompStmt(new forkStmt(inFork),
                                                new CompStmt(new PrintStmt(new VarExp("v")), new PrintStmt(new rH(new VarExp("a")))))))));

        ex11.typecheck(new MyDictionary<String, Type>());
        statementList.add(ex11);

        //Wrong type check
        //bool a;a=13;
        IStmt ex12 = new CompStmt(new VarDeclStmt("a", new BoolType()), new AssignStmt("a", new ValueExp(new IntValue(13))));
        try{
            ex12.typecheck(new MyDictionary<String, Type>());

        }catch (MyException e)
        {
            System.out.println(e.getMessage());
        }


        //Wrong type check
        //Ref Int a; new(a,'ana')
        IStmt ex13 = new CompStmt(new VarDeclStmt("a", new RefType(new IntType())), new newH("a", new ValueExp(new StringValue("ana"))));
        try{
            ex13.typecheck(new MyDictionary<String, Type>());

        }catch (MyException e)
        {
            System.out.println(e.getMessage());
        }

        /*IStmt ex14 = new CompStmt(new VarDeclStmt("a", new IntType()),new CompStmt(
                new VarDeclStmt("b", new IntType()), new CompStmt(new VarDeclStmt("c", new IntType()),
                new CompStmt(new AssignStmt("a", new ValueExp(new IntValue(1))),
                        new CompStmt(new AssignStmt("b", new ValueExp(new IntValue(2))),
                                new CompStmt(new AssignStmt("c", new ValueExp(new IntValue(5))),
                                        new CompStmt(new SwitchStmt(new ArithExp('*', new VarExp("a"), new ValueExp(new IntValue(10))),
                                                new ArithExp('*', new VarExp("b"), new VarExp("c")),
                                                new ValueExp(new IntValue(10)),
                                                new CompStmt(new PrintStmt(new VarExp("a")), new PrintStmt(new VarExp("b"))),
                                                new CompStmt(new PrintStmt(new ValueExp(new IntValue(100))), new PrintStmt(new ValueExp(new IntValue(200)))),
                                                new PrintStmt(new ValueExp(new IntValue(300)))), new PrintStmt(new ValueExp(new IntValue(300))))))))));
        statementList.add(ex14);

        IStmt ex15 = new CompStmt(new VarDeclStmt("v",new IntType()),new CompStmt(new AssignStmt("v",new ValueExp(new IntValue(20))),
                new CompStmt(new WaitStmt(new ValueExp(new IntValue(10))),new PrintStmt(new ArithExp('*',new VarExp("v"),new ValueExp(new IntValue(10)))))));
        statementList.add(ex15);

        IStmt ex16 = new CompStmt(new VarDeclStmt("v",new IntType()),new CompStmt(new AssignStmt("v",new ValueExp( new IntValue(20))),
                new CompStmt(new ForStmt(new ValueExp(new IntValue(0)), new ValueExp(new IntValue(3)), new ArithExp('+', new VarExp("v"),new ValueExp(new IntValue(1))),
                        new forkStmt(new CompStmt(new PrintStmt(new VarExp("v")), new AssignStmt("v", new ValueExp(new IntValue(1)))))),
                        new PrintStmt(new ArithExp('*', new ValueExp(new IntValue(10)), new VarExp("v"))))));
        statementList.add(ex16);

        IStmt ex16 = new CompStmt(new VarDeclStmt("b",new BoolType()), new CompStmt(new VarDeclStmt("c", new IntType()),
                new CompStmt(new AssignStmt("b", new ValueExp(new BoolValue(true))),new CompStmt(new CondStmt(new VarExp("b"),new ValueExp(new IntValue(100)),
                        new ValueExp(new IntValue(200)),"c"),new CompStmt(new PrintStmt(new VarExp("c")),
                        new CompStmt(new CondStmt(new ValueExp(new BoolValue(false)),new ValueExp(new IntValue(100)), new ValueExp(new IntValue(200)),
                                "c"),new PrintStmt(new VarExp("c"))))))));*/


        IStmt ex15 = new CompStmt(new VarDeclStmt("a", new RefType(new IntType())),
                new CompStmt(new VarDeclStmt("b", new RefType(new IntType())),
                        new CompStmt(new VarDeclStmt("v",new IntType()),
                                new CompStmt(new newH("a",new ValueExp(new IntValue(0))),
                                        new CompStmt(new newH("b",new ValueExp(new IntValue(0))),
                                                new CompStmt(new wH("a",new ValueExp(new IntValue(1))),
                                                        new CompStmt(new wH("b",new ValueExp(new IntValue(2))),
                                                                new CompStmt(new CondStmt(new RelExp(new rH(new VarExp("a")), new rH(new VarExp("b")),"<"),new ValueExp(new IntValue(100)),new ValueExp(new IntValue(200)),"v"),
                                                                        new CompStmt(new PrintStmt(new VarExp("v")),
                                                                                new CompStmt(new CondStmt(new RelExp(new ArithExp('-',new rH(new VarExp("b")), new ValueExp(new IntValue(2))),new rH(new VarExp("a")),">"),new ValueExp(new IntValue(100)),new ValueExp(new IntValue(200)),"v"), new PrintStmt(new VarExp("v"))))))))))));

        statementList.add(ex15);




    }

    private List<String> transformIntoString(){
        return statementList.stream().map(IStmt::toString).collect(Collectors.toList());
    }

    public void setExecController(ExecGuiController c){
        execController = c;
    }

    private Controller generateController(int index)
    {
        MyIStack<IStmt> stk = new MyStack<IStmt>();
        MyIDictionary<String, Value> dict = new MyDictionary<String, Value>();
        MyIList<Value> list = new MyList<Value>();
        MyIFileTable fileTable = new MyFileTable();
        MyIHeap hp = new MyHeap();
        PrgState prg = new PrgState(stk, dict, list,statementList.get(index), fileTable,hp);
        IRepository repository = new Repository("repo.txt");
        repository.add(prg);

        return new Controller(repository);
    }


}
