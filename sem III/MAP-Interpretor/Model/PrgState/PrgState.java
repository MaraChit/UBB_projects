package Model.PrgState;

import Exceptions.MyException;
import Model.Stm.IStmt;
import Model.Values.StringValue;
import Model.Values.Value;

import java.io.BufferedReader;

public class PrgState{
    MyIStack<IStmt> exeStack;
    MyIDictionary<String, Value> symTable;
    MyIList<Value> out;
    MyIFileTable fileTable;
    MyIHeap heap;
    IStmt originalProgram;
    static int id = 1;
    int prgId;


    public PrgState(MyIStack<IStmt> stk, MyIDictionary<String, Value> symtbl, MyIList<Value> ot, IStmt prg, MyIFileTable ftbl, MyIHeap hp){
        exeStack=stk;
        symTable=symtbl;
        out = ot;
        fileTable=ftbl;
        heap=hp;
        prgId=id;
        //originalProgram=deepCopy(prg);//recreate the entire original prg
        stk.push(prg);
    }

    public MyIList<Value> getOut() {
        return out;
    }

    public MyIDictionary<String, Value> getSymTable() {
        return symTable;
    }

    public MyIStack<IStmt> getStk() {
        return exeStack;
    }

    public MyIFileTable<StringValue, BufferedReader> getFileTable() {return fileTable;}

    @Override
    public String toString() {
        return "ID: "+String.valueOf(prgId)+"\ne: " + exeStack.toString() +"\ns: "+symTable.toString()+"\no: "+out.toString()+ "\nh:"+heap.toString();
    }

    public MyIHeap getHeap()
    {
        return heap;
    }

    public void setHeap(MyIHeap h)
    {
        heap = h;
    }

    public boolean isNotCompleted()
    {
        if (exeStack.isEmpty())
            return false;

        return true;
    }

    public PrgState oneStep() throws MyException
    {
        if(exeStack.isEmpty())
            throw new MyException("exe stack is empty!");
        IStmt currentStmt = exeStack.pop();
        return currentStmt.execute(this);
    }

    public static synchronized void setId()
    {

        id++;
    }

    public PrgState get() {

        return this;
    }

    public int getPrgId() {
        return prgId;
    }

    public MyIDictionary<String, Value> cloneSymTbl() throws MyException {
        MyIDictionary<String, Value> symTblClone = new MyDictionary<>();
        for(String key : symTable.getContent().keySet())
        {
            symTblClone.update(key, symTable.lookup(key));
        }
        return symTblClone;
    }
}

