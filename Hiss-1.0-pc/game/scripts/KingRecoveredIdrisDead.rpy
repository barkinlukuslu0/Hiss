label KingRecoveredIdrisDead:

    stop music fadeout 5.0

    hide screen player_hud with dissolve
            
    hide Idris Idle with dissolve

    hide Vizier Idle with dissolve

    hide King Idle with dissolve

    play sound "eating_meat.mp3" volume 0.5
    
    scene bg_kingeating with dissolve

    pause(10)

    stop sound fadeout 2.0

    play music "vizierandkingroom_music.mp3" fadein 2.0

    scene bg_kingroom with dissolve

    show screen player_hud with dissolve

    show Idris Idle With Hat at left with dissolve

    show Vizier Idle at center with dissolve

    show King Idle at right with dissolve

    King "I already feel much better. Well done to you, you saved my life! Anything you desire, just name it."

    Idris "Aaaargh!"

    stop music fadeout 5.0

    hide screen player_hud with dissolve

    hide Idris with dissolve

    play sound "vomit.mp3" volume 10 fadein 2.0

    window hide
    
    scene bg_idrisvomit with dissolve

    pause(10)

    stop sound fadeout 2.0

    scene black with dissolve

    centered "{font=BerkshireSwash-Regular.ttf}{size=*1.5}You fool of a peasant. Did you listen to Şahmeran with your butt? You died for devouring her body. Enjoy your time with Şahmeran on the other side.{/size}{/font}" with dissolve

    return