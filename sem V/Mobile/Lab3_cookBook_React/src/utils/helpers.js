export const emptyFn = () => {}

export const addRecipe = (repo, recipe) => {
    repo.push(recipe);
    return repo;
}

export const editRecipe = (repo, id, newRecipe) => {
    const Recipe = repo.find((elem) => { return elem.id === id });

    Recipe.recipeName = newRecipe.recipeName;
    Recipe.difficulty = newRecipe.difficulty;
    Recipe.ingredients = newRecipe.ingredients;
    Recipe.instructions = newRecipe.instructions;

    return repo;
}

export const deleteRecipe = (repo, id) => {
    repo = repo.filter((elem) => { return elem.id !== id });
    return repo;
}