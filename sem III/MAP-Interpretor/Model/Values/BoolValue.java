package Model.Values;

import Model.Type.BoolType;
import Model.Type.StringType;
import Model.Type.Type;

public class BoolValue implements Value{

    boolean val;
    public BoolValue(boolean v){val=v;}

    public boolean equals(Object another){

        if (another instanceof BoolValue)
            if(((BoolValue) another).getVal() == val)
                return  true;
            else
                return false;
        else
            return false;
    }

    public boolean getVal() {return val;}
    public String toString() {

        return  String.valueOf(val);
    }
    public Type getType() {
        return new BoolType();
    }

}