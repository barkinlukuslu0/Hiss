label Honey_Cave:

    scene bg_caveinterior3 with dissolve

    show Side Idris Idle at left with dissolve

    play sound "audio/Bee Buzzing Right.mp3" volume 1 fadein 1.0

    menu:
        "This dark road could be a shortcut.":

            stop music fadeout 5.0

            hide screen player_hud with dissolve

            hide Side Idris Idle with dissolve
            
            stop sound fadeout 1.0
            
            window hide

            scene bg_idrisfall with dissolve

            pause(10)

            scene black with dissolve
            
            centered "{font=BerkshireSwash-Regular.ttf}{size=*1.5}You fell into a hole and couldn't find a way out. Hoping someone would come looking for you, you waited, but no one came. Left to perish, abandoned to your fate, you died.{/size}{/font}" with dissolve

            return

        "Keep moving towards the sound.":
            stop sound fadeout 1.0
            
            jump FoundHoney

label FoundHoney:

    scene bg_honeycave with dissolve:
        zoom 0.5

    show Idris Idle at left with dissolve

    Idris "I found the honey. I should get as much as I can and get out."

    hide Idris Idle with dissolve

    stop music fadeout 1.0

    play music "background_music.mp3" fadein 2.0

    scene bg_village with dissolve

    show Memed Idle at left with dissolve

    show Idris Idle at center with dissolve

    show Ahmed Idle at right with dissolve

    Idris "Hey cowards. I got the honey."

    Ahmed "Wait, how…"

    Memed "Sush… What do you mean, how? This was what we were planning all along." 

    show Memed Smug at left

    Memed "Well done İdris, we're going to make a lot of money!"

    show Memed Idle at left

    Idris "Let's go and sell this at the village."

    hide Memed Idle with dissolve

    hide Idris Idle with dissolve

    hide Ahmed Idle with dissolve

    scene bg_villagecenter with dissolve

    show Memed Idle at left with dissolve

    show Idris Idle No Axe at center with dissolve

    show Ahmed Idle at right with dissolve

    Memed "Here's your money kardeş."

    menu:
        "Is this all that you got for me? ":
            jump KillFriend

        "Eyvallah":
            jump StaySilend
    
    
    label KillFriend:

        show Idris Angry at center
    
        Idris "I entered that dreadful cave, where there could be a monster lurking, all for the sake of a little money."

        show Memed Smug at left

        Memed "Well, there's nothing to do. Thank Allah for even this. Some couldn't find it at all."

        Idris "Don't get on my nerves Memed. Give me more, let's call it a day."
         
        Idris "I'm the one doing the most work, why do you get a bigger share?!"

        Memed "Because I said so. What will happen if you get on your nerves kardeş?"

        show Memed Idle at left

        Idris "Don't force me into things I don't want to do. Are you going to give me a bigger share or not?"

        Memed "What will you do you coward?"
         
        Memed "If we didn't want to put you in danger, we wouldn't have sent you into the cave in the first place."

        Memed "Do you think we care about you? Take your money, and get out."

        show Idris Idle No Axe at center

        Idris " And I'm out here thinking that you are my friends… So be it. I won't let you get away with this."

        hide screen player_hud with dissolve

        hide Memed Idle with dissolve

        hide Idris Idle No Axe with dissolve

        hide Ahmed Idle with dissolve

        window hide
    
        scene black with dissolve

        show screen video_with_text("images/Snake_Animation.ogv", "{font=BerkshireSwash-Regular.ttf}{size=*2}Night falls.{/size}{/font}")

        pause(5.0)
    
        hide screen video_with_text

        play music "Night.mp3" volume 3 fadein 2.0

        scene bg_villagenight with dissolve

        show screen player_hud with dissolve

        show Idris Idle at center with dissolve

        show Memed Smug at left with dissolve
        
        show Ahmed Idle at right with dissolve

        Memed "Oh, look who came back crawling? What do you have to say now, sucker?"

        stop music fadeout 5.0

        hide screen player_hud with dissolve

        hide Memed Idle with dissolve

        hide Ahmed Idle with dissolve

        hide Idris Idle with dissolve

        scene black with dissolve

        play sound "chopping_meat.mp3"

        pause(2.5)

        stop sound

        scene bg_villagenight with dissolve

        show Idris Blood2 at center with dissolve

        pause(5)

        jump KillFriendEnd

label StaySilend:

    Idris "May Allah grant you plenty."
    
    stop music fadeout 5.0

    hide screen player_hud with dissolve

    hide Memed Idle with dissolve

    hide Idris Idle with dissolve

    hide Ahmed Idle with dissolve

    window hide
    
    scene bg_woodcutscene1 with dissolve

    pause(2)

    play sound "audio/chopping-wood.mp3" volume 1 fadeout 1.0

    scene bg_woodcutscene2 with dissolve

    pause(2)

    stop sound

    scene black with dissolve

    pause(1.5)

    centered "{font=BerkshireSwash-Regular.ttf}{size=*1.5}The money you made from selling honey will sustain you for a while, but you must continue your wretched woodsman life.{/size}{/font}"

    return

label KillFriendEnd:
   
    window hide

    scene black with dissolve

    centered "{font=BerkshireSwash-Regular.ttf}{size=*1.5}You've murdered your friends. For what? Yet you don't feel bad about it at all. Let's hope the royals don't catch on to this.{/size}{/font}"

    return