import { ADD_RECIPE, EDIT_RECIPE, DELETE_RECIPE } from '../actions/actionTypes'
import { DATA } from '../../constants/data'
import _ from 'lodash'

import { addRecipe, editRecipe, deleteRecipe } from '../../utils/helpers'

const initialState = {
    recipeRepo: _.cloneDeep(DATA)
}

const recipeReducer = (state = initialState, action) => {
    switch(action.type) {
        case DELETE_RECIPE:
            {
                const newRepo = deleteRecipe(_.cloneDeep(state.recipeRepo), action.payload)
                return ({
                    recipeRepo: newRepo
                });
            }

        case ADD_RECIPE:
            {
                const newRepo = addRecipe(_.cloneDeep(state.recipeRepo), action.payload);
                return ({
                    recipeRepo: newRepo
                });
            }

        case EDIT_RECIPE:
            {
                const newRepo = editRecipe(_.cloneDeep(state.recipeRepo), action.payload.id, action.payload.newRecipe);
                return ({
                    recipeRepo: newRepo
                });
            }

        default:
            return state;
    }
};

export default recipeReducer;