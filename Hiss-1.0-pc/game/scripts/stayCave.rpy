label stayCave:
    Sahmeran "Oh, splendid! Trust me, we're in for a grand time."

    hide screen player_hud with dissolve

    hide Idris Idle with dissolve

    hide Sahmeran Idle with dissolve

    window hide
    
    scene black with dissolve

    show screen video_with_text("images/Snake_Animation.ogv", "{font=BerkshireSwash-Regular.ttf}{size=*2}Moments drift by...{/size}{/font}")

    pause(5.0)
    
    hide screen video_with_text

    scene bg_sahmerancave with dissolve

    show screen player_hud with dissolve

    show Idris Idle at left with dissolve

    show Sahmeran Idle at right with dissolve

    Sahmeran "My serpents have informed me that the king's condition is dire." 
    Sahmeran "They whisper that the sole remedy is for me to sacrifice my own head for his recovery."

    Idris "Isn't there another way? "

    Sahmeran "I have imparted much wisdom to you during your stay. Do you believe there's another path to be found?"

    menu:
        "We can try making a medicine. So I can use Şahmeran for something else.":

            jump MakeMedicine

        "This is my time. If I take Şahmeran to the king he will vallahi give me a lot of money.":

            jump GiveSahmeranToKing
