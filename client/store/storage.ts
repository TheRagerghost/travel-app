import { defineStore } from 'pinia'

export const mainStore  = defineStore({
    id: 'main-store',
    state: () => {
      return {
        apiBaseUrl: 'http://localhost:8000/api/v1/',
        userList: [
            { title: 'No User', link: 'logout/' },
            { title: 'Evelin', link: 'login/?username=evelin57&password=iamuser'},
            { title: 'Roland', link: 'login/?username=roland80&password=iamuser'},
        ],
        selectedUser: 0,
        loggedUser : { title: 'No User', link: 'logout/' },
        tourList:[],
        cityList:[],

      }
    },
    actions: {
        setCurrUsr(id : number) {
            this.selectedUser = id
        },
        async fetchTours(){
            const {data:list} = await useFetch(this.apiBaseUrl + 'tours/')
            this.tourList = list
            return this.tourList
        },
        async fetchCities(){
            const {data:list, refresh} = await useFetch(this.apiBaseUrl + 'cities/')
            this.cityList = list
            return this.cityList
        },
        getCityById(id : number){
            return this.cityList.find((c: { id: number }) => c.id === id)
        },
        sortToursByPrice(h2l : Boolean = false){
            if(h2l)
                return this.tourList.sort((a: { price: number },b: { price: number })=> a.price - b.price)
            else
                return this.tourList.sort((a: { price: number },b: { price: number })=> b.price - a.price)
        },
        getTourById(id : number){
            var temp = this.tourList.find((c: { id: number }) => c.id === id)
            return temp
        },
        addUser(usrnm : string, psswrd : string){
            let r = (Math.random() + 1).toString(36).substring(7);
            this.userList.push({ title: usrnm, link: 'login/?username='+ usrnm +'&password=' + psswrd});
        },
        async loginUser(id : number){
            var {data: loggedUser} = await useFetch(this.apiBaseUrl + this.userList[id].link)
            this.selectedUser = id
            
            return loggedUser
        }
    },
    getters: {
        apiUrl: state => state.apiBaseUrl,
        users: state => state.userList,
        currUsr: state => state.selectedUser,
        loggedUsr: state => state.loggedUser,
        tours: state => state.tourList,
        cities: state => state.cityList,
    },
  })