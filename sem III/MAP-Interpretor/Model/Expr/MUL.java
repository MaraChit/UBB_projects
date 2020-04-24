package Model.Expr;

import Exceptions.MyException;
import Model.PrgState.MyIDictionary;
import Model.PrgState.MyIHeap;
import Model.Type.IntType;
import Model.Type.Type;
import Model.Values.IntValue;
import Model.Values.Value;

public class MUL implements Exp {
    Exp exp1,exp2;

    public MUL(Exp exp1, Exp exp2) {
        this.exp1 = exp1;
        this.exp2 = exp2;
    }

    @Override
    public Value eval(MyIDictionary<String, Value> tbl, MyIHeap hp) throws MyException {
        IntValue res =(IntValue)new ArithExp('-', new ArithExp('*',exp1,exp2),new ArithExp('+', exp1, exp2)).eval(tbl,hp);
        return res;
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return new IntType();
    }

    @Override
    public String toString() {
        return "MUL("+exp1.toString()+", "+exp2.toString()+")";
    }
}
