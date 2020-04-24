package Model.Expr;

import Exceptions.MyException;
import Model.PrgState.MyIDictionary;
import Model.PrgState.MyIHeap;
import Model.Type.BoolType;
import Model.Type.IntType;
import Model.Type.Type;
import Model.Values.BoolValue;
import Model.Values.IntValue;
import Model.Values.Value;

public class ValueExp implements Exp {
    private Value e;

    public ValueExp(Value e) {
        this.e = e;
    }

    public Value eval(MyIDictionary<String, Value> tbl, MyIHeap hp) throws MyException {
        if (e.getType().equals(new IntType())) {
            return (IntValue)e;}

        if(e.getType().equals(new BoolType())) {
            return (BoolValue) e; }
        return e;

    }

    @Override
    public Type typecheck(MyIDictionary<String,Type> typeEnv) throws MyException{
        return e.getType();
    }

    @Override
    public String toString() {
        return e.toString();
    }
}
