The Feature Collector Class
---------------------------

.. autoclass:: alhazen.feature_collector.Collector

Main Functions
^^^^^^^^^^^^^^

This method gives back all features defined by the grammar.
You can find in :doc:`features` what kind of features are implemented.

.. literalinclude:: ../../src/alhazen/feature_collector.py
   :pyobject: Collector.get_all_features
   :caption:  Wrapper for collect features method


.. literalinclude:: ../../src/alhazen/feature_collector.py
   :pyobject: Collector.collect_features_from_list
   :caption: Colletcts all the grammar based features.

.. literalinclude:: ../../src/alhazen/feature_collector.py
   :pyobject: Collector.collect_features
   :caption: Takes a derivation tree as input returns parsed features

.. literalinclude:: ../../src/alhazen/feature_collector.py
   :pyobject: Collector.feature_collection
   :caption: Gets all one and two dimensional features.

