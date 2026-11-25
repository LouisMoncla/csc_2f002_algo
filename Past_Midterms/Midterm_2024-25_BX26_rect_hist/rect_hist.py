# -*- coding: utf-8 -*-
"""
Given a histogram, find the largest area of a rectangle contained in the
histogram.
"""
import math

def rect_from_left(hist, i):
    """compute max area of a rectangle [i,j] for all j, in linear time"""
    pass


def rect_hist_brute(hist):
    """brute force solution"""
    pass

def expand_rect(hist, i, j, left, right, h):
    """expand rectangle [l:r] to the left or the right, update height"""
    pass

def best_from_middle(hist, i, j, m):
    """compute max area of a rectangle that includes bar at position m"""
    pass

def rect_hist_dac_aux(hist, i, j):
    """solve over interval [i,j)"""
    pass

def rect_hist_dac(hist):
    """divide-and-conquer solution"""
    return rect_hist_dac_aux(hist, 0, len(hist))
