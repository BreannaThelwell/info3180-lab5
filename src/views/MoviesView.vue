<template>
  <div class="movies-container">
    <h1>Movies</h1>
    <div class="movies-grid">
      <div v-for="movie in movies" :key="movie.id" class="movie-card">
        <img :src="movie.poster" :alt="movie.title" class="movie-poster" />
        <div class="movie-info">
          <h2>{{ movie.title }}</h2>
          <p>{{ movie.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

const fetchMovies = async () => {
  try {
    const response = await fetch("http://localhost:8080/api/v1/movies");
    const data = await response.json();
    movies.value = data.movies;
  } catch (error) {
    console.error("Error fetching movies:", error);
  }
};

onMounted(fetchMovies);
</script>

<style scoped>
.movies-container {
  max-width: 900px;
  margin: 0 auto;
}

.movies-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: space-between;
}

.movie-card {
  display: flex;
  align-items: center;
  background: white;
  border-radius: 8px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  padding: 10px;
  width: calc(50% - 10px); /* Each card takes half the width with spacing */
  box-sizing: border-box;
}

.movie-poster {
  width: 120px;
  height: 180px;
  object-fit: cover;
  border-radius: 5px;
  margin-right: 15px;
}

.movie-info {
  flex: 1;
}

/* Make it stack on smaller screens */
@media (max-width: 768px) {
  .movie-card {
    width: 100%; /* Full width on small screens */
  }
}
</style>


