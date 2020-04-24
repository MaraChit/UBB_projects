package Model.Stm;

import Exceptions.MyException;
import Model.PrgState.MyIDictionary;
import Model.PrgState.PrgState;
import Model.Type.IntType;
import Model.Type.Type;
import Model.Values.BoolValue;
import Model.Values.IntValue;

public class VarDeclStmt implements IStmt{
    String name;
    Type typ;

    public VarDeclStmt(String a, Type type) {
        this.name=a;
        this.typ = type ;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {

        if(!state.getSymTable().isDefined(name)){
            state.getSymTable().update(name,typ.defaultValue());

        }

        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        typeEnv.update(name,typ);
        return typeEnv;
    }

    @Override
    public String toString() {
        return typ.toString()+" "+name;
    }
}
