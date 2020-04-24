package Model.PrgState;

import Exceptions.MyException;
import Model.Values.Value;

import java.util.Map;

public interface MyIDictionary<K,v> {
    v getValue(K k) throws MyException;
    void update(K k , v x);

    v lookup(K id) throws MyException;

    boolean isDefined(K id);

    MyIDictionary<K, v> clone();

    Map<K, v> getContent();
}
