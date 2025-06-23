<template>
  <div id="app">
    
    <img id="fond" src="../public/img/assets/fond.gif" alt="">
    <HomeComp/>
    <RecordComp/>
    <RecordingComp/>
    <ListenMessComp/>
    <SentComp/>
    <ReceivedComp/>
    <div @click="playVideo()" v-if="showVideo" id="video-container" >
      <video id="video" autoplay  playsinline @ended="onVideoEnded">
          <source src="../public/img/assets/video1.mp4" type="video/mp4">
          Your browser does not support the video tag.
      </video>
    </div>
 </div> 
  <!--<AudioRecorder/>-->
</template>

<script>
// import AudioRecorder from './components/AudioRecorder.vue';
import axios from 'axios';
import SentComp from './components/SentComp.vue';
import RecordingComp from './components/RecordingComp.vue';
import ListenMessComp from './components/ListenMessComp.vue';                                                                                                                         
import HomeComp from './components/HomeComp.vue';
import RecordComp from './components/RecordComp.vue';
import ReceivedComp from './components/ReceivedComp.vue';
import { mapState, mapMutations } from 'vuex'
//import store from './store';

export default {
  name: 'App',
  components: {
    HomeComp,
    RecordComp,
    RecordingComp,
    ListenMessComp,
    SentComp,
    ReceivedComp,
    /*AudioRecorder*/

  },
  data() {
    return {
      socket: null,
      messageInput: '',
      message: '',
      messages: [],
      messageReceived: false,
      textToSay: '',                                                        
      transcription: '',
      audioFile:"",
      destname: "",
      destNumber: '',
      srcname: '',
      srcMessage: '',
      showVideo: true,
    };
  },
  computed: {
    ...mapState(['displayHome','dest', 'number', 'name', 'message','displayDestChosen'])
  },
  methods: {
    ...mapMutations(['displayHome','setDest', 'setNumber', 'setName', 'setMessage', 'setDisplayReceived','setDisplayHome', 'setDisplaySend','setDisplayDestChosen', 'setDisplayRecord', 'setDisplayListen']),
    onVideoEnded() {
      this.showVideo = false;
      window.removeEventListener('click', console.log("Video played"))
    },
    playVideo() {
      this.showVideo = true;
      const videoElement = document.getElementById('video')
      this.$nextTick(() => {
          if (videoElement) {
              videoElement.play().catch(e => console.log(e));
          }
      });
    },
    async recordAudio() {
      try {
        const response = await axios.post('http://192.168.121.246:3000/record', { duration: 2 });
        console.log(response.data.file)
        this.audioFile = response.data.file
        //this.sendMessage(response.data.file)
      } catch (error) {
        console.error('Erreur lors de l\'enregistrement:', error);
      }
    },
    async startRecordAudio() {
      try {
        const response = await axios.post('http://192.168.121.246:3000/api/start-recording', { duration: 2 });
        console.log(response.data.file)
        this.audioFile = response.data.file
        //this.sendMessage(response.data.file)
      } catch (error) {
        console.error('Erreur lors de l\'enregistrement:', error);
      }
    },
    async stopRecordAudio() {
      try {
        const response = await axios.post('http://192.168.121.246:3000/api/stop-recording', { duration: 2 });
        console.log(response.data.file)
        this.audioFile = response.data.file
        //this.sendMessage(response.data.file)
      } catch (error) {
        console.error('Erreur lors de l\'enregistrement:', error);
      }
    },
    async sayText(textToSay) {
      try {
        const response = await axios.post('http://172.28.59.50:3000/say', { filepath: textToSay });
        console.log(response.data.message);
      } catch (error) {
        console.error('Erreur lors de la synthèse vocale:', error);
      }
    },
    async send() {
      try {
        // const formData = new FormData();
        // formData.append('audio', file);

        const response = await axios.post('http://192.168.121.246:3000/send-message', { phoneNumber: this.destNumber});
        console.log(response.data.message);
      } catch (error) {
        console.error('Erreur lors de l envoi des données:', error);
      }
    },
    async submitFile() {
      // if (file) {
      //   alert('Veuillez sélectionner un fichier.');
      //   return;
      // }

      const formData = new FormData();
      //formData.append('a                                                                                                                                   
      formData.append('phoneNumber', '+33768405719'); // Remplacez par le numéro de téléphone réel
      //let phoneNumber = {'phoneNumber':'+33768405719'}
      try {
        const response = await axios.post('http://192.168.121.246:3000/send-message', '+33768405719', {
          headers: {                                                                                                                                                            
            'Content-Type': 'multipart/form-data'
          }
        });
        console.log('Fichier envoyé avec succès:', response.data);
      } catch (error) {
        console.error('Erreur lors de l\'envoi du fichier:', error);
      }
    },

    connect() {
      this.socket = new WebSocket('ws://192.168.121.225:8081');
//ws://192.168.121.225:8081
//http://192.168.121.246:3000/
      this.socket.addEventListener('open', () => {
        console.log('Connecté au serveur WebSocket');
        const presentationMessage = {
          client_name: 'Kinmo'
        };
        this.socket.send(JSON.stringify(presentationMessage));
      });

      this.socket.addEventListener('message', (event) => {
        console.log('Message reçu du serveur:', event.data);
        let messageText = JSON.parse(event.data);
        let decriptedMessage = '0'
        console.log(decriptedMessage)
        if(messageText.src === 'button'){
          if (messageText.data === 'RECORD'){
           messageText = messageText.data
            this.setDisplayRecord(true)
            this.startRecordAudio()
          }
          if (messageText.data === 'STOP'){
            messageText = messageText.data
            this.sayText('./public/assets/sons/son2.mp3')
            this.setDisplayListen(true)
            this.stopRecordAudio()
          }
          if (messageText.data === 'RESET'){
            messageText = messageText.data
            this.sayText('Votre mesage a été annulé')
            this.setDisplayHome(true)
          }
          if (messageText.data === 'SEND'){
            messageText = messageText.data
            this.sayText('Votre mesage a été envoyé')
            this.setDisplaySend(true)
            this.submitFile()
          }
        }else if(messageText.src === 'User'){
          let nameData = JSON.parse(messageText.data)
            this.setDisplayDestChosen(true);
            this.sayText(`Votre mesage sera envoyé a ${nameData.name}`)

            console.log(messageText.data)
            if (nameData.name) {
              this.destname = nameData.name
              this.setDest(nameData.name);
            }
            if (nameData.phonenumber) {
              this.destNumber = nameData.phonenumber
              this.setNumber(nameData.phonenumber);

            }
            console.log('name', this.destname,'phone', this.destNumber)
        }else if(messageText.src === 'Backend'){
          // if (messageText.data === "RECEIVED") {
          //   this.setDisplayHome(false)
          // }
          let nameData = JSON.parse(messageText.data)
            this.setDisplayReceived(true);
            console.log(messageText.data)
            if (nameData.name) {
              this.srcname = nameData.name
              this.setName(nameData.name);
            }
            if (nameData.message) {
              this.srcMessage = nameData.message
              this.setMessage(nameData.message);

            }
            console.log('name', this.srcname,'phone', this.srcMessage)
        }
      });

      this.socket.addEventListener('close', () => {
        console.log('Déconnecté du serveur WebSocket');
      });

      this.socket.addEventListener('error', (event) => {
        console.error('Erreur WebSocket:', event);
      });
    },
    sendMessage(messageToSend) {
      if (this.socket && this.socket.readyState === WebSocket.OPEN) {
        let message = {
          src: 'Kinmo',
          dest: 'Kinmo', // Remplacez par le nom du client destinataire
          data: `${messageToSend}`
        };
        if(messageToSend.filename === "wisper/recorded_audio.wav"){
          message = {
          src: 'Kinmo',
          dest: 'Kinmo', 
          data: `${messageToSend}`
        };
        }
        this.socket.send(JSON.stringify(message));
        this.messageInput = '';
      } else {
        console.error('WebSocket n\'est pas connecté.');
      }
    }
  }, 
  created() {            
    this.sayText('./public/img/assets/sons/son2.mp3')

    //this.connect()
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  overflow: hidden;
  margin-top: -10px;
}
#video-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.8);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

#video {
    width: 100%;
    height: 100%;
    object-fit: contain;
}
#fond{
  width: 100%;
}
#LetterContainer{
  width: 100%;
  display: flex;
  justify-content: center;
}
#letterHeader{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2px;
}
#letter{
  width: 60%;
  height: 40%;
  border: 1px solid black;
  border-radius: 5px;
}
#entete{
  font-size: 100%;
}
#basDeLettre{
  display: flex;
  flex-direction: row-reverse;
}
</style>
