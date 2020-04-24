package Model.Expr;

import Exceptions.MyException;
import Model.PrgState.MyIDictionary;
import Model.PrgState.MyIHeap;
import Model.Type.RefType;
import Model.Type.Type;
import Model.Values.RefValue;
import Model.Values.Value;

public class rH implements Exp {
    Exp exp;
    public rH(Exp e)
    {
        exp = e;
    }
    @Override
    public String toString() {
        return "rH("+exp.toString()+")";
    }

    @Override
    public Value eval(MyIDictionary<String, Value> tbl, MyIHeap hp) throws MyException {
        Value v = exp.eval(tbl,hp);
        if(v instanceof RefValue)

        {
            RefValue rv = (RefValue) v;
            int addr = rv.getAddr();
            if(hp.isKey(addr))
            {
                return hp.getValue(addr);
            }
            else {throw new MyException("Invalid address");}
        }
        else throw new MyException("not a ref value");
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typ=exp.typecheck(typeEnv);
        if (typ instanceof RefType) {
            RefType reft =(RefType) typ;
            return reft.getInner();
        } else
            throw new MyException("the rH argument is not a Ref Type");
    }
}
