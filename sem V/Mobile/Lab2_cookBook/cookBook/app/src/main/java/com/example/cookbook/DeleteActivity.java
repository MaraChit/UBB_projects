package com.example.cookbook;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.cookbook.model.Recipe;
import com.example.cookbook.repository.Repository;

public class DeleteActivity extends AppCompatActivity{
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.delete_recipe);

        CookBookApplication application = (CookBookApplication) getApplicationContext();
        Repository repository = application.getRepo();

        Bundle bundle = getIntent().getExtras();
        int position = bundle.getInt("position");

        String textToDisplay = "Are you sure you want to delete this recipe ?";
        TextView textView = findViewById(R.id.deleteText);
        textView.setText(textToDisplay);

        Button deleteButton = (Button) findViewById(R.id.deleteBtn);
        deleteButton.setOnClickListener(v->{
            repository.delete(position);
            Intent mainActivity = new Intent(getApplicationContext(), MainActivity.class);
            mainActivity.setFlags(Intent.FLAG_ACTIVITY_NO_HISTORY);
            startActivityForResult(mainActivity, 3);
        });

        Button cancelButton = (Button) findViewById(R.id.cancelDeleteBtn);
        cancelButton.setOnClickListener(v->{
            Intent mainActivity = new Intent(getApplicationContext(), MainActivity.class);
            mainActivity.setFlags(Intent.FLAG_ACTIVITY_NO_HISTORY);
            startActivity(mainActivity);
        });
    }

}
