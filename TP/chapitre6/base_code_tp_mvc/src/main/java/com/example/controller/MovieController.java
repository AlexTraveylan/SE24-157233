package com.example.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.example.repository.MovieRepository;
import com.example.model.Movie;
import java.util.List;
import java.util.Optional;

/* ICI LE CODE EST A MODIFIER */
@Service
public class MovieController {
    @Autowired
    private MovieRepository movieRepository;

    public void addMovie(String title) {
        movieRepository.save(new Movie(title));
    }

    public void likeMovie(int id) {
        Optional<Movie> optionalMovie = movieRepository.findById(id);
        if (optionalMovie.isPresent()) {
            Movie movie = optionalMovie.get();
            movie.incrementLikes();
            movieRepository.save(movie);
        } else {
            throw new RuntimeException("Movie not found");
        }
    }

    public List<Movie> getAllMoviesSortedByLikes() {
        return movieRepository.findAllByOrderByLikesDesc();
    }
}