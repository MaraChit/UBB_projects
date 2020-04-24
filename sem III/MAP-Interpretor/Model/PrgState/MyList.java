package Model.PrgState;

import java.util.LinkedList;
import java.util.List;

public class MyList<T> implements MyIList<T> {
    private LinkedList<T> list;

    public MyList() {
        this.list = new LinkedList<T>();
    }

    @Override
    public void add(T el) {
        list.add(el);
    }

    @Override
    public List<T> getList() {
        return list;
    }

    @Override
    public String toString() {
        return list.toString();
    }
}
