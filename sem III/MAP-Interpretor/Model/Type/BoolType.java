package Model.Type;

import Model.Values.BoolValue;
import Model.Values.Value;

public class BoolType implements Type {

    public BoolType(){}

    public boolean equals(Object another){
        if (another instanceof BoolType)
            return true;
        else
            return false;
    }
    public String toString() { return "bool";}

    @Override
    public Value defaultValue() {
        return new BoolValue(false);
    }
}
