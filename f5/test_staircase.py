'''
Created on Oct 4, 2015

@author: ljiang
'''
import pytest
from staircase import draw_staircase

@pytest.mark.parametrize('input', [6])
def test_draw_staircases(input):
    draw_staircase(input)