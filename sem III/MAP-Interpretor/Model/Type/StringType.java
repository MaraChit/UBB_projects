package Model.Type;

import Model.Values.StringValue;

public class StringType implements Type {

    public StringType(){}
    @Override
    public boolean equals(Object another){

        if (another instanceof StringType)
            return true;
        else
            return false;
    }

    @Override
    public StringValue defaultValue() {
        return  new StringValue("");
    }

    @Override
    public String toString() {
        return "string";
    }
}
