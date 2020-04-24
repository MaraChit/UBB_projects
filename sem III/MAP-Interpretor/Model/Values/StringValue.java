package Model.Values;

import Model.Type.StringType;
import Model.Type.Type;

public class StringValue implements Value {

    String val;
    public StringValue(String s) {val = s;}

    @Override
    public Type getType() {
        return new StringType();
    }

    public String getVal() { return val;}

    public boolean equals(Object another){

        if (another instanceof StringValue)
            if (((StringValue) another).getVal() == val)
                return true;
            else
                return false;
        else
            return false;
    }

    @Override
    public String toString(){
        return val;
    }
}
