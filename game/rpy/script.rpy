define e = Character(None, image="eileen", kind=bubble) # 艾琳
define l = Character(None, image="lucy", kind=bubble)   # 露西



label start:

    scene bg library_morning
    with fade
    show wenxuan
    show test at right

    e "hello world"

    l "你好啊我的朋友"

    return