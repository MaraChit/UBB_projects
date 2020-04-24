package Model.Stm;

import Exceptions.MyException;
import Model.Expr.Exp;
import Model.PrgState.MyIDictionary;
import Model.PrgState.MyIFileTable;
import Model.PrgState.MyIHeap;
import Model.PrgState.PrgState;
import Model.Type.IntType;
import Model.Type.StringType;
import Model.Type.Type;
import Model.Values.IntValue;
import Model.Values.StringValue;
import Model.Values.Value;

import java.io.BufferedReader;
import java.io.IOException;

public class readRFile implements IStmt {

    Exp exp;
    String var_name;

    public readRFile(Exp e, String s){
        exp=e;
        var_name=s;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTable = state.getSymTable();
        if(symTable.isDefined(var_name)) {
            MyIFileTable fileTable = state.getFileTable();
            MyIHeap heap = state.getHeap();
            Value v = exp.eval(symTable,heap);
            if (v.getType().equals(new StringType())) {
                BufferedReader fd = fileTable.get((StringValue) v);

                if (fd == null)
                    throw new MyException("invalid fd");
                try {
                    String read = fd.readLine();
                    IntValue nr;
                    if (read == null)
                        nr = new IntValue(0);
                    else
                        nr = new IntValue(Integer.parseInt(read));
                    symTable.update(var_name,nr);
                } catch (IOException e) {
                    throw new MyException("invalid reading");
                }

            } else throw new MyException("invalid filename");
        }
        else
            throw new MyException("invalid var name");
        return null;

    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typeVar = typeEnv.lookup(var_name);
        Type typeExp = exp.typecheck(typeEnv);
        if(!typeVar.equals(new IntType()))
            throw new MyException("Variable not of type int");
        if(typeExp.equals(new StringType()))
            return typeEnv;
        else throw new MyException("ReadFile: not a string");
    }

    @Override
    public String toString() {
        return "readFile("+exp.toString()+")";
    }
}
