import math
import pymesh
from AffineMatrix import AffineMatrix

unitBox = pymesh.generate_box_mesh([-1, -1, -1], [1, 1, 1])

slicerBox = pymesh.generate_box_mesh([-2, -2, -2], [2, 0, 2])

unitBox = AffineMatrix().rotateX(0.25 * math.pi).rotateZ(0.25 * math.pi).translate(0, 0.05, 0).dot(unitBox)

sliced = pymesh.boolean(unitBox, slicerBox, 'difference')

pymesh.save_mesh('output/sliced.stl', sliced)
