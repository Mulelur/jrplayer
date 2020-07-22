//<![CDATA[
$(document).ready(function(){
    "use strict";
    new jPlayerPlaylist({
        jPlayer: "#musica-jquery-jplayer",
        cssSelectorAncestor: "#musica-audio-player-container"
    }, [
        { 
            title:"Rock boy", 
            artist:"<span class='music-time'></span>",
            mp3:"http://127.0.0.1:8000/media/songs/27034207_rb-chill-kit_by_deeflack92_preview.mp3",
            poster: "{% static 'home/img/gallery3.jpg' %}",
			
        },
        { 
            title:"JR-Pylare", 
            artist:"<span class='music-time'></span>",
            mp3:"http://127.0.0.1:8000/media/songs/04_.mp3",
            poster: "{% static 'home/img/gallery3.jpg' %}",
			
        }
        
    ], {
        playlistOptions: {
            autoPlay: false,
            loopOnPrevious: true,
            shuffleOnLoop: true,
            enableRemoveControls: true,
            displayTime: "show",
            freeItemClass: "jp-playlist-item-free",
        },
        swfPath: "js/jquery.jplayer.swf",
        supplied: "mp3",
        wmode: "window",
        useStateClassSkin: true,
        autoBlur: true,
        smoothPlayBar: true,
        keyEnabled: true,
        remainingDuration: true,
        volume: 1,
    });



});
//]]>
