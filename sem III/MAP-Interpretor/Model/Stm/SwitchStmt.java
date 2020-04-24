package Model.Stm;

import Exceptions.MyException;
import Model.Expr.Exp;
import Model.Expr.RelExp;
import Model.PrgState.MyIDictionary;
import Model.PrgState.PrgState;
import Model.Type.Type;

public class SwitchStmt implements IStmt {
    Exp exp, exp1, exp2;
    IStmt stmt1, stmt2, stmt3;

    public SwitchStmt(Exp exp, Exp exp1, Exp exp2, IStmt stmt1, IStmt stmt2, IStmt stmt3) {
        this.exp = exp;
        this.exp1 = exp1;
        this.exp2 = exp2;
        this.stmt1 = stmt1;
        this.stmt2 = stmt2;
        this.stmt3 = stmt3;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        IStmt st = new IfStmt(new RelExp(exp, exp1,"=="), stmt1, new IfStmt(new RelExp(exp,exp2,"=="), stmt2, stmt3));
        state.getStk().push(st);
        return null;
    }

    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        if(exp.typecheck(typeEnv).equals(exp1.typecheck(typeEnv)) && exp.typecheck(typeEnv).equals(exp2.typecheck(typeEnv)))
        {
            stmt1.typecheck(typeEnv.clone());
            stmt2.typecheck(typeEnv.clone());
            stmt3.typecheck(typeEnv.clone());
            return typeEnv;
        }
        else
            throw new MyException("Different types for expressions!");
    }

    @Override
    public String toString() {
        return "Switch("+exp.toString()+")(case "+exp1.toString()+": "+stmt1.toString()+
                ")(case "+exp2.toString()+": "+stmt2.toString()+"(default: "+stmt3.toString()+")";
    }
}
