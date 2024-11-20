package com.example.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.example.model.Movie;
import java.util.List;

/* NE PAS TOUCHER */
/* REPOSITORY DE FILM */

@Repository
public interface MovieRepository extends JpaRepository<Movie, Integer> {
    List<Movie> findAllByOrderByLikesDesc();
}

/* NE PAS TOUCHER */