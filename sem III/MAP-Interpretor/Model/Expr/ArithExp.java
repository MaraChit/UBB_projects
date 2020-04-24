package Model.Expr;

import Exceptions.MyException;
import Model.PrgState.MyIDictionary;
import Model.PrgState.MyIHeap;
import Model.Type.IntType;
import Model.Type.Type;
import Model.Values.IntValue;
import Model.Values.Value;
public class ArithExp implements Exp {
    Exp e1;
    Exp e2;
    int op;
    char ops;

     public ArithExp(char c, Exp e1, Exp e2) {
        if(c=='+')
            this.op=1;
        else if (c=='-')
            this.op = 2;
        else if (c=='*')
            this.op =3;
        else if (c=='/')
            this.op =4;
        ops = c;
        this.e2= e2;
        this.e1= e1;
    }
/*
    public ArithExp(char c, ValueExp valueExp, ArithExp arithExp) {
        this.op= c;
        e2
    }
*/
    public Value eval(MyIDictionary<String, Value> tbl, MyIHeap hp) throws MyException {
        Value v1, v2;
        v1 = e1.eval(tbl,hp);
        if (v1.getType().equals(new IntType())) {
            v2 = e2.eval(tbl,hp);
            if (v2.getType().equals(new IntType())) {
                IntValue i1 = (IntValue) v1;
                IntValue i2 = (IntValue) v2;
                int n1, n2;
                n1 = i1.getVal();
                n2 = i2.getVal();
                if (op == 1) return new IntValue(n1 + n2);
                if (op == 2) return new IntValue(n1 - n2);
                if (op == 3) return new IntValue(n1 * n2);
                if (op == 4)
                    if (n2 == 0) throw new MyException("division by zero");
                    else return new IntValue(n1 / n2);
            } else
                throw new MyException("second operand is not an integer");
        } else
            throw new MyException("first operand is not an integer");
    return new IntValue(0);
    }

    @Override
    public Type typecheck(MyIDictionary<String,Type> typeEnv) throws MyException {
        Type typ1, typ2;
        typ1 = e1.typecheck(typeEnv);
        typ2 = e2.typecheck(typeEnv);
        if (typ1.equals(new IntType())){
            if(typ2.equals(new IntType())){
                return new IntType();
            } else
            throw new MyException("second operand is not an integer");
        }else
        throw new MyException("first operand is not an integer");
    }


    @Override
    public String toString(){ return e1.toString()+String.valueOf(ops)+e2.toString();}
}

