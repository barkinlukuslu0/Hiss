label StuffsCorrect:

    Idris "I successfully made the medicine. Let me go and give it to the king so they won't need to rely on your head."

    Sahmeran "You have astonished me… Thank you for sparing my life, mortal. This act shall not be forgotten."

    Idris "Well, it's time for me to go now."

    Sahmeran "Farewell, İdris. May my serpents show you kindness."

    stop music fadeout 5.0

    hide Idris Idle with dissolve

    hide Sahmeran Idle with dissolve

    play music "vizierandkingroom_music.mp3" volume 2 fadein 2.0

    scene bg_vizierroom with dissolve

    show Idris Idle No Axe at left with dissolve

    show Vizier Idle at right with dissolve

    Idris "Selamın aleyküm vizier. I've heard that king is very sick."

    Vizier "Ve aleyküm selam. That's right peasant. It's an emergency so don't try wasting our time if you don't have a solution."

    Idris "I have the medicine right here."

    Vizier "Yeah right! As if a peasant like you would find a cure for such an illness."

    Idris "But you have no options left."

    Vizier "..."

    Vizier "We don't trust villagers with this stuff so give it to me and I'll have a taste first."
    
    Idris "Here you go."

    hide screen player_hud with dissolve

    hide Idris Idle No Axe with dissolve

    hide Vizier Idle with dissolve
   
    window hide
    
    scene black with dissolve

    show screen video_with_text("images/Snake_Animation.ogv", "{font=BerkshireSwash-Regular.ttf}{size=*2}Moments drift by...{/size}{/font}")

    pause(5.0)

    hide screen video_with_text

    show screen player_hud with dissolve

    scene bg_vizierroom with dissolve

    show Idris Idle No Axe at left with dissolve

    show Vizier Idle at right with dissolve

    Vizier "I'm not dead. The king needs something immediately so you can take it to him."

    hide Idris Idle No Axe with dissolve

    hide Vizier Idle with dissolve

    scene bg_kingroom with dissolve

    show Idris Idle With Hat at left with dissolve

    show King Idle at right with dissolve

    King "Well, there, peasant. I've heard that you might have my medicine."

    Idris "That's right your majesty. They tested it to find out if it was poisoned."

    King "Yeah, I know. I've tried everything already and nothing seems to work. There's no harm in trying."

    stop music fadeout 5.0

    hide screen player_hud with dissolve

    hide Idris Idle With Hat with dissolve

    hide King Idle with dissolve

    scene bg_kingmedicine with dissolve

    pause(3)

    scene black with dissolve

    centered "{font=BerkshireSwash-Regular.ttf}{size=*1.5}Vay vay. Guess you proved useful after all, peasant. You saved the king; he owes you his life.{/size}{/font}"

    return
