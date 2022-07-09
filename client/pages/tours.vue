<template>
<div>
<div class="flex items-center justify-center pb-8">
  <h1 class="font-bold pr-8">Tours</h1>
  <span v-if="enabled" :key="l2h">Price low to high</span>
  <span v-if="!enabled" :key="h2l">Price high to low</span>
  <div class="py-16 pl-4">
    <Switch
      v-model="enabled"
      :key="price_switch"
      :class="enabled ? 'bg-teal-900' : 'bg-teal-700'"
      class="relative inline-flex h-[20px] w-[36px] shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75"
    >
      <span class="sr-only">Use setting</span>
      <span
        aria-hidden="true"
        :class="enabled ? 'translate-x-4' : 'translate-x-0'"
        class="pointer-events-none inline-block h-[16px] w-[16px] transform rounded-full bg-white shadow-lg ring-0 transition duration-200 ease-in-out"
      />
    </Switch>
  </div>
</div>
  

  <div class="max-w-none mx-auto">
        <div class="bg-white overflow-hidden shadow sm:rounded-lg">
          <ul role="list" class="divide-y divide-gray-200">
            
              <li v-for="index in store.tours" :key="tour_list">
                <div class="block">
                  <div class="px-4 py-4 sm:px-6">
                    <div class="flex items-center justify-between">
                      <div class="text-sm font-medium text-indigo-600 truncate">
                        {{index.title}}
                      </div>
                      <div class="ml-2 flex-shrink-0 flex">
                        <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                          ${{index.price}}
                        </span>
                      </div>
                    </div>
                    <div class="mt-2 flex justify-between">
                      <div class="sm:flex">
                        <div class="mr-6 flex items-center text-sm text-gray-500 text-ellipsis max-w-3xl" >
                          {{index.desc}}
                        </div>
                      </div>
                      <div class="flex items-center text-sm text-gray-500">
                        {{store.getCityById(index.from_city).name}} - {{store.getCityById(index.to_city).name}}
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
import { ref } from 'vue'
import { mainStore } from '~/store/storage'
import { Switch } from '@headlessui/vue'

const enabled = ref(false)

const store = mainStore()
store.sortToursByPrice()

watch(enabled, (newVal) => {
  store.sortToursByPrice(newVal)
  })
</script>