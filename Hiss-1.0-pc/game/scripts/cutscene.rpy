label cutscenes:
    window hide
    
    scene bg_woodcutscene1 with dissolve

    pause(2)

    play sound "audio/chopping-wood.mp3" volume 1 fadeout 1.0

    scene bg_woodcutscene2 with dissolve

    pause(2)

    stop sound

    scene black with dissolve

    pause(1.5)

    jump introduction 