package Model.Stm;

import Exceptions.MyException;
import Model.PrgState.MyIDictionary;
import Model.PrgState.PrgState;
import Model.Type.Type;

public interface IStmt {
        PrgState execute(PrgState state) throws MyException; //which is the execution method for a statement.
        MyIDictionary<String, Type> typecheck(MyIDictionary<String,Type> typeEnv) throws MyException;
}
