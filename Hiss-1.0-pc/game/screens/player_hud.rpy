screen player_hud:

    imagebutton:
        align(0.0, 0.0)
        auto "/images/bag %s.png"
        action [ToggleScreen("player_hud"), Show("player_inventory")]
        at transform:
            xysize(175,175)