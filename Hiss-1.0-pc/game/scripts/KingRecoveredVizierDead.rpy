label KingRecoveredVizierDead:

    stop music fadeout 5.0

    hide screen player_hud with dissolve
            
    hide Idris Idle with dissolve

    hide Vizier Idle with dissolve

    hide King Idle with dissolve

    window hide
    
    play sound "eating_meat.mp3" volume 0.5
    
    scene bg_kingeating with dissolve

    pause(10)

    play music "vizierandkingroom_music.mp3" fadein 2.0

    stop sound fadeout 2.0

    scene bg_kingroom with dissolve

    show screen player_hud with dissolve

    show Idris Idle With Hat at left with dissolve

    show Vizier Idle at center with dissolve

    show King Idle at right with dissolve

    King "I already feel much better. Well done to you, you saved my life! Anything you desire, just name it."

    Vizier "Aaaargh!"

    stop music fadeout 5.0

    hide screen player_hud with dissolve
    
    hide Vizier Idle with dissolve

    play sound "vomit.mp3" volume 10 fadein 2.0

    scene bg_viziervomit with dissolve

    pause(10)

    stop sound fadeout 2.0

    play music "vizierandkingroom_music.mp3" fadein 2.0

    scene bg_kingroom with dissolve

    show screen player_hud with dissolve

    show Idris Idle With Hat at left with dissolve

    show King Idle at right with dissolve

    King "What's happening to the vizier? What have you done to him?"

    Idris "Your Majesty, I haven't done anything." 
    Idris "As you can see, I have just returned from a long journey, and the meat might have spoiled along the way." 
    Idris "Please bring the doctors immediately."

    King "Forget about the doctors. You saved my life. A vizier means nothing to me compared to that. I can't thank you enough."

    Idris "It is my duty to serve you with all I got your majesty."

    stop music fadeout 5.0

    hide screen player_hud with dissolve

    hide Idris Idle With Hat with dissolve

    hide King Idle with dissolve

    scene black with dissolve

    centered "{font=BerkshireSwash-Regular.ttf}{size=*1.5}You saved the king and he really couldn't thank you enough. You also showed the vizier what you're made of!{/size}{/font}" with dissolve

    return
