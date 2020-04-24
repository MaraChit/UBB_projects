package Model.Values;

import Model.Type.RefType;
import Model.Type.Type;

public class RefValue implements Value {
    int address;
    Type locationType;

    public RefValue(Type t, int addrs)
    {
        locationType = t;
        address = addrs;
    }

    public int getAddr()
    {
        return address;
    }

    @Override
    public Type getType() {
        return new RefType(locationType);
    }

    @Override
    public String toString() {
        return "("+String.valueOf(address)+","+locationType.toString()+")";
    }
}
