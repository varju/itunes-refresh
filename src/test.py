import eyeD3

tag = eyeD3.Tag()
tag.link("M:\\ipod\\loaded\\Arrogant Worms - Toast\\01 - Life on the Road.mp3", eyeD3.ID3_V2)

print "Tag: %s" % str(tag)


userTextFrames = tag.getUserTextFrames()
for frame in userTextFrames:
    print "Frame: %s: %s" % (frame.description, frame.text)
    
