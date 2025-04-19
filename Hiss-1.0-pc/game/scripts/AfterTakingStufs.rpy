label AfterTakingStuffs:

    play music "sahmeran_cave.mp3" fadein 2.0

    scene bg_sahmerancave with dissolve

    show screen player_hud with dissolve

    show Idris Blood3 at left with dissolve
    show Sahmeran Idle at right with dissolve

    Idris "I've gathered everything and now, I can return to the cave."

    Sahmeran "Ah, Idris, it seems you've finally arrived. Have you managed to understand the idioms?"
    
    Idris "I got some things, we'll see if it's right or not."

    $ remove_items_from_inventory(player_inventory, 3)

    hide screen player_hud with dissolve

    hide Idris Blood3 with dissolve

    hide Sahmeran Idle with dissolve

    window hide
    
    scene black with dissolve

    show screen video_with_text("images/Snake_Animation.ogv", "{font=BerkshireSwash-Regular.ttf}{size=*2}Idris works on making the medicine.{/size}{/font}")

    pause(5.0)
    
    hide screen video_with_text

    scene bg_sahmerancave with dissolve

    show screen player_hud with dissolve

    show Idris Blood3 at left with dissolve

    show Sahmeran Idle at right with dissolve

    if isFeetTaken == True and isLegTaken == True and isHoneyTaken == True:
        jump StuffsCorrect
    
    else:
        Idris "Damn it, I've gathered the items wrong! I can't make the medicine."

        show Sahmeran Angry at right

        Sahmeran "You worthless human. You can't do anything right, can you? Now what shall I do?!"
        
        jump GiveSahmeranToKing

    return