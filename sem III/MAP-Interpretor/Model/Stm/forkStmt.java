package Model.Stm;

import Exceptions.MyException;
import Model.PrgState.MyIDictionary;
import Model.PrgState.MyStack;
import Model.PrgState.PrgState;
import Model.Type.Type;

public class forkStmt implements IStmt {

    IStmt stmt;

    public forkStmt(IStmt st)
    {
        stmt = st;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        PrgState.setId();
        PrgState newState = new PrgState(new MyStack<IStmt>(), state.cloneSymTbl(), state.getOut(), stmt, state.getFileTable(), state.getHeap());
        return newState;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        stmt.typecheck(typeEnv.clone());
        return typeEnv;
    }

    @Override
    public String toString() {
        return "fork("+stmt.toString()+")";
    }
}
