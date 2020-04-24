package Model.PrgState;

import Model.Values.Value;

import java.util.Map;


public interface MyIHeap {

        void add(Value v);

        int getCurrentKey();

        boolean isKey(int addr);

        Value getValue(int addr);

        void update(int addr, Value v);

        void setContent(Map<Integer, Value> m);

        Map<Integer, Value> getContent();
}

