package Model.Expr;

import Exceptions.MyException;
import Model.PrgState.MyIDictionary;
import Model.PrgState.MyIHeap;
import Model.Type.BoolType;
import Model.Type.Type;
import Model.Values.BoolValue;
import Model.Values.Value;

public class LogicExp implements Exp{
    Exp e1;
    Exp e2;
    int op;

    public LogicExp(Exp e1, Exp e2, int op) {
        this.e1 = e1;
        this.e2 = e2;
        this.op = op;
    }

    public Value eval(MyIDictionary<String, Value> tbl, MyIHeap hp) throws MyException {
        Value v1, v2;
        v1 = e1.eval(tbl,hp);
        if (v1.getType().equals(new BoolType())) {
            v2 = e2.eval(tbl,hp);
            if (v2.getType().equals(new BoolType())) {
                BoolValue i1 = (BoolValue) v1;
                BoolValue i2 = (BoolValue) v2;
                boolean n1, n2;
                n1 = i1.getVal();
                n2 = i2.getVal();
                if (op == 1) return new BoolValue(n1 || n2);
                if (op == 2) return new BoolValue(n1 && n2);
            } else
                throw new MyException("second operand is not a boolean");
        } else
            throw new MyException("first operand is not a boolean");
        return new BoolValue(false);
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type tExp1 = e1.typecheck(typeEnv);
        Type tExp2 = e2.typecheck(typeEnv);
        if (tExp1 instanceof BoolType)
            if (tExp2 instanceof BoolType)
                return new BoolType();
            else throw new MyException("second operand not bool");
        else throw new MyException("first operand not bool");
    }

    @Override
    public String toString() {
        return e1.toString() + String.valueOf(op)+e2.toString();
    }
}

