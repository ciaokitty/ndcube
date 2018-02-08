# -*- coding: utf-8 -*-
import pytest

import numpy as np

from ndcube import utils

def test_convert_item_to_sequence_items_error():
    with pytest.raises(TypeError):
        utils.sequence.convert_item_to_sequence_items('item')


def test_get_sequence_items_from_int_item():
    pass


def test_get_sequence_items_from_slice_item():
    pass


def test_get_sequence_items_from_tuple_item():
    pass


def test_slice_sequence():
    pass


def test_index_sequence_as_cube():
    pass


def test_convert_cube_like_item_to_sequence_items():
    pass



@pytest.mark.parametrize("test_input,expected", [
    ((5, np.array([8] * 4)), utils.sequence.SequenceSlice(0, 5)),
    ((8, np.array([8] * 4)), utils.sequence.SequenceSlice(1, 0)),
    ((20, np.array([8] * 4)), utils.sequence.SequenceSlice(2, 4)),
    ((50, np.array([8] * 4)), utils.sequence.SequenceSlice(3, 8)),
])
def test_convert_cube_like_index_to_sequence_slice(test_input, expected):
    assert utils.sequence._convert_cube_like_index_to_sequence_slice(
        *test_input) == expected


@pytest.mark.parametrize("test_input,expected",
                         [((slice(2, 5), np.array([8] * 4)),
                           [utils.sequence.SequenceSlice(0, slice(2, 5, 1))]),
                          ((slice(5, 15), np.array([8] * 4)), [
                              utils.sequence.SequenceSlice(0, slice(5, 8, 1)),
                              utils.sequence.SequenceSlice(1, slice(0, 7, 1))
                          ]), ((slice(5, 16), np.array([8] * 4)), [
                              utils.sequence.SequenceSlice(0, slice(5, 8, 1)),
                              utils.sequence.SequenceSlice(1, slice(0, 8, 1))
                          ]), ((slice(5, 23), np.array([8] * 4)), [
                              utils.sequence.SequenceSlice(0, slice(5, 8, 1)),
                              utils.sequence.SequenceSlice(1, slice(0, 8, 1)),
                              utils.sequence.SequenceSlice(2, slice(0, 7, 1))
                          ]), ((slice(5, 100), np.array([8] * 4)), [
                              utils.sequence.SequenceSlice(0, slice(5, 8, 1)),
                              utils.sequence.SequenceSlice(1, slice(0, 8, 1)),
                              utils.sequence.SequenceSlice(2, slice(0, 8, 1)),
                              utils.sequence.SequenceSlice(3, slice(0, 8, 1))
                          ])])
def test_convert_cube_like_slice_to_sequence_slices(test_input, expected):
    assert utils.sequence._convert_cube_like_slice_to_sequence_slices(
        *test_input) == expected


def test_convert_sequence_slice_to_sequence_item():
    pass


@pytest.mark.parametrize(
    "test_input,expected",
    [((slice(0, 10), 20), slice(0, 10, 1)),
     ((slice(0, 10, 2), 20), slice(0, 10, 2)),
     ((slice(None, 0, -1), 20), slice(20, 0, -1))
    ])
def test_convert_slice_nones_to_ints(test_input, expected):
    assert utils.sequence.convert_slice_nones_to_ints(*test_input) == expected
