import csdl

from src.utils.data2csv import create_csv
from src.caddee.concept.geometry.geometry import Geometry

# from modopt.scipy_library import SLSQP
from modopt.snopt_library import SNOPT
from modopt.csdl_library import CSDLProblem



# FROM THE CADDEE REPO
from src.caddee.concept.geometry.geometry import Geometry
from src.caddee.concept.geometry.geocore.component import Component
from src.caddee.concept.geometry.geocore.utils.create_thrust_vector_origin_pair import generate_origin_vector_pair
from src.caddee.concept.geometry.geocore.utils.generate_corner_points import generate_corner_points
from src.caddee.concept.geometry.geocore.utils.generate_camber_mesh import generate_camber_mesh
from src.caddee.concept.geometry.geocore.utils.thrust_vector_creation import generate_thrust_vector



from geometry_files.both_wings_all_nacelles_tiltwing_geometry_points import both_wings_all_nacelles

import python_csdl_backend
import numpy as np
from vedo import Points, Plotter
import cProfile


pointsets = both_wings_all_nacelles()

print('hi')