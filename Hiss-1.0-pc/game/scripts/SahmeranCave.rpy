label Before_Sahmeran:

    scene bg_caveinterior2 with dissolve

    show Side Idris Idle at left with dissolve
            
    menu:
        "This dark road could be a shortcut.":

            stop music fadeout 5.0

            hide screen player_hud with dissolve

            hide Side Idris Idle with dissolve
            
            stop music fadeout 1.0
            
            window hide

            scene bg_idrisfall with dissolve

            pause(10)

            scene black with dissolve
            
            centered "{font=BerkshireSwash-Regular.ttf}{size=*1.5}You fell into a hole and couldn't find a way out. Hoping someone would come looking for you, you waited, but no one came. Left to perish, abandoned to your fate, you died.{/size}{/font}" with dissolve

            return

        "Keep moving towards the light.":
            stop music fadeout 1
            hide Side Idris Idle with dissolve
            jump Sahmeran_Cave
            return

label Sahmeran_Cave:

    play music "sahmeran_cave.mp3" fadein 5.0

    scene bg_sahmerancave with dissolve
    
    show Idris Idle at center with dissolve

    Idris "Finally I've reached somewhere."

    hide screen player_hud with dissolve

    hide Idris Idle with dissolve

    scene bg_sahmerandark0 with dissolve
    pause(2)
    scene bg_sahmerandark1 with dissolve
    pause(2)
    scene bg_sahmerandark2 with dissolve
    pause(2)
    scene bg_sahmerandark3 with dissolve
    pause(2)

    scene bg_sahmerancave with dissolve

    show Idris Idle at left with moveinleft

    show Sahmeran Idle at right with dissolve

    play sound "Sahmeran_Tssss.mp3" volume 1.0 fadein 1

    Sahmeran "{i}{color=#CCD1D1}Tssssssssssssss...{/i}{/color}"

    stop sound fadeout 1.0

    show Idris Idle Shock at left with dissolve

    Idris "Allah!! What is that noise?"
    Sahmeran "With what audacious boldness dare you invade my cave?"
    Idris "Allahu akbar!! Who's speaking?"
    Sahmeran "The ruler of serpents, the great healer of all, for not all eyes to behold, Şahmeran."
    Idris "Hassiktir Lan! The myth was true!"
    Sahmeran "Myth!? Were you mortals questioning my existence?"
    Idris "How could anyone even imagine something like this?"

    hide Sahmeran Idle with dissolve

    show Idris Idle Smug at center with moveinright

    Idris "{i}{color=#CCD1D1}This woman will surely make me more money than the honey. I should get close with her.{/i}{/color}"

    hide Idris Idle with dissolve

    show Sahmeran Idle at center with dissolve

    Sahmeran "{i}{color=#CCD1D1}I wonder what this human tastes like. It certainly appears unappetizing, yet my curiosity compels me.{/i}{/color}" 
    
    hide screen player_hud with dissolve
   
    window hide
    
    scene black with dissolve

    show screen video_with_text("images/Snake_Animation.ogv", "{font=BerkshireSwash-Regular.ttf}{size=*2}Moments drift by...{/size}{/font}")

    pause(5.0)
    
    hide screen video_with_text

    scene bg_sahmerancave with dissolve

    show screen player_hud with dissolve

    show Idris Idle at left with dissolve

    show Sahmeran Idle at right with dissolve

    Sahmeran "İdris, do you know the tale? "

    Idris "What tale?"

    Sahmeran "The tale about me; "
    Sahmeran "{color=#f00}whoever feasts upon my head shall mend, whoever devours my body shall meet their end.{/color}"
    Sahmeran "{color=#f00}and whoever consumes my tail shall rise as a great healer.{/color}"

    Idris "So, what should I do with this information?"

    Sahmeran "My body's quite a marvel, you know, with plenty of tricks up its sleeve. My intellect, too, holds great depths." 
    Sahmeran "I could teach you a ton about the medical world."
    Sahmeran "Idris, are you resolved to stay here with me? If not, seize this opportunity to return to your home."

    menu:
        "You are a healer so I want to learn some things from you.":
            jump stayCave
            
        "Ahh I should go back to the village, this was never a good idea.":
            jump returnHome

    return
