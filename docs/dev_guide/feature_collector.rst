The Feature Collector Class
---------------------------

.. autoclass:: alhazen.feature_collector.Collector

Main Functions
^^^^^^^^^^^^^^

This method gives back all features defined by the grammar.
You can find in :doc:`features` what kind of features are implemented.

.. literalinclude:: ../../src/alhazen/feature_collector.py
   :pyobject: Collector.get_all_features
   :caption:  Description: Colletcts all the grammar based features. Input: / Output: List of Features as Dict{feature.name:feature.value}


.. literalinclude:: ../../src/alhazen/feature_collector.py
   :pyobject: Collector.collect_features_from_list
   :caption:  Description: Wrapper for collect features method Input: Set of Input. Input is a class describing a test input and containing a derivation tree, a oracle and features. Output: List of Features as Dict{feature.name:feature.value}

.. literalinclude:: ../../src/alhazen/feature_collector.py
   :pyobject: Collector.collect_features
   :caption: Description: Collects Features from a Test Input. Input: Input Output: Dict{feature.name:feature.value}

.. literalinclude:: ../../src/alhazen/feature_collector.py
   :pyobject: Collector.feature_collection
   :caption: Description: Gets all one and two dimensional features. Input: Derivation Tree, TODO: Feature Table Output: /

