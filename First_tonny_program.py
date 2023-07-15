"""
Simple example code for pygal, use to test installation
"""

import pygal
pygal.Bar()(1,3,5,6)(2,3,4,6).render_to_file("pygal_test.svg")