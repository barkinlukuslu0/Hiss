label introduction:

    scene bg_village with dissolve

    play music "background_music.mp3" volume 1 fadein 5.0

    show screen player_hud with dissolve

    show Idris Idle at center with dissolve

    pause (1.5)

    show Idris Idle at left with moveinleft

    show Memed Idle at right with dissolve

    Memed "Ula İdris! Don't tell anyone this but we found the cave full of honey and it's gonna make a lot of money."

    Idris "Who's gonna go in there?"

    Memed "We haven't decided yet. It's by the end of the village we'll check it and decide what's gonna happen."

    Idris "Isn't that the cave the snake creature lives in?"

    Memed "It's a myth, don't believe that bullshit."

    Idris "I'm going to get my axe just in case."

    hide Memed Idle with dissolve

    hide Idris Idle with dissolve

    hide screen player_hud with dissolve

    window hide
    
    scene black with dissolve

    show screen video_with_text("images/Snake_Animation.ogv", "{font=BerkshireSwash-Regular.ttf}{size=*2}İdris continues working.{/size}{/font}")

    pause(5.0)
    
    hide screen video_with_text

    scene bg_village with dissolve
    
    show screen player_hud with dissolve

    show Memed Idle at left with dissolve

    show Ahmed Idle at right with dissolve

    Ahmed "Who's going to go in the cave?"

    show Memed Smug at left 

    Memed "We should make İdris go and we can leave him in the cave. No worries."
    Ahmed "Why would we leave him there though?"
    Memed "So, we can make more money of the honey genius."

    show Memed Idle at left

    show Idris Idle at center with dissolve

    Memed "So İdris, you are the youngest one. We discussed and decided that you should be the one who's going to go into the cave."

    show Idris Idle Smug at center

    Idris "What's that, are you guys scared?"

    show Idris Idle at center

    Memed "No, of course not. Since you are the woodsman; we know you are the best at using an axe among us."
    Memed "If the snake thing comes, we can't beat it."
    Idris "Okay, fair enough."

    stop music fadeout 5.0

    hide Memed Idle with dissolve

    hide Idris Idle with dissolve

    hide Ahmed Idle with dissolve

    scene bg_cave1 with dissolve

    play music "cave_sound.mp3" volume 5 fadein 1.0

    show Side Idris Idle at left with dissolve

    Idris "It's very dark, but I need to keep going."

    window hide

    scene bg_caveinterior1 with dissolve

    show Side Idris Idle at left with dissolve

    play sound "audio/Bee Buzzing Left.mp3" volume 1 fadein 1.0

    menu:
        "If I follow the sound of bees, I might find the cave.":
            stop sound fadeout 1.0
            hide Idris Idle with dissolve

            jump Honey_Cave

        "I wonder where is that light coming through in a cave.":
            stop sound fadeout 1.0 
            hide Idris Idle with dissolve

            jump Before_Sahmeran
