package Model.PrgState;

import java.util.Stack;

public interface MyIStack<T>{
    public T pop();
    public void push(T v);
    public Stack<T> getContentStk();
    boolean isEmpty();
}

