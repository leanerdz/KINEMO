<template>
    <div v-if="displaySend">
        <div id="content">
            <div id="textCont">
                <p id="text">Votre message a bien été envoyé !</p>             
            </div> 
        </div>
    </div>
    
    </template>
    
    <script>
import { mapMutations, mapState } from 'vuex'

    export default {
        name: 'App',
        data() {
            return {
                date: "",
                hour: '',
                destinataire: 'Emilie',
            }
        },
        computed: {
            ...mapState(['displaySend'])
        },
        methods: {
            ...mapMutations(['setDisplayReceived', 'setDisplayHome',]),
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
            setTimeout(() => {
                this.setDisplayHome(false)
                this.setDisplayReceived(true)
            },300000)
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
    
    body {
        margin: 0px;
    }
    
    #oiseau{
        position: absolute;
        width: 15%;
        top: 77%;
        left: 2%;
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
        width: 900px;
        display: flex;
        justify-content: center;
        align-items: center;
        align-content: center;
    }
    
    #text{
        font-family: "Puffin-black", sans-serif;
        font-size: 80px;
        color: #3D332A;
        margin: 0px;
    }
    
    </style>
      