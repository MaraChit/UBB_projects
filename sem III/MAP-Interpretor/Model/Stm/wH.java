package Model.Stm;

import Exceptions.MyException;
import Model.Expr.Exp;
import Model.PrgState.MyIDictionary;
import Model.PrgState.MyIHeap;
import Model.PrgState.PrgState;
import Model.Type.RefType;
import Model.Type.Type;
import Model.Values.RefValue;
import Model.Values.Value;

public class wH implements IStmt {
    String var_name;
    Exp exp;
    public wH(String v, Exp e)
    {
        var_name = v;
        exp = e;
    }
    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTbl = state.getSymTable();
        MyIHeap heap = state.getHeap();
        if(symTbl.isDefined(var_name))
        {
            Value v = symTbl.lookup(var_name);
            if(v.getType() instanceof  RefType)
            {
                RefValue rv = (RefValue) v;
                if(heap.isKey(rv.getAddr()))
                {
                    Value ev = exp.eval(symTbl, heap);
                    if(ev.getType().equals(((RefType)rv.getType()).getInner()))
                    {
                        heap.update(rv.getAddr(), ev);
                        return null;
                    }
                    else throw new MyException("invalid type");
                }
                else throw new MyException("invalid address");
            }
            else throw new MyException("invalid type");
        }
        else throw new MyException("variable not defined");
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typeVar = typeEnv.lookup(var_name);
        Type typeExp = exp.typecheck(typeEnv);
        if(typeVar.equals(new RefType(typeExp)))
            return typeEnv;
        else
            throw new MyException("Wh stmt: different types");
    }

    @Override
    public String toString() {
        return "wH("+var_name+", "+exp.toString()+")";
    }
}

