The Feature Collector Class
---------------------------

.. autoclass:: alhazen.feature_collector.Collector

Main Functions
^^^^^^^^^^^^^^

This method gives back all features defined by the grammar.
You can find in :doc:`features` what kind of features are implemented.

.. code-block:: text

    Input: List of Features as Dict{feature.name:feature.value}
    Output: List of Features as Dict{feature.name:feature.value}

.. automethod:: alhazen.feature_collector.Collector.get_all_features
.. literalinclude:: ../../src/alhazen/feature_collector.py
   :pyobject: Collector.get_all_features
   :caption:  Colletcts all the grammar based features.

.. code-block:: text

    Input: Set of Input. Input is a class describing a test input and containing a derivation tree, a oracle and features.
    Output: List of Features as Dict{feature.name:feature.value}

.. automethod:: alhazen.feature_collector.Collector.collect_features_from_list
.. literalinclude:: ../../src/alhazen/feature_collector.py
   :pyobject: Collector.collect_features_from_list
   :caption:  Description: Wrapper for collect features method

.. code-block:: text

    Input: Input
    Output: Dict{feature.name:feature.value}

.. automethod:: alhazen.feature_collector.Collector.collect_features
.. literalinclude:: ../../src/alhazen/feature_collector.py
   :pyobject: Collector.collect_features
   :caption: Description: Collects Features from a Test Input.

.. code-block:: text

    Input: Derivation Tree

.. automethod:: alhazen.feature_collector.Collector.feature_collection
.. literalinclude:: ../../src/alhazen/feature_collector.py
   :pyobject: Collector.feature_collection
   :caption: Description: Gets all one and two dimensional features.

