package com.example.cookbook;

import android.app.Application;

import com.example.cookbook.repository.Repository;

public class CookBookApplication extends Application {
    public Repository repo;

    public Repository getRepo() {
        return repo;
    }

    @Override
    public void onCreate() {
        super.onCreate();
        repo = new Repository();
    }
}
