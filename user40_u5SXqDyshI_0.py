import simplegui

def draw_handler(canvas):
    
   canvas.draw_line((10, 20), (90, 20), 12, 'Red')
   canvas.draw_line((96, 14), (96, 100), 12, 'Blue')
   canvas.draw_line((96, 100), (-100, 100), 12, 'Green')


frame = simplegui.create_frame('Testing', 100, 100)
frame.set_draw_handler(draw_handler)
frame.start()