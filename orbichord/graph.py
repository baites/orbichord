"""Create a graph with chords as nodes."""

from music21.chord import Chord
from music21.scale import ConcreteScale
from orbichord.chordinate import EfficientVoiceLeading
from orbichord.generator import Generator
from typing import Callable


def createGraph(
    generator: Generator,
    voice_leading: EfficientVoiceLeading,
    tolerance: Callable[[float], bool]
) -> tuple:
    """Create a graph as adjacency list of chords.

    Parameters
    ----------
        generator : Generator
            An orbichord generator.
        voice_leading : EfficientVoiceLeading
            A voice leading object.
        tolerance : Callable[[float], bool]
            Tolerance function.
    Return:
        nodes: list
            Graph node.
        adjacencies: list
            Graph adjacencies
        weights: list
            weight lists.
    """
    # Adjacency list
    nodes = []
    adjacencies = []
    weights = []
    # Loop over all chords
    for chord in generator.run():
        # Add the first node
        if len(nodes) == 0:
            nodes.append(chord)
            adjacencies.append([])
            weights.append([])
            continue
        # Loop over the nodes
        adjacency = []
        weight = []
        number_nodes = len(nodes)
        for index in range(number_nodes):
            node = nodes[index]
            # Compute distance of efficient leading voice
            _, distance = voice_leading(chord, node)
            # If within tolerance
            if tolerance(distance):
                # Add node to new adjancy
                adjacency.append(index)
                # Add chord to previous adjancy
                adjacencies[index].append(number_nodes)
                # Add node weight
                weight.append(distance)
                # Add chord distance to the node
                weights[index].append(distance)
        # Add chrod as a node
        nodes.append(chord)
        # Add new adjacency
        adjacencies.append(adjacency)
        # Add new weight
        weights.append(weight)
    return nodes, adjacencies, weights


def convertGraphToData(
    graph: tuple,
    label: Callable[[Chord], str] = None,
    identify: Callable[[Chord], str] = None
):
    """Convert a chrod graph to columnal dataset.

    Parameters
    ----------
        graph : tuple
            A tuple containing graph nodes, adjacencies, and weights.
        label : Callable[[Chord], str]
            Function to name chords.
        identify : Callable[[Chord], str]
            Function to identify identical chords.

    Return
    ------
        edges : list
            List of graph edges.
        vertices : list
            List of vertices
    """
    nodes, adjacencies, weights = graph

    vetoed_nodes = set()

    vertices= []
    edges = []

    for source in range(len(nodes)):
        node = nodes[source]
        if identify(node) in vetoed_nodes:
            continue
        vertices.append({
            'name': label(node),
            'group': 1
        })
        for tindex in range(len(adjacencies[source])):
            target = adjacencies[source][tindex]
            value = weights[source][tindex]
            edges.append({
                'source': source,
                'target': target,
                'value': value
            })
    return edges, vertices
