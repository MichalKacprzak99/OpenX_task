from tree import Tree_methods
from tree import root
import pytest


class TestSum:
    def test_one(self,):
        assert Tree_methods(root).sum() == 38
    def test_two(self):
        assert Tree_methods(root.children[0]).sum() == 10
    def test_three(self):
        assert Tree_methods(root.children[1].children[0]).sum() == 1
class TestAverage:
    def test_one(self):
        assert Tree_methods(root).average() == 3.8
    def test_two(self):
        assert Tree_methods(root.children[0]).average() == 10/3
    def test_three(self):
        assert Tree_methods(root.children[1].children[0]).sum() == 1

class TestMediana:
    def test_one(self):
        assert Tree_methods(root).mediana() == 4
    def test_two(self):
        assert Tree_methods(root.children[0]).mediana() == 3
    def test_three(self):
        assert Tree_methods(root.children[1].children[0]).mediana() == 1