package Model.Stm;

import Exceptions.MyException;
import Model.Expr.Exp;
import Model.Expr.VarExp;
import Model.PrgState.*;
import Model.Type.Type;
import Model.Values.Value;

public class PrintStmt implements IStmt{
    Exp exp;

    public PrintStmt(Exp v) {
        this.exp = v;
    }

    @Override
    public String toString(){ return "print(" +exp.toString()+")";}
    public PrgState execute(PrgState state) throws MyException {
        MyIList<Value> out = state.getOut();
        MyIDictionary<String,Value> symTable = state.getSymTable();
        MyIHeap heap = state.getHeap();
        out.add(exp.eval(symTable,heap));
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        exp.typecheck(typeEnv);
        return typeEnv;
    }

}
