package com.example.cookbook;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.cookbook.model.Recipe;
import com.example.cookbook.repository.Repository;
import com.google.android.material.floatingactionbutton.FloatingActionButton;

import java.util.List;

public class AddActivity extends AppCompatActivity {
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.add_recipe);

        CookBookApplication application = (CookBookApplication) getApplicationContext();
        Repository repository = application.getRepo();

        EditText nameInput = findViewById(R.id.recipeNameAddInput);
        EditText difficultyInput = findViewById(R.id.difficultyAddInput);
        EditText ingredientsInput = findViewById(R.id.ingredientsAddInput);
        EditText instructionsInput = findViewById(R.id.instructionsAddInput);
        
        Button addButton = (Button) findViewById(R.id.addRecipeBtn);
        addButton.setOnClickListener(v->{
            repository.add(new Recipe(nameInput.getText().toString(),difficultyInput.getText().toString(),ingredientsInput.getText().toString(),instructionsInput.getText().toString()));
            Intent mainActivity = new Intent(getApplicationContext(), MainActivity.class);
            mainActivity.setFlags(Intent.FLAG_ACTIVITY_NO_HISTORY);
            startActivityForResult(mainActivity, 1);
        });

        Button cancelButton = (Button) findViewById(R.id.cancelAddBtn);
        cancelButton.setOnClickListener(v->{
            Intent mainActivity = new Intent(getApplicationContext(), MainActivity.class);
            mainActivity.setFlags(Intent.FLAG_ACTIVITY_NO_HISTORY);
            startActivity(mainActivity);
        });
    }
}
