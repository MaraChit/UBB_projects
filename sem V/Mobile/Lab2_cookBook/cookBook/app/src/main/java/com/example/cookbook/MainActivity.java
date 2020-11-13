package com.example.cookbook;

import android.content.Intent;
import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.cookbook.adapter.RecipeAdapter;
import com.example.cookbook.model.Recipe;
import com.example.cookbook.repository.Repository;
import com.example.cookbook.CookBookApplication;
import com.google.android.material.floatingactionbutton.FloatingActionButton;

import java.util.List;
import java.util.Objects;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        CookBookApplication application = (CookBookApplication) getApplicationContext();
        Repository repository = application.getRepo();
        List<Recipe> exampleList = repository.getAll();

        RecyclerView rv = (RecyclerView) findViewById(R.id.recycler_view);
        RecipeAdapter adapter = new RecipeAdapter(exampleList);

        rv.setAdapter(adapter);
        rv.setLayoutManager(new LinearLayoutManager(this));

        FloatingActionButton addButton = (FloatingActionButton) findViewById(R.id.floating_action_button);
        addButton.setOnClickListener(v->{
            Intent addActivity = new Intent(getApplicationContext(), AddActivity.class);
            addActivity.setFlags(Intent.FLAG_ACTIVITY_NO_HISTORY);
            startActivityForResult(addActivity, 1);
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if(resultCode == 1 || resultCode == 2 || resultCode == 3){
            RecyclerView rv = (RecyclerView) findViewById(R.id.recycler_view);
            Objects.requireNonNull(rv.getAdapter()).notifyDataSetChanged();
        }
    }
}
