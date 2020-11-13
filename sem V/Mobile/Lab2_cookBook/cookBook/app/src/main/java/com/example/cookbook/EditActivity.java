package com.example.cookbook;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.cookbook.model.Recipe;
import com.example.cookbook.repository.Repository;

public class EditActivity extends AppCompatActivity {
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.update_recipe);

        CookBookApplication application = (CookBookApplication) getApplicationContext();
        Repository repository = application.getRepo();

        Bundle bundle = getIntent().getExtras();
        int position = bundle.getInt("position");

        EditText nameInput = findViewById(R.id.recipeNameEditInput);
        String name = bundle.getString("name");
        nameInput.setText(name);

        EditText difficultyInput = findViewById(R.id.difficultyEditInput);
        String difficulty = bundle.getString("difficulty");
        difficultyInput.setText(difficulty);

        EditText ingredientsInput = findViewById(R.id.ingredientsEditInput);
        String ingredients = bundle.getString("ingredients");
        ingredientsInput.setText(ingredients);

        EditText instructionsInput = findViewById(R.id.instructionsEditInput);
        String instructions = bundle.getString("instructions");
        instructionsInput.setText(instructions);

        Button updateButton = (Button) findViewById(R.id.updateBtn);
        updateButton.setOnClickListener(v->{
            repository.update(new Recipe(nameInput.getText().toString(),difficultyInput.getText().toString(),ingredientsInput.getText().toString(),instructionsInput.getText().toString()), position);
            Intent mainActivity = new Intent(getApplicationContext(), MainActivity.class);
            mainActivity.setFlags(Intent.FLAG_ACTIVITY_NO_HISTORY);
            startActivityForResult(mainActivity, 2);
        });

        Button deleteButton = (Button) findViewById(R.id.deleteBtn2);
        deleteButton.setOnClickListener(v->{
            Intent deleteActivity = new Intent(getApplicationContext(), DeleteActivity.class);
            deleteActivity.putExtra("position", position);
            deleteActivity.setFlags(Intent.FLAG_ACTIVITY_NO_HISTORY);
            startActivity(deleteActivity);
        });

        Button cancelButton = (Button) findViewById(R.id.cancelEditBtn);
        cancelButton.setOnClickListener(v->{
            Intent mainActivity = new Intent(getApplicationContext(), MainActivity.class);
            mainActivity.setFlags(Intent.FLAG_ACTIVITY_NO_HISTORY);
            startActivity(mainActivity);
        });
    }
}
