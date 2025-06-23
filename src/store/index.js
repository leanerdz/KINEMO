import { createStore } from 'vuex'

export default createStore({
  state: {
    dest: '',
    number: 0,
    name: '',
    message: '',
    displayHome: false,
    displayDestChosen: false,
    displayRecord: false,
    displayListen: true,
    displaySend: false,
    displayReceived: false,
  },
  getters: {
  },
  mutations: {
    setDest(state, payload) {
      state.dest = payload;
    },
    setNumber(state, payload) {
      state.number = payload;
    },
    setName(state, payload) {
      state.name = payload;
    },
    setMessage(state, payload) {
      state.message = payload;
    },
    setDisplayHome(state, payload){
      state.displayHome = payload
      state.displayDestChosen = false;
      state.displaySend = false;
      state.displayRecord = false
      state.displayListen = false;
      state.displayReceived = false

    },
    setDisplayDestChosen(state, payload) {
      state.displayDestChosen = payload;
      state.displayHome = false
      state.displaySend = false;
      state.displayRecord = false
      state.displayListen = false;
      state.displayReceived = false

    },
    setDisplayRecord(state, payload) {
      state.displayRecord = payload;
      state.displayHome = false
      state.displayListen = false
      state.displayDestChosen = false
      state.displaySend = false;
      state.displayReceived = false


    },
    setDisplayListen(state, payload) {
      state.displayListen = payload;
      state.displayHome = false
      state.displayRecord = false
      state.displayDestChosen = false
      state.displaySend = false;
      state.displayReceived = false


    },
    setDisplaySend(state, payload) {
      state.displaySend = payload;
      state.displayHome = false
      state.displayRecord = false
      state.displayDestChosen = false
      state.displayListen =  false
      state.displayReceived = false

    },
    setDisplayReceived(state, payload) {
      state.displaySend = false;
      state.displayHome = false
      state.displayRecord = false
      state.displayDestChosen = false
      state.displayListen =  false
      state.displayReceived = payload

    },

  },
  actions: {
  },
  modules: {
  }
})
