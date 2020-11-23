import React from 'react';
import { StyleSheet} from 'react-native';
import { createStore } from 'redux'
import { Provider } from 'react-redux';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from './src/screens/homeScreen';
import AddScreen from './src/screens/addScreen';
import EditScreen from './src/screens/editScreen';
import DeleteScreen from './src/screens/deleteScreen';
import recipeReducer from './src/redux/reducers/recipeReducer';
import { HOME, ADD, EDIT, DELETE } from './src/constants/navigationConstants';


const Stack = createStackNavigator();
const store = createStore(recipeReducer);

export default function App() {
  return (
    <Provider store={store}>
      <NavigationContainer>
        <Stack.Navigator initialRouteName={HOME}>
          <Stack.Screen name={HOME} component={HomeScreen} />
          <Stack.Screen name={ADD} component={AddScreen} />
          <Stack.Screen name={EDIT} component={EditScreen} />
          <Stack.Screen name={DELETE} component={DeleteScreen} />
        </Stack.Navigator>
      </NavigationContainer>
    </Provider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
