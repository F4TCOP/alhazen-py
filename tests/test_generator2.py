import unittest

from isla.solver import ISLaSolver

from alhazen.input_specifications import Requirement, InputSpecification

from alhazen.generator import (
    SimpleGenerator,
    AdvancedGenerator,
    Generator,
    generate_samples_advanced,
    ISLAGenerator
)

from alhazen_formalizations.calculator import grammar
from alhazen.features import ExistenceFeature, NumericInterpretation

class TestGenerator(unittest.TestCase):
    def test_isla_generator2(self):
        from alhazen_formalizations.calculator import grammar
        isla_generator = ISLAGenerator(grammar)
        
        req_sqrt = Requirement(
            ExistenceFeature("exists(<function>@0)", "<function>", "sqrt"), ">", "0.5"
        )
        req_term = Requirement(
            NumericInterpretation("num(<term>)", "<term>"), ">", "-900.0"
        )
        input_specification = InputSpecification([req_sqrt, req_term])

        input = isla_generator.generate(input_specification)

        print(input)


if __name__ == "__main__":
    unittest.main()