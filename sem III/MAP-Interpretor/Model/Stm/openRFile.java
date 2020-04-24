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
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.Reader;

public class openRFile implements IStmt {

    Exp exp;

    public openRFile(Exp e)
    {

        exp = e;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTable = state.getSymTable();
        MyIFileTable<StringValue, BufferedReader> fileTable = state.getFileTable();
        MyIHeap heap = state.getHeap();
        Value v = exp.eval(symTable,heap);
        if(v.getType().equals(new StringType()))
        {
            StringValue name = (StringValue) v;
            if(!fileTable.isDefined(name))
            {
                try {
                    BufferedReader fd = new BufferedReader(new FileReader((String) name.getVal()));
                    fileTable.add(name, fd);
                }
                catch (FileNotFoundException e){
                    throw new MyException("file not found!");
                }
            }
            else throw new MyException("name already defined!");
        }
        else throw new MyException("invalid filename!");
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        if(exp.typecheck(typeEnv).equals(new StringType()))
            return typeEnv;
        else
            throw new MyException("Open file: not a string");
    }

    @Override
    public String toString() {
        return "openRFile("+exp.toString()+")";
    }
}
