"""
Module for testing method of NodeMethods class. 
Contains three classes. Each applies to a different method.
Also class contains tests that check output for three nodes:
    1.tree root
    2.intermediate node
    3.leaf
"""
import pytest
from tree import NodeMethods, init_example_tree

root = init_example_tree() # create sample tree for testing


class TestSum:
    """Class for testing sum method from NodeMethods class"""
    def test_one(self,):
        assert NodeMethods(root).sum() == 38
    def test_two(self):
        assert NodeMethods(root.children[0]).sum() == 10
    def test_three(self):
        assert NodeMethods(root.children[1].children[0]).sum() == 1

class TestAverage:
    """Class for testing average method from NodeMethods class"""
    def test_one(self):
        assert NodeMethods(root).average() == 3.8
    def test_two(self):
        assert NodeMethods(root.children[0]).average() == 10/3
    def test_three(self):
        assert NodeMethods(root.children[1].children[0]).sum() == 1

class TestMedian:
    """Class for testing median method from NodeMethods class"""
    def test_one(self):
        assert NodeMethods(root).median() == 4
    def test_two(self):
        assert NodeMethods(root.children[0]).median() == 3
    def test_three(self):
        assert NodeMethods(root.children[1].children[0]).median() == 1