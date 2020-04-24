package Model.Stm;

import Exceptions.MyException;
import Model.Expr.ArithExp;
import Model.Expr.Exp;
import Model.Expr.ValueExp;
import Model.PrgState.MyIDictionary;
import Model.PrgState.PrgState;
import Model.Type.Type;
import Model.Values.IntValue;

public class WaitStmt implements IStmt {
    Exp number;

    public WaitStmt(Exp number) {
        this.number = number;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        if(!(number.eval(state.getSymTable(),state.getHeap()).equals(new IntValue(0)))){
            IStmt st = new CompStmt(new PrintStmt(number),new WaitStmt(new ArithExp('-',number,new ValueExp(new IntValue(1)))));
            state.getStk().push(st);
        }
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return typeEnv;
    }
    @Override
    public String toString(){
        return "wait("+ String.valueOf(number)+")";

    }
}
