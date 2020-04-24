package Model.Values;

import Model.Type.IntType;
import Model.Type.StringType;
import Model.Type.Type;

public class IntValue implements Value{
    int val;
    public IntValue(int v){val=v;}

    public int getVal() {return val;}

    public boolean equals(Object another){

        if (another instanceof IntValue)
            if (((IntValue) another).getVal() == val)
                return true;
            else
                return false;
        else
            return false;
    }
    public String toString() {
        return  String.valueOf(val);
    }

    public  Type getType() {
        return new IntType();
    }
}


