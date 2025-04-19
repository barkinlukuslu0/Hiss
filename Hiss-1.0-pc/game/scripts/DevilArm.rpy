image glowing_bag:
    "glowing_bag.png"
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.0
    repeat 5

label DevilArm:

    scene black with dissolve

    play sound "chopping_meat.mp3" volume 1.0

    pause(3)

    stop sound

    scene bg_villagenight with dissolve

    show Devil Without Arm at center with dissolve

    show screen DevilArm_screen with dissolve

    "You need to drag and drop this Devil's arm into your inventory."

    while not isArmTaken:
        "You need to drag and drop this devil arm into your inventory."
        show glowing_bag with dissolve:
            xysize(175,175)

    if isArmTaken == True:
        hide glowing_bag with dissolve
        jump DevilArmContinue
    
    label DevilArmContinue:
    
        Devil "Wow you're playing hard, I like it. A useless limb means nothing to me, I have lots." 
        Devil "I like your boldness so I will let you get away with it, but I won't be so nice again."

        Idris "Stop yapping old man."

        hide Devil Without Arm with dissolve
    
        show Idris Blood2 at center with dissolve

        Idris "Lastly, I have “One hand in honey one hand in oil.”." 
        Idris "Maybe I can find something in Memed's house I should go there and look."

        hide screen DevilArm_screen with dissolve

        hide Idris Blood2 with dissolve

        scene black with dissolve

        play sound "door_creak_2.mp3" volume 1.0 fadein 1.0

        pause(2)

        stop sound fadeout 1

        scene bg_idrisfriendhousewithoutblood with dissolve

        show screen player_hud with dissolve

        show Idris Blood2 at left with dissolve
        
        Idris "Wait, what… These bastards went in and took the honey? If they knew the way, why would they let me in?" 
        Idris "They've been scheming behind my back!"

        Memed "Mmmmh..."

        Idris "Rest well kardeş. This is the beginning of your eternal sleep."

        hide screen player_hud with dissolve

        scene black with dissolve

        play sound "chopping_meat.mp3" volume 1.0

        pause(1.5)

        stop sound

        scene bg_idrisfriendhouse with dissolve

        show screen player_hud with dissolve

        show Idris Blood3 at left with dissolve

        Idris "So, what was I here for?"

    menu:
        "The expensive honey from the cave can help us.":
            hide screen player_hud with dissolve
            jump TakeHoney

        "The oil can come in handy for us.":
            hide screen player_hud with dissolve
            jump TakeOil

