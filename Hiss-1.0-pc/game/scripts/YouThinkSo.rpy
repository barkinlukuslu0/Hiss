image glowing_bag:
    "glowing_bag.png"
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.0
    repeat 5

label YouThinkSo:

    stop music fadeout 5.0

    hide screen player_hud with dissolve

    hide Idris Idle with dissolve

    hide Sahmeran Idle with dissolve

    scene black with dissolve

    play sound "chopping_meat.mp3"

    pause(2.5)

    stop sound

    scene bg_sahmerancave with dissolve

    play music "sahmeran_cave.mp3" fadein 2.0

    show screen player_hud with dissolve

    show Idris Blood3 at center with dissolve

    Idris "Finally beeeee! Now it's time to take these to the kingdom and collect my reward."

    hide screen player_hud with dissolve

    hide Idris Blood3 with dissolve

    show screen SahmeranBody_screen with dissolve

    show glowing_bag with dissolve:
        xysize(175,175)

    "First, drag its head into the inventory, then its body, and finally its tail."

    while not isBody1Taken:
        "First, drag its head into the inventory, then its body, and finally its tail."
        show glowing_bag with dissolve:
            xysize(175,175)

    while not isBody2Taken:
        "First, drag its head into the inventory, then its body, and finally its tail."
        show glowing_bag with dissolve:
            xysize(175,175)

    while not isBody3Taken:
        "First, drag its head into the inventory, then its body, and finally its tail."
        show glowing_bag with dissolve:
            xysize(175,175)

    if isBody1Taken == True, isBody2Taken == True, isBody3Taken == True:

        hide glowing_bag with dissolve

        hide screen SahmeranBody_screen with dissolve

        hide glowing_bag with dissolve

        hide Idris Blood1 with dissolve
        
        jump ContinueYouThinkSo

label ContinueYouThinkSo:

    stop music fadeout 5.0

    hide Idris Blood3 with dissolve

    play music "vizierandkingroom_music.mp3" volume 2 fadein 2.0

    scene bg_vizierroom with dissolve

    show screen player_hud with dissolve

    show Idris Idle No Axe at left with dissolve

    show Vizier Idle at right with dissolve

    Vizier "Oooooo, look who it is! Our beloved peasant. What did you bring us?"

    Idris "I've brought you Şahmeran to heal the king. So, my job here is done. What will you give me in return for this?"

    Vizier "Hooop, hold on a moment. Your job isn't done yet. You need to take these to the king." 
    Vizier "Then we can talk about your money."

    Idris "Don't you have any servants to do this?"

    Vizier "The king ordered that whoever powerful warrior slaughters Şahmeran should also take these to the king himself."
    Vizier "And unfortunately, in this situation, that warrior turned out to be a wretch like you."

    show Idris Angry at left with dissolve

    Idris "You're talking a bit too much, vizier!"

    show Vizier Angry at right

    Vizier "You're the one who's talking too much, you filthy peasant of Allah. You're facing a vizier here." 
    Vizier "Do as I say, and then the job will be done."

    show Idris Idle No Axe with dissolve

    Idris "Anyway, when the job's done, just give me my money, and let's call it a day."

    Vizier "Come on, let's get going already!"

    hide Idris Idle No Axe with dissolve

    hide Vizier Angry with dissolve

    scene bg_kingroom with dissolve

    show Idris Idle With Hat at left with dissolve

    show King Idle at right with dissolve

    King "So, you are the one who is brave enough to face Şahmeran and kill it."

    Idris "Correct, your majesty."

    King "I heard your name is İdris. Do you know the meaning of your name, young man?"

    Idris "I'm sorry but I don't."

    King "Idris means; a very knowledgeable person. You seem to embody the meaning of your name."

    Idris "Thank you, your majesty. It's very honorable to hear such things from you."

    King "Now, let's address the main issue. I'm very sick as you can see." 
    King "Trusting in your wisdom, I request that you provide me with my medicine."

    Idris "I have brought you your medicine, but there are other parts of Şahmeran as well." 
    Idris "As you can see, she is a very beneficial creature. The vizier might also find it useful."

    King "Very well then. Call the vizier to come as well. How generous you are." 
    King "You will be fully rewarded for this, wise man, don't worry."

    show Vizier Idle at center with dissolve

    menu:
        "Head -> King | Body  -> Vizier | Tail  -> İdris":
            $ remove_items_from_inventory(player_inventory, 3)
            hide screen player_hud with dissolve
            jump KingRecoveredVizierDead

        "Head -> King | Body  -> İdris | Tail  -> Vizier":
            $ remove_items_from_inventory(player_inventory, 3)
            hide screen player_hud with dissolve
            jump KingRecoveredIdrisDead

        "Head -> Vizier | Body  -> King | Tail  -> İdris":
            $ remove_items_from_inventory(player_inventory, 3)
            hide screen player_hud with dissolve
            jump KingDead
        

