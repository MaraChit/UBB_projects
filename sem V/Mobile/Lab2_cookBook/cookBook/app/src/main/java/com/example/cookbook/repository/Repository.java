package com.example.cookbook.repository;

import com.example.cookbook.model.Recipe;

import java.util.ArrayList;

public class Repository {
    private static ArrayList<Recipe> recipes;

    public Repository() {
        InitRepo();
    }

    private void InitRepo() {
        recipes = new ArrayList<>();

        recipes.add(new Recipe("muffins", "easy", "ingredients for muffins", "instructions for muffins"));
        recipes.add(new Recipe("apple pie", "medium", "apples", "instructions"));
        recipes.add(new Recipe("chicken soup", "easy", "chicken", "boil water"));
        recipes.add(new Recipe("sarmale", "difficult", "rice", "instructions 2"));

    }

    public void add(Recipe recipe) {
        recipes.add(recipe);
    }

    public void update(Recipe recipe, int index) {
        recipes.set(index, recipe);
    }

    public void delete(int position) {
        recipes.remove(position);
    }

    public ArrayList<Recipe> getAll() {
        return recipes;
    }

}
