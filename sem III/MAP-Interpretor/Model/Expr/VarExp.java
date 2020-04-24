package Model.Expr;

import Exceptions.MyException;
import Model.PrgState.MyIDictionary;
import Model.PrgState.MyIHeap;
import Model.Type.Type;
import Model.Values.Value;

public class VarExp implements Exp {
    String id;

    public VarExp(String v) {
        this.id = v;
    }

    public Value eval(MyIDictionary<String,Value> tbl, MyIHeap hp) throws MyException
    {
        return tbl.lookup(id);
    }

    @Override
    public Type typecheck(MyIDictionary<String,Type> typeEnv) throws MyException{
        return typeEnv.lookup(id);
    }

    @Override
    public String toString() {
        return id;
    }
}

