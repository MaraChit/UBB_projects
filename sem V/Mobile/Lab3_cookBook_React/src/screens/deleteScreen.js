import React from "react"
import {
    StyleSheet,
    View,
    Text
} from 'react-native';

import { TouchableHighlight } from "react-native-gesture-handler";
import { connect } from 'react-redux';
import { deleteRecipe } from '../redux/actions/recipeActions'
import { HOME } from "../constants/navigationConstants";

const mapStateToProps = (state) => {
    return {
        recipes: state.recipeRepo
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        deleteRecipe: (payload) => dispatch(deleteRecipe(payload))
    }
}

const DeleteScreen = ( props ) => {
    const { id } = props.route.params;

    const DATA = props.recipes;
    const deleteRecipe = props.deleteRecipe;

    const item = DATA.find((elem) => { return elem.id === id });

    const handleDeleteRecipe = () => {
        deleteRecipe(item.id);
        props.navigation.reset({
            index: 0,
            routes: [
              {
                name: HOME,
              }
            ]
        });
    };

    const handleCancelRecipe = () => {
        props.navigation.navigate(HOME);
    };

    return (
        <View>
            <Text style={styles.questionText}>
                Are you sure you want to delete this recipe?
            </Text>

            <TouchableHighlight
                activeOpacity={0.6}
                underlayColor="#AE4D8E"
                onPress={() => handleDeleteRecipe() }
                style={styles.deleteRecipe}>
                <Text style={styles.deleteRecipeText}>Yes</Text>
            </TouchableHighlight>

            <TouchableHighlight
                activeOpacity={0.6}
                underlayColor="#AE4D8E"
                onPress={() => handleCancelRecipe() }
                style={styles.deleteRecipe}>
                <Text style={styles.deleteRecipeText}>No</Text>
            </TouchableHighlight>
        </View>
    );
}

const styles = StyleSheet.create({
    questionText:{
        margin: 10,
        padding: 10,
        borderRadius: 15,
        fontWeight: "bold",
        fontSize: 20
    },
    deleteRecipe: {
        backgroundColor: '#ff8f66', 
        margin: 10,
        padding: 15,
        borderRadius: 10,
        alignItems: 'center'
    },
    deleteRecipeText:{
        color: '#FFFFFF',
        fontSize: 20
    }
});

export default connect(mapStateToProps, mapDispatchToProps)(DeleteScreen);