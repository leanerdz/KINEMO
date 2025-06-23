<template>
    <div id="audio-recorder">
      <h1>Enregistrement et Transcription</h1>
      <button @click="recordAudio">Enregistrer</button>
      <button @click="transcribeAudio">Transcrire</button>
      <button @click="sayText">Dire quelque chose</button>
      <input v-model="textToSay" placeholder="Texte à dire">
      <button @click="vocalLettrer">Enregistrer la lettre</button>
      <div>
        <h2>Transcription:</h2>
        <p>{{ transcription }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'AudioRecorder',
    data() {
      return {
        textToSay: '',
        transcription: ''
      };
    },
    methods: {
      vocalLettrer(){
        this.recordAudio()
        this.transcribeAudio()
      },
      async recordAudio() {
        try {
          const response = await axios.post('http://127.0.0.1:5000/record', { duration: 2 });
          console.log(response.data.message)
        } catch (error) {
          console.error('Erreur lors de l\'enregistrement:', error);
        }
      },
      async transcribeAudio() {
        try {
          const response = await axios.post('http://127.0.0.1:5000/transcribe', { file_path: 'wisper/recorded_audio.wav' });
          this.transcription = response.data.transcription;
        } catch (error) {
          console.error('Erreur lors de la transcription:', error);
        }
      },
      async sayText() {
        try {
          const response = await axios.post('http://127.0.0.1:5000/say', { text: this.textToSay });
          console.log(response.data.message);
        } catch (error) {
          console.error('Erreur lors de la synthèse vocale:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  #audio-recorder {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }

  button{
    width: fit-content;
  }
  </style>
  