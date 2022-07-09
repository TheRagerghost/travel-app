<template>
  <div>

    <h1 class=" font-bold">{{profile.user.first_name}} - {{profile.user.username}}</h1>
    <h1 class=" pb-8">{{profile.user.email}}</h1>

    <div class="max-w-none mx-auto" v-if="profile.bookings"> 
        <div class="bg-white overflow-hidden shadow sm:rounded-lg">
          <ul role="list" class="divide-y divide-gray-200">
              <li v-for="index in profile.bookings" :key="bkng_list">
                <div class="block">
                  <div class="px-4 py-4 sm:px-6">
                    <div class="flex items-center justify-between">
                      <div class="text-sm font-medium text-indigo-600 truncate">
                        Booked tour: {{store.getTourById(index.tour).title}}
                      </div>
                      <div class="ml-2 flex-shrink-0 flex">
                        <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                          Status: {{index.status}}
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
          </ul>
        </div>
  </div>
  </div>
</template>

<script setup>
import { mainStore } from '~/store/storage'

const store = mainStore()

var usrId = store.currUsr

var { data: profile, refresh } = await useFetch(store.apiBaseUrl + store.users[usrId].link)

</script>