package Model.Stm;

import Exceptions.MyException;
import Model.Expr.Exp;
import Model.PrgState.MyIDictionary;
import Model.PrgState.MyIHeap;
import Model.PrgState.PrgState;
import Model.Type.BoolType;
import Model.Type.Type;
import Model.Values.BoolValue;
import Model.Values.Value;

public class WhileStmt implements IStmt {

    Exp exp;
    IStmt st;
    public WhileStmt(Exp e, IStmt s)
    {
        exp = e;
        st = s;
    }
    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTbl = state.getSymTable();
        MyIHeap heap = state.getHeap();
        Value v = exp.eval(symTbl, heap);
        if(v.getType().equals(new BoolType()))
        {
            BoolValue bv = (BoolValue) v;
            if(bv.getVal() == true)
            {
                state.getStk().push(new WhileStmt(exp, st));
                state.getStk().push(st);
            }
            return null;
        }
        else throw new MyException("invalid type");
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typeExp = exp.typecheck(typeEnv);
        if(typeExp instanceof BoolType)
        {
            st.typecheck(typeEnv.clone());
            return typeEnv;
        }
        else throw new MyException("While condition not a bool expression");
    }

    @Override
    public String toString() {
        return "while("+exp.toString()+")("+st.toString()+")";
    }
}