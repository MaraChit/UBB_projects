package com.example.cookbook.adapter;
import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.cookbook.EditActivity;
import com.example.cookbook.model.Recipe;
import com.example.cookbook.R;
import java.util.List;

public class RecipeAdapter extends RecyclerView.Adapter<RecipeAdapter.RecipeViewHolder> {
    private final List<Recipe> recipes;
    private Context context;

    public RecipeAdapter(List<Recipe> recipes) {
        this.recipes = recipes;
    }

    @NonNull
    @Override
    public RecipeViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        context = parent.getContext();
        LayoutInflater inflater = LayoutInflater.from(context);
        View roleView = inflater.inflate(R.layout.recipe_item_view, parent, false);

        RecipeViewHolder roleViewHolder = new RecipeViewHolder(roleView);
        return roleViewHolder;
    }

    @Override
    public void onBindViewHolder(@NonNull RecipeViewHolder holder, final int position) {
        final Recipe recipe = recipes.get(position);

        holder.name.setText(recipe.getName());
        holder.ingredients.setText(recipe.getIngredients());
        holder.difficulty.setText(recipe.getDifficulty());
        holder.instructions.setText(recipe.getInstructions());

        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent editActivity = new Intent(context.getApplicationContext(), EditActivity.class);
                editActivity.putExtra("position", position);
                editActivity.putExtra("name", recipe.getName());
                editActivity.putExtra("difficulty", recipe.getDifficulty());
                editActivity.putExtra("ingredients", recipe.getIngredients());
                editActivity.putExtra("instructions", recipe.getInstructions());
                context.startActivity(editActivity);
            }
        });
    }

    @Override
    public int getItemCount() {
        return recipes.size();
    }

    public class RecipeViewHolder extends RecyclerView.ViewHolder {
        public TextView name;
        public TextView difficulty;
        public TextView ingredients;
        public TextView instructions;

        public RecipeViewHolder(View itemView) {
            super(itemView);

            name = (TextView) itemView.findViewById(R.id.text_view_name);
            difficulty = (TextView) itemView.findViewById(R.id.text_view_difficulty);
            ingredients = (TextView) itemView.findViewById(R.id.text_view_ingredients);
            instructions = (TextView) itemView.findViewById(R.id.text_view_instructions);
        }
    }
}
