transform alpha_dissolve:
    alpha 0.0
    linear 0.05 alpha 1.0
    on hide:
        linear 0.05 alpha 0

screen countdown():
    timer 0.01 repeat True action If(time > 0, true = SetVariable('time', time - 0.01), false = [Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.7 xmaximum 300 at alpha_dissolve