package Model.PrgState;

import Model.Values.StringValue;

import java.io.BufferedReader;
import java.io.Reader;
import java.util.HashMap;

public interface MyIFileTable<S, B extends Reader> {

    boolean isDefined(StringValue name);


    void add(StringValue name, BufferedReader fd);

    BufferedReader get(StringValue v);

    HashMap<StringValue, BufferedReader> getContent();

    void delete(StringValue v);
}
