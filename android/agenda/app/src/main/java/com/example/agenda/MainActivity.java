package com.example.agenda;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Adapter

import androidx.annotation.Nullable;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MainActivity extends Activity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        List<String> alunos = new ArrayList<>(
                Arrays.asList("Alex", "Fran", "Pedro"));
        View listaDeLaunos = findViewById(R.id.activity_main_lista_de_alunos);
        listaDeLaunos.setAdapter(new ArrayAdapter<>(
                this, android.R.layout.simple_list_item_1, alunos));
    }

}

