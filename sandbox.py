#%%
from geom.grid import Grid

grid_size = 8
cells = Grid(1, 1, grid_size, grid_size, padding=0.03).cells()


%load_ext helpers.ipython_cairo
from modules.render import Render
from modules.color import hex_to_rgba

CANVAS_SQUARE_SIZE = 900
PIXEL = 1.0 / CANVAS_SQUARE_SIZE
BACKGROUND = hex_to_rgba("#f9f8f4")
FOREGROUND = hex_to_rgba("#ec3636")

render = Render(CANVAS_SQUARE_SIZE, BACKGROUND, FOREGROUND)
render.remap(domain=(0, 1), range=(0, 1))
render.set_line_width(2.0 * PIXEL)

# render poly
for cell in cells:
    render.rect(cell.x, cell.y, cell.w, cell.h)
    # render.circle(cel, 0.5, 0.01)

render.ctx