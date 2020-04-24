package Model.Stm;

import Exceptions.MyException;
import Model.Expr.Exp;
import Model.Expr.ValueExp;
import Model.PrgState.MyIDictionary;
import Model.PrgState.MyIHeap;
import Model.PrgState.MyIStack;
import Model.PrgState.PrgState;
import Model.Type.Type;
import Model.Values.Value;

public class AssignStmt implements IStmt {
    String id;
    Exp exp;

    public AssignStmt(String v, Exp valueExp) {
        this.id = v;
        this.exp = valueExp;
    }

    public String toString(){
        return id+"="+ exp.toString();
    }

    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stk = state.getStk();
        MyIDictionary<String, Value> symTbl = state.getSymTable();
        MyIHeap heap = state.getHeap();
        Value val = exp.eval(symTbl,heap);
        if (symTbl.isDefined(id)) {
            Type typId = (symTbl.getValue(id)).getType();
            if (val.getType().equals(typId))
                symTbl.update(id, val);
            else
                throw new MyException("declared type of variable" + id + " and type of the assigned expression do not match");

        } else throw new MyException("the used variable" + id + " was not declared before");
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typevar = typeEnv.lookup(id);
        Type typexp = exp.typecheck(typeEnv);
        if (typevar.equals(typexp))
            return typeEnv;
        else
            throw new MyException("Assignment: right hand side and left hand side have different types ");
    }
}
