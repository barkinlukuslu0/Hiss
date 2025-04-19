label KingDead:

   stop music fadeout 5.0

   hide screen player_hud with dissolve

   hide Idris Idle with dissolve

   hide Vizier Idle with dissolve

   hide King Idle with dissolve

   window hide

   play sound "eating_meat.mp3" volume 0.5 fadein 2.0
    
   scene bg_kingeating with dissolve

   pause(10)

   stop sound fadeout 2.0

   play sound "vomit.mp3" volume 10 fadein 2.0

   scene bg_kingvomit with dissolve

   pause(10)

   stop sound fadeout 2.0

   scene bg_idrishead1 with dissolve

   pause(10)

   play sound "chopping_meat.mp3"

   scene bg_idrishead2 with dissolve

   pause(1)

   stop sound
   
   pause(9)

   play sound "cutting_head_part2.mp3"

   scene bg_idrishead3 with dissolve
   
   pause(10)

   scene black with dissolve

   centered "{font=BerkshireSwash-Regular.ttf}{size=*1.5}How did you manage to feed the king the wrong part? You couldn't do one thing right, you fool of a peasant. Enjoy your time with Şahmeran on the other side.{/size}{/font}" with dissolve
   
   return