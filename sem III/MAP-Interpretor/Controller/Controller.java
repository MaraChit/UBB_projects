package Controller;

import Exceptions.MyException;
import Model.PrgState.MyIHeap;
import Model.PrgState.MyIStack;
import Model.PrgState.PrgState;
import Model.Stm.IStmt;
import Model.Values.RefValue;
import Model.Values.Value;
import Repository.IRepository;

import java.nio.channels.ScatteringByteChannel;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Controller{
   private IRepository repo;
    private ExecutorService executor;

    public Controller(IRepository repo) {
        this.repo = repo;
    }

    public List<Integer> getIds(){
        return repo.getPrgList().stream().map(p->p.getPrgId()).collect(Collectors.toList());
    }

    public List<String> getOut(){
        return repo.getPrgList().get(0).getOut().getList().stream().map(p->p.toString()).collect(Collectors.toList());
    }

    public List<String> getFileTblAsString(){return repo.getPrgList().get(0).getFileTable().getContent().keySet().stream().map(p -> p.toString()).collect(Collectors.toList());}

    public MyIHeap getHeap(){return repo.getPrgList().get(0).getHeap();}

    public PrgState getPrgByIndex(int index){ return repo.getPrgList().get(index);}

    public boolean finishExec(){return removeCompletedPrg(repo.getPrgList()).size()==0;}

    Map<Integer, Value> safeGarbageCollector(List<Integer> symTableAddr, Map<Integer,Value>
            heap){
        return heap.entrySet().stream()
                .filter(e->symTableAddr.contains(e.getKey()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }



    public static List<Integer> getAddrFromSymTable (Collection<Value> symTableValues, Collection<Value> heap){
        return Stream.concat(
                heap.stream()
                        .filter(v-> v instanceof RefValue)
                        .map(v-> {RefValue v1 = (RefValue)v; return v1.getAddr();}),
                symTableValues.stream()
                        .filter(v-> v instanceof RefValue)
                        .map(v-> {RefValue v1 = (RefValue)v; return v1.getAddr();})
        )
                .collect(Collectors.toList());


    }

    /*public PrgState oneStep(PrgState state) throws MyException {
        MyIStack<IStmt> stk=state.getStk();
        if(stk.isEmpty()) {

            throw new MyException("prgstate stack is empty");
        }
        IStmt crtStmt = stk.pop();
        return crtStmt.execute(state);
    }

    public void allSteps()throws MyException{

        PrgState prg = repo.getCrtPrg(); // repo is the controller field of type MyRepoInterface
        //here you can display the prg state

            while (!prg.getStk().isEmpty()) {
                oneStep(prg);
                repo.logPrgStateExec();
                prg.getHeap().setContent(safeGarbageCollector(
                        getAddrFromSymTable(
                                prg.getSymTable().getContent().values(),
                                prg.getHeap().getContent().values()),
                        prg.getHeap().getContent()));
                //here you can display the prg state
            }


    }*/


    List<PrgState> removeCompletedPrg(List<PrgState> inPrgList)
    {
        return inPrgList.stream().filter(v->v.isNotCompleted()).collect(Collectors.toList());
    }

    public void oneStepForAllPrg(List<PrgState> prgList) throws MyException, InterruptedException {
        /*prgList.forEach(p-> {
            try {
                repo.logPrgStateExec(p);
                System.out.println(p.toString());
            } catch (MyException e) {
                System.out.println(e.getMessage());
            }
        });*/
        List<Callable<PrgState>> callList = prgList.stream().
                map((PrgState p) -> (Callable<PrgState>)(()->{return p.oneStep();})).collect(Collectors.toList());
        try {
            List<PrgState> newProgramList = executor.invokeAll(callList).stream()
                    .map(programStateFuture -> {try{
                        return programStateFuture.get();
                    } catch (ExecutionException e) {
                        throw new RuntimeException("Thread exception: " + e.getMessage());
                    } catch (InterruptedException e) {
                        throw new RuntimeException("Thread exception: " + e.getMessage());
                    }
                    })
                    .filter(programState -> programState != null)
                    .collect(Collectors.toList());
            prgList.addAll(newProgramList);
            prgList.forEach(p-> {
                try {
                    repo.logPrgStateExec(p);
                    System.out.println(p.toString());
                } catch (MyException e) {
                    System.out.println(e.getMessage());
                }
            });
            repo.setPrgList(prgList);
        }
        catch (InterruptedException e)
        {
            throw new MyException("Thread exception");
        }
        /*catch (RuntimeException e)
        {
            throw new MyException("Thread exception");
        }*/
    }

    public void allStepsModifiedToBeOneStep() throws MyException, InterruptedException {
        executor = Executors.newFixedThreadPool(2);
        List<PrgState> prgList=removeCompletedPrg(repo.getPrgList());
        oneStepForAllPrg(prgList);

        Collection<Value> allSymTbl = new ArrayList<>();
        prgList.forEach(v-> allSymTbl.addAll(v.getSymTable().getContent().values()));
        List<Integer> addr = getAddrFromSymTable(allSymTbl, prgList.get(0).getHeap().getContent().values());
        Map<Integer, Value> newHeap = safeGarbageCollector(addr, prgList.get(0).getHeap().getContent());
        prgList.get(0).getHeap().setContent(newHeap);
        //prgList=removeCompletedPrg(repo.getPrgList());


        executor.shutdownNow();
        repo.setPrgList(prgList);
    }

}
