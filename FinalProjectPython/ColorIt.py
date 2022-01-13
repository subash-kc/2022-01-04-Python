from builtins import print

colors = {
    'red'    : (245, 90 , 66 ),
    'yellow' : (245, 252, 71 ),
    'green'  : (92 , 252, 71 ),
    'blue'   : (71 , 177, 252),
    'orange' : (200, 100, 0  ),
    'purple' : (130, 80 , 200),
    'white'  : (255, 255, 255),
}

def color(text, rgb):
    return f"\033[38;2;{str(rgb[0])};{str(rgb[1])};{str(rgb[2])}m{text}\033[0m"

class print():
    __init__ = print

def add_function(colour):
    def func(*text, end=None):
        text = [*text]
        last = len(text)-1
        final = end
        for i, t in enumerate(text):
            print(
                color(t, colors[colour]),
                end = ((i < last) and ' ') or final
            )
    func.__name__ = colour
    setattr(print, colour, func)

for fn in colors:
    add_function(fn)