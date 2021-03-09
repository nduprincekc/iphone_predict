import rotatescreen

screen = rotatescreen.get_primary_display()

s = screen.rotate_to(0)

print(s)
