package Model.PrgState;



import java.util.HashMap;
import java.util.Map;

import Exceptions.MyException;
import Model.Type.BoolType;
import Model.Type.IntType;
import Model.Values.BoolValue;
import Model.Values.IntValue;
import Model.Values.Value;


public class MyDictionary<String,Value> implements MyIDictionary<String,Value>{
    private HashMap<String, Value> dictionary;

    public MyDictionary(){
        dictionary = new HashMap<String, Value>();
    }
    public Value getValue(String k)throws MyException{
        return dictionary.get(k);
    }
   // void addValue(String k, Value v){
    //    dictionary.put(k,v);
    //}
    public void update(String k , Value v){
        dictionary.put(k,v);
    }

    @Override
    public Value lookup(String id) throws  MyException {
         /*if(getValue(id).getType().equals(new BoolType()))
             return (BoolValue) getValue(id);

         if(getValue(id).getType().equals(new IntType()))
             return (IntValue) getValue(id);*/

         return getValue(id);

    }

    @Override
    public boolean isDefined(String id) {

        return(dictionary.get(id) != null);
    }

    @Override
    public MyIDictionary<String, Value> clone() {
        MyIDictionary<String, Value> output = new MyDictionary<>();
        for(String k:this.dictionary.keySet()) {
            try {
                output.update(k, this.lookup(k));
            } catch (MyException e) {
                e.printStackTrace();
            }
        }
        return output;
    }

    @Override
    public Map<String, Value> getContent() {
        return dictionary;
    }
    @Override
    public java.lang.String toString() {
        return dictionary.toString();
    }
}
