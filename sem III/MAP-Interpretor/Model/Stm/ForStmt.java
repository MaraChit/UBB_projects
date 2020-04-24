package Model.Stm;

import Exceptions.MyException;
import Model.Expr.Exp;
import Model.Expr.RelExp;
import Model.Expr.VarExp;
import Model.PrgState.MyIDictionary;
import Model.PrgState.PrgState;
import Model.Type.Type;
import Model.Values.IntValue;

public class ForStmt implements IStmt {
    Exp e1,e2,e3;
    IStmt stm1;

    public ForStmt(Exp e1, Exp e2, Exp e3, IStmt stm1) {
        this.e1 = e1;
        this.e2 = e2;
        this.e3 = e3;
        this.stm1 = stm1;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {

        IStmt st =  new CompStmt(new AssignStmt("v",e1),new WhileStmt(new RelExp(new VarExp("v"),e2,"<"),new CompStmt(stm1,new AssignStmt("v",e3))));
        state.getStk().push(st);
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return typeEnv;
    }


    @Override
    public String toString() {
        return "for(v=" + e1.toString() +",v<" + e2.toString() +",v="+e3.toString() + " )"+ stm1.toString() ;
    }
}
