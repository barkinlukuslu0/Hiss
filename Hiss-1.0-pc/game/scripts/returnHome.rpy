label returnHome:

    show Idris Idle at left with dissolve

    show Sahmeran Idle at right with dissolve

    Idris "I'm going back home. There's nothing worth for me to stay here."

    Sahmeran "Farewell İdris. It was nice to get to know a mortal."

    hide screen player_hud with dissolve

    hide Idris Idle with dissolve

    hide Sahmeran Idle with dissolve

    stop music fadeout 2.0

    window hide
    
    scene bg_woodcutscene1 with dissolve

    pause(2)

    play sound "audio/chopping-wood.mp3" volume 1 fadeout 1.0

    scene bg_woodcutscene2 with dissolve

    pause(2)

    stop sound

    scene black with dissolve

    pause(1.5)

    scene black with dissolve

    pause(1)

    play music "background_music.mp3" volume 1 fadein 2.0

    scene bg_idrishouse with dissolve

    show screen player_hud with dissolve

    show Idris Idle at left with dissolve

    show Messenger Idle at right with dissolve

    Messenger "Selamın aleyküm, the good folk of the village! I bring urgent news from the kingdom!"

    Idris "Ve aleyküm selam. What news ya bring, messenger?"

    Messenger "The order's been given! His Majesty, the king, calls all villagers to the baths at once."

    Idris "To the baths, you say? What could be the King's purpose in summoning us so?"

    Messenger "It ain't my place to guess, villager. Just gotta get the word out quickly."

    Idris "Very well, we shall follow the King's word. Thank you, messenger, for bringing the news."

    Messenger "May Allah guide you quickly to the baths, 'cause the King doesn't wait around."

    stop music fadeout 5.0

    hide Idris Idle with dissolve

    hide Messenger Idle with dissolve

    hide screen player_hud with dissolve

    play music "bath_music.mp3" fadein 2.0

    scene bg_bath with dissolve

    show screen player_hud with dissolve

    show Idris Idle No Axe at left with dissolve

    show BathAttendant Idle at right with dissolve

    BathAttendant "Strip, and be quick about it! We've got a whole village to check."

    Idris "Check what?"

    show BathAttendant Angry at right

    BathAttendant "You've been asking too much just strip. It is not your place to know."

    hide Idris Idle with dissolve

    hide BathAttendant Idle with dissolve

    play sound "Naked.mp3" volume 5

    show Idris Naked at center with dissolve

    BathAttendant "We found what we're looking for. Come on, grab him, and take him to the vizier, quick!"

    stop music fadeout 5.0

    hide BathAttendant Idle with dissolve

    hide Idris Naked with dissolve

    hide screen player_hud with dissolve

    play music "vizierandkingroom_music.mp3" volume 2 fadein 2.0

    scene bg_vizierroom with dissolve

    show screen player_hud with dissolve

    show Idris Idle No Axe at left with dissolve

    show Vizier Idle at right with dissolve

    Vizier "Well, well, to think a poor woodsman like you found Şahmeran." 
    Vizier "I wonder what else is going on in this village that we don't know about?"
    Vizier "Anyway, we need you to bring us Şahmeran, or tell us where it is."

    Idris "What do you need Şahmeran for, huh?"

    show Vizier Smug at right with dissolve

    Vizier "We're gonna cut up and eat it. Hahahahaha."

    show Idris Angry at left with dissolve

    Idris "You think you're funny? Tell me!"

    show Idris Idle No Axe at left with dissolve

    show Vizier Idle at right with dissolve

    Vizier "No, really. The king is very sick, and the only solution is for us to find Şahmeran. The king will eat it and recover."

    Idris "What the hell… Isn't there another way?"

    show Vizier Angry at right

    Vizier "You think you know it all, don't you? All the doctors in the kingdom searched for a solution, but no, no, no."

    Vizier "Are you going to bring us Şahmeran willingly, or do we have to go and take it by force?"

    Idris "What's in this for me?"

    Vizier "Oh, you cunning one. So, you want something for yourself too. The king is dying, you bastard." 
    Vizier "We'll give you a couple of coins, and that's it."

    show Idris Angry at left

    Idris "A couple of coins won't cut it. The king's life is at stake here, and if I bring you Şahmeran, the king will recover."

    Idris "You either pay me properly or you'll have to find Şahmeran yourselves."

    show Idris Idle No Axe at left with dissolve

    Vizier "So, you filthy peasant… You'll get what you want as soon as you bring it to us or tell us where it is."

    menu:
        "I'll get her myself.":
            jump BringSahmeran
            
        "I won't lift a finger for a tiny bit of money. Go get her yourselves.":
            jump DontBringSahmeran
