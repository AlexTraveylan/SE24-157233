package com.example.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import lombok.Getter;
import lombok.Setter;
import lombok.NoArgsConstructor;

/* NE PAS TOUCHER */
/* ENTITE DE FILM */

@Entity
@Table(name = "movies")
@Getter
@Setter
@NoArgsConstructor
public class Movie {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;
    private String title;
    private int likes;

    public Movie(String title) {
        this.title = title;
        this.likes = 0;
    }

    public void incrementLikes() {
        this.likes++;
    }
}

/* NE PAS TOUCHER */
