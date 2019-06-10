# bch_code.py
# Copyright (2014) Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000, there is a non-exclusive license for use of this
# work by or on behalf of the U.S. Government. Export of this program
# may require a license from the United States Government.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import os, bitstring, random, math
import subprocess

from bchlib import BCH

from .bitstringutils import *

class bch_code(object):
    """An error-correcting class"""
    
    def __init__(self, first_measurement, gen_poly=0x25AF, bit_strength=32):
        """A function to enroll the PUF with the error corrector object and
        generate helper data for subsequent regeneration"""
        self.codec = BCH(gen_poly, bit_strength)
        self.bit_strength = bit_strength
        self.helper_data = self.codec.encode(first_measurement.bytes)
    
    def regenerate(self, response):
        n_err_detected, corrected, _ = self.codec.decode(response.bytes, self.helper_data)
        return bitstring.Bits(bytes=corrected)
