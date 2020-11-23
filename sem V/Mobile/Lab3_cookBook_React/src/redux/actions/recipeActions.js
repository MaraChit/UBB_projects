import { ADD_RECIPE, EDIT_RECIPE, DELETE_RECIPE } from './actionTypes'

export const addRecipe = (payload) => (
    {
        type: ADD_RECIPE,
        payload
    }
)

export const editRecipe = (payload) => (
    {
        type: EDIT_RECIPE,
        payload
    }
)

export const deleteRecipe = (payload) => (
    {
        type: DELETE_RECIPE,
        payload
    }
)