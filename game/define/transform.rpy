## Main Menu screen ############################################################


transform transform_main_menu_bg_zoomin:
    zoom 1.0
    anchor (0.5, 0.5)
    align (0.5, 0.5)
    easein2 1.0 zoom 1.1

transform transform_confirm_bg_zoomin:
    zoom 1.1
    alpha 0.0
    anchor (0.5, 0.5)
    align (0.5, 0.5)
    easeout_circ 0.1 zoom 1.0 alpha 1.0

transform transform_main_menu_button():
    size (160, 80)
    anchor (0.5, 0.5)
    xpos -160
    on idle:
        linear 0.05 zoom 1.0 xoffset 0
    on hover:
        bop_in_time_warp 0.1 zoom 1.1 xoffset 20

transform transform_main_menu_button2(delay):
    on start:
        time delay
        bop_to_time_warp 0.5 xpos 200