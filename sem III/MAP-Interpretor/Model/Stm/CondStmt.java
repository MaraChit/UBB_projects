package Model.Stm;

import Exceptions.MyException;
import Model.Expr.Exp;
import Model.PrgState.MyIDictionary;
import Model.PrgState.PrgState;
import Model.Type.BoolType;
import Model.Type.Type;

public class CondStmt implements IStmt {

    Exp exp1,exp2,exp3;
    String var_name;

    public CondStmt(Exp exp1, Exp exp2, Exp exp3, String var_name) {
        this.exp1 = exp1;
        this.exp2 = exp2;
        this.exp3 = exp3;
        this.var_name = var_name;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {

        IStmt st = new IfStmt(exp1,new AssignStmt(var_name,exp2),new AssignStmt(var_name,exp3));
        state.getStk().push(st);
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {

        Type typexp1=exp1.typecheck(typeEnv);
        Type tyexp2=exp2.typecheck(typeEnv);
        Type tyxp3=exp3.typecheck(typeEnv);
        if (typexp1.equals(new BoolType())) {
            if(tyexp2.equals(tyxp3) && tyexp2.equals(var_name))
                return typeEnv;
            else throw new MyException("Exp2, exp 3 and variable don't have the same type");
        }
        else
            throw new MyException("The condition has not the type bool");
        //return typeEnv;
    }

    @Override
    public String toString(){
        return var_name+"="+exp1.toString()+"?"+exp2.toString()+":"+exp3.toString();
    }
}
