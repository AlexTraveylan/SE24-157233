package com.example.view;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import com.example.controller.MovieController;
import com.example.model.Movie;
import java.util.Scanner;

/* ICI LE CODE EST A MODIFIER */
/* CONSIGNE: Les méthodes de la vue affichent des messages à l'utilisateur dans le terminal */
/* Les actions de l'utilisateur sur la vue doivent appeler les méthodes du contrôleur */

@Component
public class ConsoleView {
    @Autowired
    private MovieController controller;
    private Scanner scanner;

    public ConsoleView() {
        this.scanner = new Scanner(System.in);
    }

    public void start() {
        while (true) {
            System.out.println("\n=== Menu Films ===");
            System.out.println("1. Ajouter un film");
            System.out.println("2. Liker un film");
            System.out.println("3. Afficher tous les films");
            System.out.println("4. Quitter");
            System.out.print("Votre choix : ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consommer la nouvelle ligne

            switch (choice) {
                case 1:
                    addMovie();
                    break;
                case 2:
                    likeMovie();
                    break;
                case 3:
                    displayMovies();
                    break;
                case 4:
                    System.out.println("Au revoir !");
                    return;
                default:
                    System.out.println("Choix invalide !");
            }
        }
    }

    private void addMovie() {

    }

    private void likeMovie() {

    }

    private void displayMovies() {

    }
}

/* ICI LE CODE EST A MODIFIER */
