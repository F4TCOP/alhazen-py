
The Feature Collector Class
---------------------------

.. autoclass:: alhazen.feature_collector.Collector

Main Functions
^^^^^^^^^^^^^^

This method gives back all features defined by the grammar.
You can find in :doc:`features` what kind of features are implemented.

.. literalinclude:: ../../src/alhazen/feature_collector.py
   :pyobject: Collector.get_all_features

Wrapper for collect features method

.. literalinclude:: ../../src/alhazen/feature_collector.py
   :pyobject: Collector.collect_features_from_list

Colletcts all the grammar based features. 

.. literalinclude:: ../../src/alhazen/feature_collector.py
   :pyobject: Collector.collect_features

Takes a Derivation Tree and 

.. literalinclude:: ../../src/alhazen/feature_collector.py
   :pyobject: Collector.feature_collection



