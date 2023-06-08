# Copyright (c) 2023, twiinIT - All Rights Reserved
# twiinIT proprietary - See licence file packaged with this code

from cosapp.systems import System

from tube.systems.tube import TubeAero, TubeGeom, TubeMech


class Tube(System):
    """tube model.

    Inputs
    ------
    fl_in: FluidPort
        inlet fluid

    Outputs
    -------
    fl_out: FluidPort
        exit fluid
    """

    def setup(self):
        # Physics
        self.add_child(TubeGeom("geom"), pulling=["d_in", "d_exit", "length"])
        self.add_child(TubeMech("mech"), pulling=["d_in", "d_exit"])
        self.add_child(TubeGeom("geom_hot"))
        self.add_child(TubeAero("aero"), pulling=["fl_in", "fl_out"])

        # connections
        self.connect(
            self.mech.outwards, self.geom_hot.inwards, {"d_hot_in": "d_in", "d_hot_exit": "d_exit"}
        )
        self.connect(self.geom_hot.outwards, self.aero.inwards, ["area_in", "area_exit"])
        self.connect(self.aero.outwards, self.mech.inwards, ["ps_in", "ps_exit"])
