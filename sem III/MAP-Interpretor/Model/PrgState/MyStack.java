package Model.PrgState;

import java.util.Stack;

public class MyStack<T> implements MyIStack<T>{
    Stack<T> stack; //a field whose type CollectionType is an appropriate

    public MyStack()
    {
        stack = new Stack<T>();
    }
    @Override
    public void push(T v) {
        stack.push(v);
    }

    @Override
    public Stack<T> getContentStk() {
        return stack;
    }

    @Override
    public boolean isEmpty() {
        if(stack.isEmpty())
            return true;

        return false;
    }

    @Override
    public T pop() {
        return stack.pop();
    }

    @Override
    public String toString() {
        return stack.toString();
    }
}

