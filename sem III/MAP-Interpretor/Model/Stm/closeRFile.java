package Model.Stm;

import Exceptions.MyException;
import Model.Expr.Exp;
import Model.PrgState.MyIDictionary;
import Model.PrgState.MyIFileTable;
import Model.PrgState.MyIHeap;
import Model.PrgState.PrgState;
import Model.Type.StringType;
import Model.Type.Type;
import Model.Values.StringValue;
import Model.Values.Value;

import java.io.BufferedReader;
import java.io.IOException;

public class closeRFile implements IStmt {
    Exp exp;

    public closeRFile (Exp e) {
        exp = e;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTable = state.getSymTable();
        MyIFileTable fileTable = state.getFileTable();
        MyIHeap heap = state.getHeap();
        Value v = exp.eval(symTable,heap);
        if(v.getType().equals(new StringType()))
        {
            if(fileTable.isDefined((StringValue) v))
            {
                BufferedReader fd = fileTable.get((StringValue)v);
                try {
                    fd.close();
                    fileTable.delete((StringValue) v);
                }
                catch (IOException e)
                {
                    throw new MyException("invalid close!");
                }

            }
            else throw new MyException("invalid filename");

        }
        else throw new MyException("invalid filename");
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        if(exp.typecheck(typeEnv).equals(new StringType()))
            return typeEnv;
        else throw new MyException("wrong type of argument");
    }

    @Override
    public String toString() {
        return "closeRFile("+exp.toString()+")";
    }
}

