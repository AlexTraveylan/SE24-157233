package com.example.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.example.repository.MovieRepository;
import com.example.model.Movie;
import java.util.List;

/* ICI LE CODE EST A MODIFIER */
@Service
public class MovieController {
    @Autowired
    private MovieRepository movieRepository;

    public void addMovie(String title) {

    }

    public void likeMovie(int id) {
    }

    public List<Movie> getAllMoviesSortedByLikes() {

    }
}