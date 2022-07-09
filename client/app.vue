<template>
  <div class=" bg-slate-100 min-h-screen relative">
    <NuxtLayout>
      <NuxtPage/>
    </NuxtLayout>
  </div>
</template>

<script setup>
import { mainStore } from '~/store/storage'

const store = mainStore()
await store.fetchTours()
await store.fetchCities()
</script>