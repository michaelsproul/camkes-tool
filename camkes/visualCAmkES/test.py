#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

from PyQt5 import QtWidgets

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../'))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from View.Graph_Widget import GraphWidget
from Model.AST_Model import ASTModel

def test(argv):
    # Create graph widget
    app = QtWidgets.QApplication(argv)
    graph = GraphWidget()
    graph.ast = ASTModel.get_ast("../")

    print ASTModel.find_instance(graph.ast.assembly.instances, "hello") is not None
    # find_component is not being tested because it is not used anywhere. However
    # there is no reason why find_component will fail to work, if everything else worked.

    print "visualCAmkES test passed"

if __name__ == '__main__':
    sys.exit(test(sys.argv))
