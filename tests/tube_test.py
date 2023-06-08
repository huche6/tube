# Copyright (C) 2022-2023, twiinIT
# SPDX-License-Identifier: BSD-3-Clause

from cosapp.drivers import NonLinearSolver

from tube.systems import Tube


class TestTube:
    """Define tests for the tube model."""

    def test_system_setup(self):
        # default constructor
        sys = Tube("sys")

        data_input = ["fl_in"]
        data_output = ["fl_out"]
        data_inward = ["d_in", "d_exit", "length"]
        data_outward = []

        for data in data_input:
            assert data in sys.inputs
        for data in data_inward:
            assert data in sys.inwards
        for data in data_output:
            assert data in sys.outputs
        for data in data_outward:
            assert data in sys.outwards

    def test_run_once(self):
        sys = Tube("sys")

        sys.fl_in.W = 10.0
        sys.run_drivers()

        assert sys.fl_out.W == sys.fl_in.W

    def test_run_nls(self):
        sys = Tube("sys")

        sys.add_driver(NonLinearSolver('nls'))
        sys.run_drivers()

        assert sys.geom_hot.d_in > sys.geom_hot.d_exit
