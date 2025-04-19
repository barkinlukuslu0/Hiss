screen video_with_text(video_file, text):

    add Movie(size=(1920, 1080), play=video_file, loop=False) xpos 0.5 ypos 0.5 anchor (0.5, 0.5)
    
    text text:
        align (0.5, 0.8)