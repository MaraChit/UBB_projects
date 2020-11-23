import React from "react"
import {
    SafeAreaView,
    TouchableHighlight,
    StyleSheet,
    FlatList,
    View,
    Text,
    StatusBar,
} from 'react-native';

import { connect } from 'react-redux';

import { ADD, EDIT } from "../constants/navigationConstants";

const mapStateToProps = (state) => {
    return {
        recipes: state.recipeRepo
    }
}

const mapDispatchToProps = (dispatch) => {
    return {

    }
}

const RecipeItem = (props) => (
        <View style={styles.recipeItem}>
            <Text style={styles.recipeName}>{props.recipeName}</Text>
            <Text style={styles.difficulty}>{props.difficulty}</Text>
            <Text style={styles.ingredients}>{props.ingredients}</Text>
            <Text style={styles.instructions}>{props.instructions}</Text>
        </View>
);

const HomeScreen = (props) => {
    const DATA = props.recipes;

    const renderRecipeItem = ( {item, index} ) => (
        <TouchableHighlight
            key={index.toString()}
            activeOpacity={0.6}
            underlayColor="#DDDDDD"
            onPress={() => props.navigation.navigate(EDIT, { id: item.id })}
            style={styles.recipeItemTouchable}>
            <RecipeItem
                id={item.id}
                recipeName={item.recipeName}
                difficulty={item.difficulty}
                ingredients={item.ingredients}
                instructions={item.instructions}
            />
        </TouchableHighlight>
    );

    return (
        <SafeAreaView style={styles.container}>
            <FlatList
                data={DATA}
                renderItem={renderRecipeItem}
                keyExtractor={item => item.id}
            />
            <TouchableHighlight
                activeOpacity={0.6}
                underlayColor="#AE4D8E"
                onPress={() => props.navigation.navigate(ADD) }
                style={styles.fab}>
                <Text style={styles.fab_plus}>+</Text>
            </TouchableHighlight>
        </SafeAreaView>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        marginTop: StatusBar.currentHeight || 0,
        
    },
    recipeItem: {
        padding: 15,
        borderRadius: 10,
        borderWidth: 2,
        borderColor: '#C2C2C2',
        alignItems: 'center',
        backgroundColor: "#ffcc99"
    },
    recipeItemTouchable: {
        marginVertical: 5,
        marginHorizontal: 15,
        borderRadius: 10,
    },
    recipeName: {
        fontSize: 20,
        fontWeight: "bold"
    },
    difficulty: {
        fontSize: 12,
        fontStyle: "italic",
        fontWeight: "bold",
        color: "#ff8f66"
    },
    ingredients: {
        fontSize: 15,
    },
    instructions: {
        fontSize: 15,
    },
    fab: {
        width: 60,
        height: 60,
        borderRadius: 30,
        position: 'absolute',
        bottom: 20,
        right: 20,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#ff8f66',
    },
    fab_plus: {
        fontSize: 40,
        color: '#FFFFFF'
    }
});


export default connect(mapStateToProps, mapDispatchToProps)(HomeScreen)
