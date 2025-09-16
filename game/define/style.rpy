## Main Menu screen ############################################################


style style_main_menu_button_text:
    align (0.5, 0.5)
    size 30
    color "#FFFFFF"
    font "SourceHanSansLite.ttf"
    bold True
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]

style style_config_menu_button_text:
    # xsize 200
    # ysize 60
    # anchor(0.5, 0.5)
    # align (0.5, 0.5)
    size 30
    color "#FFFFFF"
    hover_color "#003357"
    selected_color "#AAAAAA"
    insensitive_color "#444444"
    background Solid("#4A86E8")        # 正常状态背景色
    hover_background Solid("#3C78D8")   # 悬停状态背景色[citation:4]
    selected_background Solid("#6D9EEB")
    insensitive_background Solid("#CCCCCC")
    outlines [ (1, "#000000DD", 1, 1) ]
    