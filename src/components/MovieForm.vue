<template>
  <div class="container mt-5">
    <h2 class="mb-4">Add a New Movie</h2>
    <form id="movieForm" @submit.prevent="saveMovie" enctype="multipart/form-data">
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input v-model="title" type="text" id="title" name="title" class="form-control" required />
      </div>

      <div class="form-group mb-3">
        <label for="description" class="form-label">Movie Description</label>
        <textarea v-model="description" id="description" name="description" class="form-control" required></textarea>
      </div>

      <div class="form-group mb-3">
        <label for="poster" class="form-label">Upload Poster</label>
        <input @change="handleFileUpload" type="file" id="poster" name="poster" class="form-control" accept="image/*" required />
      </div>

      <button type="submit" class="btn btn-primary">Submit</button>

      <div v-if="successMessage" class="alert alert-success mt-3">
        {{ successMessage }}
      </div>

      <div v-if="errors.length" class="alert alert-danger mt-3">
        <ul>
          <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
        </ul>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const title = ref('')
const description = ref('')
const poster = ref(null)
const successMessage = ref('')
const errors = ref([])
const csrf_token = ref('')

function handleFileUpload(event) {
  poster.value = event.target.files[0]
}

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then(response => response.json())
    .then(data => {
      console.log("CSRF Token received:", data)
      csrf_token.value = data.csrf_token
    })
    .catch(err => {
      console.error("Failed to fetch CSRF token", err)
    })
}

onMounted(() => {
  getCsrfToken()
})

function saveMovie() {
  successMessage.value = ''
  errors.value = []

  if (!poster.value) {
    errors.value.push('Please upload a movie poster.')
    return
  }

  const formData = new FormData()
  formData.append('title', title.value)
  formData.append('description', description.value)
  formData.append('poster', poster.value)

  fetch('/api/v1/movies', {
    method: 'POST',
    body: formData,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
    .then(response => response.json())
    .then(data => {
      if (data.errors) {
        errors.value = data.errors
      } else {
        successMessage.value = data.message
        title.value = ''
        description.value = ''
        poster.value = null
        document.getElementById('poster').value = ''
        getCsrfToken() // Refresh CSRF token after successful submission
      }
    })
    .catch(error => {
      console.error(error)
      errors.value.push("An unexpected error occurred.")
    })
}
</script>

<style scoped>
.container {
  max-width: 600px;
}
</style>

