The Generator Class
-------------------

.. autoclass:: alhazen.generator.SimpleGenerator
.. autoclass:: alhazen.generator.AdvancedGenerator
.. autoclass:: alhazen.generator.ISLAGenerator

    In development feature to transform Decision trees into First order logic

Main Functions
^^^^^^^^^^^^^^

.. code-block:: text

    Input: forest: List of Derivation Trees, spec: TODO, grammar: Dict{str:List[str]}
    Output: Tuple(Bool, Derivation Tree)

.. automethod:: alhazen.generator.best_trees
.. literalinclude:: ../../src/alhazen/generator.py
   :pyobject: best_trees
   :language: python
   :caption: Description: Selects best Decision tree.

.. code-block:: text

    Input: grammar: Grammar, new_input_specifications: List[InputSpecification], timeout: int
    Output: List[str]

.. automethod:: alhazen.generator.generate_samples_advanced
.. literalinclude:: ../../src/alhazen/generator.py
   :pyobject: generate_samples_advanced
   :language: python
   :caption: Description: Generating samples

.. automethod:: alhazen.generator.generate_samples_random
.. literalinclude:: ../../src/alhazen/generator.py
   :pyobject: generate_samples_random
   :language: python
   :caption: Description: Generates samples randomly