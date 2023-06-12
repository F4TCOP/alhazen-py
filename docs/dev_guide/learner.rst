The Learner Class
-----------------

.. autoclass:: alhazen.learner.Learner
.. autoclass:: alhazen.learner.DecisionTreeLearner
.. autoclass:: alhazen.learner.RandomForestLearner
.. autoclass:: alhazen.learner.XGBTLearner

   in development

Main Functions of all Learners
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../src/alhazen/learner.py
   :pyobject: Learner.train
   :caption: trains model on data

.. literalinclude:: ../../src/alhazen/learner.py
   :pyobject: Learner.get_input_specifications

.. literalinclude:: ../../src/alhazen/learner.py
   :pyobject: Learner.visualize

.. literalinclude:: ../../src/alhazen/learner.py
   :pyobject: Learner.predict

.. literalinclude:: ../../src/alhazen/learner.py
   :pyobject: DecisionTreeLearner.train
   :caption: trains model on data

.. literalinclude:: ../../src/alhazen/learner.py
   :pyobject: DecisionTreeLearner.get_input_specifications

