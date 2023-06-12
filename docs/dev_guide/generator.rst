The Generator Class
-------------------


.. autoclass:: alhazen.generator.SimpleGenerator
.. autoclass:: alhazen.generator.AdvancedGenerator
.. autoclass:: alhazen.generator.ISLAGenerator

    In development feature to transform Decision trees into First order logic

Main Functions
^^^^^^^^^^^^^^

.. literalinclude:: ../../src/alhazen/generator.py
   :pyobject: best_trees
   :language: python
   :caption: Description: Selects best Decision tree. Input: forest: List of Derivation Trees, spec: TODO, grammar: Dict{str:List[str]} Output: Tuple(Bool, Derivation Tree) // TODO: Tuple richtig hier?

.. literalinclude:: ../../src/alhazen/generator.py
   :pyobject: generate_samples_advanced
   :language: python
   :caption: Description: Generating samples // TODO: what kind of samples

.. literalinclude:: ../../src/alhazen/generator.py
   :pyobject: generate_samples_random
   :language: python
   :caption: Description: Generates samples randomly