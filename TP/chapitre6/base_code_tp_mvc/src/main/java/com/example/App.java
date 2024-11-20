package com.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

import com.example.view.ConsoleView;

/* NE PAS TOUCHER */

@SpringBootApplication
public class App {
    public static void main(String[] args) {
        ApplicationContext context = SpringApplication.run(App.class, args);
        ConsoleView view = context.getBean(ConsoleView.class);
        view.start();
    }
}

/* NE PAS TOUCHER */
