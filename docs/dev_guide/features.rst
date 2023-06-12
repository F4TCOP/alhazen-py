The Feature Class
-----------------

.. autoclass:: alhazen.features.ExistenceFeature

.. autoclass:: alhazen.features.NumericInterpretation

.. autoclass:: alhazen.features.LengthFeature

.. autoclass:: alhazen.features.IsDigitFeature

Main Functions
^^^^^^^^^^^^^^

.. automethod:: alhazen.features.extract_existence
.. literalinclude:: ../../src/alhazen/features.py
   :pyobject: extract_existence

.. automethod:: alhazen.features.extract_numeric
.. literalinclude:: ../../src/alhazen/features.py
   :pyobject: extract_numeric

.. automethod:: alhazen.features.extract_length
.. literalinclude:: ../../src/alhazen/features.py
   :pyobject: extract_length
   :caption: Description: Extracts feature length

.. automethod:: alhazen.features.extract_is_digit
.. literalinclude:: ../../src/alhazen/features.py
   :pyobject: extract_is_digit
   :caption: Description: Extracts digit feature