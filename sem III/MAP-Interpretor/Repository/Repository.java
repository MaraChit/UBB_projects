package Repository;

import Exceptions.MyException;
import Model.PrgState.PrgState;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Repository implements IRepository {
    int index;
    List<PrgState> lista;
    String logFilePath;


    public Repository(String lgfilePath)
    {
        lista = new ArrayList<>();
        logFilePath = lgfilePath;
    }

    public void setIndex(int index) {
        this.index = index;
    }

    public int getIndex() {
        return index;
    }

    /*@Override

    public PrgState getCrtPrg() {
        return lista.get(0);
    }*/

    @Override
    public void add(PrgState prg) {
        this.lista.add(prg);
    }


    @Override
    public void logPrgStateExec(PrgState state) throws MyException {
        try {
            PrintWriter logFile = new PrintWriter(
                    new BufferedWriter(new FileWriter(logFilePath, true)));
            logFile.append(state.toString());
            logFile.close();
        }
        catch (IOException e)
        {
            throw new MyException("file doesn't exist!");
        }
    }

    @Override
    public List<PrgState> getPrgList() {
        return lista;
    }

    @Override
    public void setPrgList(List<PrgState> listState) {

        lista = listState;

    }
}
