## Main Menu screen ############################################################


transform transform_main_menu_bg_zoomin:
    zoom 1.0
    anchor (0.5, 0.5)
    align (0.5, 0.5)
    easein2 1.0 zoom 1.1

transform transform_main_menu_button:
    zoom 0.5
    pos (100, 100)
    anchor (0.5, 0.5)
    on idle:
        linear 0.2 zoom 1.0
    on start:
        xpos -100
        easein2 1 xpos 50
    on hover:
        zoom 1.0
        bop_in_time_warp 0.2 zoom 1.1
