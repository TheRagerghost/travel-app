<template>
  <div class="max-w-none mx-auto">
        <div class="bg-white overflow-hidden shadow sm:rounded-lg">
          <ul role="list" class="divide-y divide-gray-200">
            
              <li v-for="index in cities.results" :key="city_list">
                <div class="block">
                  <div class="px-4 py-4 sm:px-6">
                    <div class="flex items-center justify-between">
                      <div class="text-sm font-medium text-indigo-600 truncate">
                        {{index.name}}
                      </div>
                      <div class="ml-2 flex-shrink-0 flex">
                        <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                          {{index.country}}
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
          </ul>
          
  <div class="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200 sm:px-6">
    <div class="flex-1 flex justify-between sm:hidden">
      <a href="#" class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
        Previous
      </a>
      <a href="#" class="ml-3 relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
        Next
      </a>
    </div>
    <div class="hidden sm:flex-1 sm:flex sm:items-center sm:justify-between">
      <div>
        <p class="text-sm text-gray-700">
          Showing
          <!-- space -->
          <span class="font-medium">{{1 + (currPage - 1) * elPerPage}}</span>
          <!-- space -->
          to
          <!-- space -->
          <span class="font-medium">{{currPage * elPerPage <= cities.count ? currPage * elPerPage : cities.count}}</span>
          <!-- space -->
          of
          <!-- space -->
          <span class="font-medium">{{cities.count}}</span>
          <!-- space -->
          results
        </p>
      </div>
      <div>
        <nav class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px" aria-label="Pagination">
          <button @click="prevPage" class="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
            <span class="sr-only">Previous</span>
            <svg class="h-5 w-5" x-description="Heroicon name: solid/chevron-left" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd"></path>
            </svg>
          </button>
          
          <button
            v-for="index in Math.ceil(cities.count / elPerPage)"
            :key="index"
            @click="goTo(index)"
            :class="[index == currPage ? 'z-10 bg-indigo-50 border-indigo-500 text-indigo-600' : 'bg-white border-gray-300 text-gray-500 hover:bg-gray-50',
                                         'relative inline-flex items-center px-4 py-2 border text-sm font-medium',
                    ]">{{index}}</button>
          <button @click="nextPage" class="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
            <span class="sr-only">Next</span>
            <svg class="h-5 w-5" x-description="Heroicon name: solid/chevron-right" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"></path>
            </svg>
          </button>
        </nav>
      </div>
    </div>
  </div>

        </div>
      </div>
</template>

<script setup>
import { mainStore } from '~/store/storage'

const store = mainStore()

const currPage = ref(1)
var { pending, data: cities } = await useLazyAsyncData('cities', () => $fetch(store.apiBaseUrl + 'cities-pg/?page=' + currPage.value))
const elPerPage = 10
const maxElements = Math.ceil(cities.value.count / elPerPage)

const refresh = () => refreshNuxtData('cities')

function prevPage() {
    currPage.value--
    if (currPage.value < 1) currPage.value = 1
    refresh()
}

function nextPage() {
    currPage.value++
    if (currPage.value > maxElements) currPage.value = maxElements
    refresh()
}

function goTo(pg) {
    currPage.value = pg
    refresh()
}
</script>