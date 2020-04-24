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

public class IfStmt implements IStmt {
    Exp exp;
    IStmt thenS;
    IStmt elseS;

    public IfStmt(Exp e, IStmt t, IStmt el) {exp=e; thenS=t;elseS=el;}

    public String toString(){ return "IF("+ exp.toString()+") THEN(" +thenS.toString()
            +")ELSE("+elseS.toString()+")";}

    public PrgState execute(PrgState state) throws MyException {

        MyIDictionary<String, Value> symTbl = state.getSymTable();
        MyIHeap heap = state.getHeap();
        Value x = exp.eval(symTbl, heap);
        if (x.getType().equals(new BoolType()))
        {
            BoolValue n = (BoolValue)x;
            if(n.getVal())
                state.getStk().push(thenS);
            else
                state.getStk().push(elseS);
        }
        else{
            throw new MyException("Exp is not booltype");
        }
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
            Type typexp=exp.typecheck(typeEnv);
            if (typexp.equals(new BoolType())) {
                thenS.typecheck(typeEnv.clone());
                elseS.typecheck(typeEnv.clone());
                return typeEnv;
            }
            else
                throw new MyException("The condition of IF has not the type bool");
    }
}
