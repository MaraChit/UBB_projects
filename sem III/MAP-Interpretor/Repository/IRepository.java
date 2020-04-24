package Repository;

import Exceptions.MyException;
import Model.PrgState.PrgState;

import java.util.List;

public interface IRepository {
    //public PrgState getCrtPrg();

    public void add(PrgState prg);

    public void logPrgStateExec(PrgState state) throws MyException;

    public List<PrgState> getPrgList();

    void setPrgList(List<PrgState> listState);

}
