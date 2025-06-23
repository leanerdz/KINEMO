<template>
    <div v-if="displayListen">
        <div id="resetButt">
            <img id="butt1" class="bouton" src="../../public/img/assets/bouton3.gif" alt="">
            <p id="text3">Appuyez sur le bouton rouge pour annuler</p>
        </div>
        <div id="content">
            <div id="textCont">
                <p id="text">Réécoutez votre message...</p>
                <div id="buttonCont">
                    <div id="button">
                        <img id="butt2" class="bouton" src="../../public/img/assets/bouton2.gif" alt="">
                    </div>
                    <p id="text2">Appuyez sur le bouton blanc pour l'envoyer.</p>
                </div>              
            </div>
        
        </div>
    </div>
    
    </template>
    
    <script>
    import { mapState } from 'vuex'
    import axios from 'axios';
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
            ...mapState(['displayListen'])
        },
        methods: {
            async sayText(textToSay) {
                try {
                    const response = await axios.post('http://192.168.121.246:3000/say', { text: textToSay });
                    console.log(response.data.message);
                } catch (error) {
                    console.error('Erreur lors de la synthèse vocale:', error);
                }
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
   
            this.sound = new Audio("sample_src");
            console.log(this.date, this.hour)
            if(this.displayListen){
                this.sayText('Réecoutez votre message. Appuyez sur le bouton vert pour l envoyer ou sur le blanc pour l annuler')

            }
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

    #button{
        top: 230px;
        width:200px;
        height: 150px;
        position: absolute;
        display: flex;
        justify-content: center;
        align-items: center;
        align-content: center;
        overflow: hidden;
    }
    
    body {
        margin: 0px;
    
    }
    
    #oiseau{
        position: absolute;
        width: 15%;
        top: 76%;
        left: 2%;
    }
    .bouton{
        width: 10%;
        position: relative;
    }
    #butt2{
        width: 500px;
        position: relative;
        top: -50px;
    }                                                     
    #butt1{
        width: 200px;
        margin-top: -10px;
        left: 0px;
    }
    #textCont{
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        align-content: center;
    }
    #content{
        margin-left: 0px;
        display: flex;
        justify-content: center;
        align-items: center;
        align-content: center;
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
        position: relative;
        top: 150px;
        justify-content: center;
        width: 500px;
        font-family: "Puffin", sans-serif;
        font-size: 30px;
        color: #3D332A;
        margin: 0px;
    }
    #text3{
        justify-content: center;
        width: 300px;
        font-family: "Puffin", sans-serif;
        font-size: 35px;
        color: #3D332A;
        margin: 0px;
    }
    #resetButt{
        display: flex;
        position: absolute;
        /*left: 50px;*/
        top: 50px;
    }
    </style>
      