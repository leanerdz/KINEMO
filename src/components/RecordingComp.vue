<template>
    <div v-if="displayRecord"> 
        <div id="content">
            <div id="textCont">
                <p id="text">Parlez maintenant...</p>
                <div id="buttonCont">
                    <img id="bouton" src="../../public/img/assets/bouton1.gif" alt="">
                    <p id="text2">Appuyez sur le bouton vert pour arreter l'enregistrement.</p>
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
              
            }
        },
        computed: {
            ...mapState(['displayRecord'])
        },
        methods: {
        }, 
        created() {
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
    #bouton{
        margin-top: 0px;
        width: 500px;
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
        margin-left: 10px;
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
        margin-top: 0px;

    }
    </style>
      