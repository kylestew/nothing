#%%
%load_ext helpers.ipython_cairo

from sketches import Sandbox

sketch = Sandbox(1920, 1080)
d = sketch.render()

sketch.ctx
