import React, { useState } from "react"
import {
    StyleSheet,
    View,
    Text,
    TextInput
} from 'react-native';

import { TouchableHighlight } from "react-native-gesture-handler";
import { connect } from 'react-redux';

import { editRecipe } from '../redux/actions/recipeActions'
import { HOME, DELETE } from "../constants/navigationConstants";

const mapStateToProps = (state) => {
    return {
        recipes: state.recipeRepo
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        editRecipe: (payload) => dispatch(editRecipe(payload))
    }
}

const EditScreen = ( props ) => {
    const { id } = props.route.params;

    const DATA = props.recipes;
    const editRecipe = props.editRecipe;

    const item = DATA.find((elem) => { return elem.id === id });

    const [recipeName, setRecipeName] = useState(item.recipeName);
    const [difficulty, setDifficulty] = useState(item.difficulty);
    const [ingredients, setIngredients] = useState(item.ingredients);
    const [instructions, setInstructions] = useState(item.instructions);
    
    const handleEditRecipe = () => {
        var recipe = { id: item.id, recipeName: recipeName, recipeName: recipeName, difficulty: difficulty, ingredients: ingredients, instructions: instructions}

        editRecipe({ id: item.id, newRecipe: recipe})

        alert("The recipe was edited");
        props.navigation.navigate(HOME);
    };

    const handleDeleteRecipe = () => {
        props.navigation.navigate(DELETE, { id: item.id });
    };

    return (
        <View style={{padding: 10}}>
            <TextInput
                style={styles.inputText}
                placeholder={recipeName}
                onChangeText={recipeName => setRecipeName(recipeName)}
                defaultValue={recipeName}
            />
            <TextInput
                style={styles.inputText}
                placeholder={difficulty}
                onChangeText={difficulty => setDifficulty(difficulty)}
                defaultValue={difficulty}
            />
            <TextInput
                style={styles.inputText}
                placeholder={ingredients}
                onChangeText={ingredients => setIngredients(ingredients)}
                defaultValue={ingredients}
            />
            <TextInput
                style={styles.inputText}
                placeholder={instructions}
                onChangeText={instructions => setInstructions(instructions)}
                defaultValue={instructions}
            />
            
            <TouchableHighlight
                activeOpacity={0.6}
                underlayColor="#AE4D8E"
                onPress={() => handleEditRecipe() }
                style={styles.editRecipe}>
                <Text style={styles.editRecipeText}>Edit recipe</Text>
            </TouchableHighlight>

            <TouchableHighlight
                activeOpacity={0.6}
                underlayColor="#AE4D8E"
                onPress={() => handleDeleteRecipe() }
                style={styles.editRecipe}>
                <Text style={styles.editRecipeText}>Delete recipe</Text>
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
    editRecipe: {
        backgroundColor: '#ff8f66', 
        margin: 10,
        padding: 15,
        borderRadius: 10,
        alignItems: 'center'
    },
    editRecipeText:{
        color: '#FFFFFF',
        fontSize: 20
    }
});

export default connect(mapStateToProps, mapDispatchToProps)(EditScreen);