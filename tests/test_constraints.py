import unittest

from isla.solver import ISLaSolver

from alhazen import Alhazen

from alhazen.helper import decision_tree_to_constraints

from alhazen_formalizations.calculator import initial_inputs, grammar_alhazen as grammar, prop
from alhazen.helper import show_tree
from alhazen.feature_collector import Collector

class TestConstraints(unittest.TestCase):
    def setUp(self) -> None:
        self.MAX_ITERATION = 30
        self.alhazen = Alhazen(
        initial_inputs=initial_inputs,
        grammar=grammar,
        evaluation_function=prop,
        max_iter=self.MAX_ITERATION
        )
        self.collector = Collector(grammar)

    def test_constraints(self):
           
        trees = self.alhazen.run()
        clf = trees[self.MAX_ITERATION-1]

        
        feature_names = self.collector.get_all_features()

        print(decision_tree_to_constraints(clf, feature_names))


        













if __name__ == "__main__":
    unittest.main()