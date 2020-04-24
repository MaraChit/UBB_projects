package Model.PrgState;

import Model.Values.StringValue;

import java.io.BufferedReader;
import java.io.Reader;
import java.util.HashMap;

public class MyFileTable implements MyIFileTable<StringValue, Reader> {

    private HashMap<StringValue, BufferedReader> filetable;

    public MyFileTable()
    {
        filetable = new HashMap<StringValue,BufferedReader>();
    }

    @Override
    public boolean isDefined(StringValue name) {
        return filetable.containsKey(name);
    }

    public HashMap<StringValue, BufferedReader> getContent() {return filetable;}

    @Override
    public void add(StringValue name, BufferedReader fd) {

        filetable.put(name, fd);

    }

    @Override
    public BufferedReader get(StringValue v) {
        return filetable.get(v);
    }

    @Override
    public void delete(StringValue v) {
         filetable.remove(v);

    }

    @Override
    public String toString() {
        String res="";
        for (StringValue s: filetable.keySet()
        ) {
            res += "\t"+s.toString() + "\n";
        }
        return res;
    }
}
