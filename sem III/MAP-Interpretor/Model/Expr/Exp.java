package Model.Expr;

import Exceptions.MyException;
import Model.PrgState.MyIDictionary;
import Model.PrgState.MyIHeap;
import Model.Type.Type;
import Model.Values.Value;

public interface Exp {
    Value eval(MyIDictionary<String,Value> tbl, MyIHeap hp) throws MyException;
    Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException;
}
