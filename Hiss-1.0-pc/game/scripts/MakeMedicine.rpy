label MakeMedicine:
    Sahmeran "So, you're not inclined to end me. Very well. The only risk lies in not attempting." 
    Sahmeran "However, it shall not transpire through the most ethical means." 
    Sahmeran "Are you prepared to forsake your moral compass?"

    Idris "I never really had morals."

    Sahmeran "I shall furnish you with idioms, and you must find them accordingly."
    Sahmeran "{color=#f00}Lay your feet according to your quilt.{/color}" 
    Sahmeran "{color=#f00}To break the devil's leg.{/color}"
    Sahmeran "{color=#f00}One hand in honey one hand in oil.{/color}"

    Idris "I will get out of the cave as soon as the night hits."

    stop music fadeout 5.0

    hide Sahmeran Idle with dissolve

    hide Idris Idle with dissolve

    hide screen player_hud with dissolve

    play music "Night.mp3" volume 3 fadein 2.0

    scene bg_villagenight with dissolve

    show screen player_hud with dissolve

    show Idris Idle at center with dissolve

    Idris "First thing on the list “Lay your feet according to your quilt.”."
    Idris "What does this mean?"
    Idris "I always believed as a child; that if your limbs are out of your quilt some bad thing can get to you in your sleep."
    Idris "I can go to the nearest house and see if someone's sleeping."

    hide Idris Idle with dissolve

    hide screen player_hud with dissolve

    scene black with dissolve

    play sound "door_creak_3.mp3" volume 1.0 fadein 1.0

    pause(2)

    stop sound fadeout 1

    scene bg_womanroomwithhandfeet with dissolve:
        zoom 0.5

    show screen player_hud with dissolve

    show Idris Idle at right with dissolve
    
    Idris "Exactly what I was looking for! Now which one should I take?"

    menu:
        "Take the old woman's feet.":

            hide screen player_hud with dissolve
            jump WomanFeet
            
        "Take the old woman's hand.":

            hide screen player_hud with dissolve
            jump WomanHand