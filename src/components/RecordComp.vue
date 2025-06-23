<template>
<div v-if="displayDestChosen">
    <div id="content">
        <div id="textCont">
            <p id="text">Votre message sera envoyé a {{ dest }}</p>
            <div id="buttonCont">
                <div id="button">
                        <img id="butt2" class="bouton" src="../../public/img/assets/bouton1.gif" alt="">
                    </div>
                    <p id="text2">Appuyez sur le bouton vert pour commencer a parler.</p>

            </div>              
        </div>
       
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
            }
        },
        computed: {
            ...mapState(['dest','displayDestChosen'])
        },
        methods: {
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
        margin-top: 85px;
        width: 300px;
        position: relative;
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
        width: 900px;
        font-family: "Puffin-black", sans-serif;
        font-size: 80px;
        color: #3D332A;
        margin: 0px;
    }
    #text2{
        justify-content: center;
        position: relative;
        width: 600px;
        font-family: "Puffin", sans-serif;
        font-size: 40px;
        color: #3D332A;
        top: 200px;
    }
    </style>
      