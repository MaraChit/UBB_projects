import React, { useState } from "react";
import {
    StyleSheet,
    View,
    Text,
    TextInput
} from 'react-native';

import { TouchableHighlight } from "react-native-gesture-handler";
import { connect } from 'react-redux';
import { addRecipe, deleteRecipe } from '../redux/actions/recipeActions'
import { HOME } from "../constants/navigationConstants";

const mapStateToProps = (state) => {
    return {
        recipes: state.recipeRepo
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        addRecipe: (payload) => dispatch(addRecipe(payload))
    }
}


const AddScreen = ( props ) => {
    const DATA = props.recipes;
    const addRecipe = props.addRecipe;

    const [recipeName, setRecipeName] = useState('');
    const [difficulty, setDifficulty] = useState('');
    const [ingredients, setIngredients] = useState('');
    const [instructions, setInstructions] = useState('');
    
    const handleAddrecipe = () => {
        const newID = Math.random().toString(36).substring(7);
        var recipe = { id: newID, recipeName: recipeName, difficulty: difficulty, ingredients: ingredients, instructions: instructions}

        addRecipe(recipe);

        alert("New recipe was added! ID: " + newID);
        props.navigation.navigate(HOME);
    };

    return (
        <View style={{padding: 10}}>
            <TextInput
                style={styles.inputText}
                placeholder="recipe name"
                onChangeText={recipeName => setRecipeName(recipeName)}
                defaultValue={recipeName}
            />
            <TextInput
                style={styles.inputText}
                placeholder="difficulty"
                onChangeText={difficulty => setDifficulty(difficulty)}
                defaultValue={difficulty}
            />
            <TextInput
                style={styles.inputText}
                placeholder="ingredients"
                onChangeText={ingredients => setIngredients(ingredients)}
                defaultValue={ingredients}
            />
            <TextInput
                style={styles.inputText}
                placeholder="instructions"
                onChangeText={instructions => setInstructions(instructions)}
                defaultValue={instructions}
            />
            
            <TouchableHighlight
                activeOpacity={0.6}
                underlayColor="#AE4D8E"
                onPress={() => handleAddrecipe() }
                style={styles.addrecipe}>
                <Text style={styles.addrecipeText}>Add recipe</Text>
            </TouchableHighlight>
        </View>
    );
}

const styles = StyleSheet.create({
    inputText: {
        margin: 10,
        padding: 10,
        borderRadius: 15,
        borderWidth: 2,
        borderColor: '#ff8f66',
        fontSize: 20
    },
    addrecipe: {
        backgroundColor: '#ff8f66', 
        margin: 10,
        padding: 15,
        borderRadius: 10,
        alignItems: 'center'
    },
    addrecipeText:{
        color: '#FFFFFF',
        fontSize: 20
    }
});

export default connect(mapStateToProps, mapDispatchToProps)(AddScreen);