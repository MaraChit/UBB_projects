package Model.PrgState;

import Model.Values.Value;

import java.util.HashMap;
import java.util.Map;

public class MyHeap implements MyIHeap {

    HashMap<Integer, Value> heap;
    int key;

    public MyHeap()
    {
        heap = new HashMap<Integer, Value>();
        key = 0;
    }

    @Override
    public String toString() {
        String res = "";
        for (Integer k : heap.keySet())
        {
            res += "\t" + String.valueOf(k) + "->" + heap.get(k) + "\n";
        }
        return res;
    }

    @Override
    public void add(Value v) {
        key++;
        heap.put(key, v);
    }

    @Override
    public int getCurrentKey() {
        return key;
    }

    @Override
    public boolean isKey(int addr) {
        return heap.containsKey(addr);
    }

    @Override
    public Value getValue(int addr) {
        return heap.get(addr);
    }

    @Override
    public void update(int addr, Value v) {
        heap.put(addr, v);
    }

    @Override
    public void setContent(Map<Integer, Value> m) {
        heap.clear();
        for (Integer key:
                m.keySet()) {
            heap.put(key, m.get(key));
        }
    }

    @Override
    public Map<Integer, Value> getContent() {
        return heap;
    }
}

