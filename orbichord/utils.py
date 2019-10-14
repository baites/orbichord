
from IPython.core.display import display, HTML, Javascript
from IPython.display import Image, Audio
import json
from midi2audio import FluidSynth
import os
import random
import uuid


def showMusicXML(xml):
    """Show music xml using javascript.

    References
    ----------
        https://notebooks.azure.com/OUsefulInfo/projects/gettingstarted/html/4.1.0%20Music%20Notation.ipynb
    """
    DIV_ID = "OSMD-div-"+str(random.randint(0,1000000))
    msg='loading OpenSheetMusicDisplay'
    msg=''
    display(HTML('<div id="'+DIV_ID+'">{}</div>'.format(msg)))
    script = """
    console.log("loadOSMD()");
    function loadOSMD() {
        return new Promise(function(resolve, reject){

            if (window.opensheetmusicdisplay) {
                console.log("already loaded")
                return resolve(window.opensheetmusicdisplay)
            }
            console.log("loading osmd for the first time")
            // OSMD script has a 'define' call which conflicts with requirejs
            var _define = window.define // save the define object
            window.define = undefined // now the loaded script will ignore requirejs
            var s = document.createElement( 'script' );
            s.setAttribute( 'src', "https://cdn.jsdelivr.net/npm/opensheetmusicdisplay@0.7.1/build/opensheetmusicdisplay.min.js" );
            s.onload=function(){
                window.define = _define
                console.log("loaded OSMD for the first time",opensheetmusicdisplay)
                resolve(opensheetmusicdisplay);
            };
            document.body.appendChild( s ); // browser will try to load the new script tag
        })
    }
    loadOSMD().then((OSMD)=>{
        console.log("loaded OSMD",OSMD)
        var div_id = "{{DIV_ID}}";
            console.log(div_id)
        window.openSheetMusicDisplay = new OSMD.OpenSheetMusicDisplay(div_id);
        openSheetMusicDisplay
            .load({{data}})
            .then(
              function() {
                console.log("rendering data")
                openSheetMusicDisplay.render();
              }
            );
    })
    """.replace('{{DIV_ID}}',DIV_ID).replace('{{data}}',json.dumps(xml))
    display(Javascript(script))
    return DIV_ID


def renderWithJS(stream):
    """Show a using javascript.

    References
    ----------
        https://notebooks.azure.com/OUsefulInfo/projects/gettingstarted/html/4.1.0%20Music%20Notation.ipynb
    """
    xml = open(stream.write('musicxml')).read()
    showMusicXML(xml)


def renderWithLily(stream):
    """Render LilyPond in Jupyter notebook."""
    return Image(filename=str(stream.write('lily.png')))


def playAudio(stream):
    """Generate audio play from stream."""
    midi = stream.write('midi')
    fs = FluidSynth('/usr/share/soundfonts/FluidR3_GM.sf2')
    filename = 'audio-{}.wav'.format(uuid.uuid4().hex)
    fs.midi_to_audio(midi, filename)
    audio = Audio(filename=filename)
    os.remove(filename)
    return audio
