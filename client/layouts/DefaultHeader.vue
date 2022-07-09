<!-- This example requires Tailwind CSS v2.0+ -->
<template>
    <nav class="backdrop-blur-md bg-white/50 h-20 shadow-md fixed top-0 left-0 right-0">
        <div class="max-w-7xl mx-auto min-h-full px-2 flex items-center justify-between">
            <div class="flex space-x-4 items-center justify-start">
                <NuxtLink
                    class="text-2xl font-bold text-zinc-800 cursor-pointer select-none"
                    to="/"
                >TraWell <span v-if="loggedUser.user.username != Null">|| {{loggedUser.user.username}}</span></NuxtLink>
            </div>
            <div class="flex space-x-4 items-center justify-end">
                <NuxtLink
                    v-for="item in navigation"
                    class="text-lg font-medium text-stone-800 cursor-pointer px-3 py-1 rounded-lg select-none hover:text-emerald-800"
                    active-class="text-white bg-emerald-500 hover:text-white cursor-default shadow-inner"
                    :to="item.href"
                >{{ item.name }}</NuxtLink>
            </div>
            <div class="flex space-x-4 items-center justify-end">
                <div class="w-64">
                    <Listbox v-model="selectedUsr">
                        <div class="relative">
                            <ListboxButton
                                class="relative w-full py-2 pl-3 pr-10 text-right text-lg font-medium text-stone-800 rounded-lg cursor-pointer group hover:text-emerald-800 focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-500"
                            >
                                <span class="block truncate select-none">{{ selectedUsr.title }}</span>
                                <span
                                    class="absolute inset-y-0 right-0 flex items-center pr-2 pointer-events-none"
                                >
                                    <SelectorIcon
                                        class="w-5 h-5 mx-1 text-zinc-800 group-hover:text-emerald-800"
                                        aria-hidden="true"
                                    />
                                </span>
                            </ListboxButton>

                            <Transition
                                leave-active-class="transition duration-100 ease-in-out"
                                leave-from-class="opacity-100"
                                leave-to-class="opacity-0"
                            >
                                <ListboxOptions
                                    class="absolute w-full mt-2 overflow-auto text-base bg-white rounded-lg max-h-72 shadow-md focus:outline-none sm:text-sm"
                                >
                                    <ListboxOption
                                        :value="users[users.length - 1]"
                                        as="div"
                                    >
                                        <NuxtLink
                                            type="button"
                                            :to="'/login'"
                                            class="cursor-pointer select-none relative py-3 pr-10 pl-4 w-full border-b-2 hover:bg-emerald-50"
                                        >
                                            <span
                                                class="block truncate text-right text-emerald-500 font-semibold"
                                            >Login user</span>
                                            <span
                                                class="absolute inset-y-0 right-0 flex items-center pr-2 text-emerald-500"
                                            >
                                                <PlusSmIcon
                                                    class="w-5 h-5 mx-1"
                                                    aria-hidden="true"
                                                />
                                            </span>
                                        </NuxtLink>
                                    </ListboxOption>
                                    <ListboxOption
                                        v-slot="{ active, selected }"
                                        v-for="(e, index) in users"
                                        :key="e.title"
                                        :value="e"
                                        as="template"
                                    >
                                        <li
                                            @click="goLink(index)"
                                            :class="[
                                                active ? 'text-white bg-emerald-500' : 'text-gray-900',
                                                'cursor-default select-none relative py-3 pr-10 pl-4',
                                            ]"
                                        >
                                            <span
                                                :class="[
                                                    selected ? 'font-semibold' : 'font-normal',
                                                    'block truncate text-right',
                                                ]"
                                            >{{ e.title }}</span>
                                            <span
                                                v-if="selected"
                                                :class="[
                                                    active ? 'text-white' : 'text-emerald-500',
                                                    'absolute inset-y-0 right-0 flex items-center pr-2 ',
                                                ]"
                                            >
                                                <CheckIcon class="w-5 h-5 mx-1" aria-hidden="true" />
                                            </span>
                                        </li>
                                    </ListboxOption>
                                </ListboxOptions>
                            </Transition>
                        </div>
                    </Listbox>
                </div>
            </div>
        </div>
    </nav>
</template>

<script setup>
import { ref } from 'vue';
import {
    Menu,
    MenuButton,
    MenuItem,
    MenuItems,
    Listbox,
    ListboxLabel,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
} from '@headlessui/vue'
import { BellIcon, MenuIcon, XIcon, PlusSmIcon } from '@heroicons/vue/outline'
import { CheckIcon, SelectorIcon } from '@heroicons/vue/solid'
import { mainStore } from '~/store/storage'

const navigation = [
    { name: 'Tours', href: '/tours' },
    { name: 'Cities', href: '/cities' },
    { name: 'Profile', href: '/profile' },
]

const store = mainStore()
const users = store.users
console.log(users[store.currUsr])

const selectedUsr = ref(users[store.currUsr])
var loggedUser = await store.loginUser(store.currUsr)

async function goLink(id) {
    loggedUser = store.loginUser(id)
    console.log(loggedUser)
}

</script>