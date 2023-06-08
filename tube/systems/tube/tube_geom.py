# Copyright (c) 2023, twiinIT - All Rights Reserved
# twiinIT proprietary - See licence file packaged with this code

import numpy as np
from cosapp.systems import System


class TubeGeom(System):
    """A geom tube model.

    Inputs
    ------
    d_in[m]: float
        inlet diameter
    d_exit[m]: float
        exit diameter
    length[m]: float
        tube length
    Outputs
    -------
    area_in[m**2]: float
        inlet area flow section
    area_exit[m**2]: float
        exit area flow section
    """

    def setup(self):
        # inwards
        self.add_inward("d_in", 0.1, unit="m")
        self.add_inward("d_exit", 0.1, unit="m")
        self.add_inward("length", 1., unit="m")

        # aero
        self.add_outward("area_in", 0.1, unit="m**2")
        self.add_outward("area_exit", 0.1, unit="m**2")

    def compute(self):
        self.area_in = np.pi * self.d_in**2 / 4
        self.area_exit = np.pi * self.d_exit**2 / 4
