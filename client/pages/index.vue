<template>
  <h3>Cities:</h3>
  <li v-for="index in cities" :key="index">{{ index.name }}</li>
</template>

<script setup>
const { data: cities } = await useApiFetch('cities/')
</script>