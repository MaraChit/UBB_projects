package Model.Stm;

import Exceptions.MyException;
import Model.PrgState.MyIDictionary;
import Model.PrgState.MyIStack;
import Model.PrgState.PrgState;
import Model.Type.Type;

public class CompStmt implements IStmt {
    IStmt first;
    IStmt snd;

    public CompStmt(IStmt v, IStmt v1) {
        this.first = v;
        this.snd= v1;
    }

    public String toString() {
        return "("+first.toString() + ";" + snd.toString()+")";
    }

   public PrgState execute(PrgState state){
        MyIStack<IStmt> stk=state.getStk();
        stk.push(snd);
        stk.push(first);
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
            //MyIDictionary<String,Type> typEnv1 = first.typecheck(typeEnv);
            //MyIDictionary<String,Type> typEnv2 = snd.typecheck(typEnv1);
            //return typEnv2;
            return snd.typecheck(first.typecheck(typeEnv));
        }
}


