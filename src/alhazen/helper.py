import graphviz
from sklearn import tree
from alhazen.requirementExtractionDT.requirements import tree_to_paths
from alhazen.requirementExtractionDT.treetools import remove_unequal_decisions
from alhazen.input_specifications import InputSpecification
from alhazen.generator import ISLAGenerator
def decision_tree_to_constraints(clf, feature_names, bug_triggering: bool = True) -> str:

    all_paths = tree_to_paths(clf, feature_names)
    relevant_paths = set()
    for path in all_paths:
        if path.is_bug() == bug_triggering:
            #TODO: how to get reqs
            reqs = path
            input_specification = InputSpecification(reqs)
            constraints = ISLAGenerator.transform_constraints(input_specification)
            relevant_paths.add(constraints)

    return relevant_paths


def show_tree(clf, feature_names):
    dot_data = tree.export_graphviz(
        remove_unequal_decisions(clf),
        out_file=None,
        feature_names=feature_names,
        class_names=["BUG", "NO_BUG"],
        filled=True,
        rounded=True,
    )
    return graphviz.Source(dot_data)


def get_dot_data(clf, feature_names):
    dot_data = tree.export_graphviz(
        clf,
        out_file=None,
        feature_names=feature_names,
        class_names=["BUG", "NO_BUG"],
        filled=True,
        rounded=True,
    )
    return dot_data
