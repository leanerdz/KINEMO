<template>
    <div v-if="displayReceived">
        <!-- <div id="content">
            <div id="textCont">
                <p id="text">Vous avez reçu un message de {{ name }}</p>
                <p id="text2">{{ message }}</p>
                <div id="buttonCont">
                    <br>
                    <p id="text2">N'oubliez pas de le récupérer sur l'imprimante !</p>

                </div>              
            </div>
        
        </div> -->
        <div  v-if="showVideo2" id="video-container" @click="playVideo2()">
            <video id="video2" autoplay  playsinline @ended="onVideoEnded">
                <source src="../../public/img/assets/video2.mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
    </div>
    
    </template>
    
    <script>
    import { mapState } from 'vuex'
    export default {
        name: 'App',
        data() {
            return {
                date: "",
                hour: '',
                destinataire: 'Emilie',
                showVideo2: true,
            }
        },
        computed: {
            ...mapState(['displayReceived','name', 'message', 'displayReceived'])
        },
        methods: {
            onVideoEnded() {
                this.showVideo2 = false;
            },
            playVideo2() {
                this.showVideo2 = true;
                const videoElement = document.getElementById('video2')
                this.$nextTick(() => {
                if (videoElement) {
                    videoElement.play().catch(e => console.log(e));
                }
            });
            },
            getFormatedDate() {
                const date = new Date();
                const options = {
                    weekday: 'long',
                    year: 'numeric',
                    month: 'long',
                    day: 'numeric'
                };
                this.date = date.toLocaleDateString('fr-FR', options).toLocaleUpperCase();
            },
            getFormatedHour() {
                const date = new Date();
                const hours = date.getHours().toString().padStart(2, '0');
                const minutes = date.getMinutes().toString().padStart(2, '0');
                this.hour = `${hours}:${minutes}`;
            },
        }, 
        created() {
            this.getFormatedDate()
            this.getFormatedHour()
            console.log(this.date, this.hour)

        }
    };
    </script>
    
    <style>
    @font-face {
        font-family: "Puffin";
        src: url("../../public/img/assets/fonnts.com-Puffin.otf") format("opentype"),
    }
    @font-face {
        font-family: "Puffin-black";
        src: url("../../public/img/assets/fonnts.com-Puffin_Black.otf") format("opentype"),
    }
    @font-face {
        font-family: "Puffin-SemiBold";
        src: url("../../public/img/assets/fonnts.com-Puffin_Display_SemiBold.otf") format("opentype"),
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

#video2 {
    width: 100%;
    height: 100%;
    object-fit: contain;
}
    body {
        margin: 0px;
    
    }
    
    #oiseau{
        position: absolute;
        width: 15%;
        top: 77%;
        left: 2%;
    }
    .bouton{
        width: 10%;
        position: relative;
    }
    #butt2{
        margin-top: 100px;

    }
    #textCont{
        position: absolute;
        top: 30%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        align-content: center;
    }
    #content{
        display: flex;
        justify-content: center;
        align-items: center;
        align-content: center;
    }
    #date{
        font-family: "Puffin-SemiBold", sans-serif;
        font-size: 50px;
        color: #3D332A;
        margin: 0px;
    }
    #buttonCont{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    #text{
        font-family: "Puffin-black", sans-serif;
        font-size: 80px;
        color: #3D332A;
        margin: 0px;
    }
    #text2{
        justify-content: center;
        width: 600px;
        font-family: "Puffin", sans-serif;
        font-size: 40px;
        color: #3D332A;
        margin: 0px;
    }
    #text3{
        justify-content: center;
        width: 400px;
        font-family: "Puffin", sans-serif;
        font-size: 35px;
        color: #3D332A;
        margin: 0px;
    }
    #resetButt{
        display: flex;
        position: absolute;
        left: 50px;
    }
    </style>
      