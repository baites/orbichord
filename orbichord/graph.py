"""Create a graph with chords as nodes."""

from music21.chord import Chord
from music21.scale import ConcreteScale
from networkx import Graph
from orbichord.chordinate import EfficientVoiceLeading
from orbichord.generator import Generator
from typing import Callable


def createGraph(
    generator: Generator,
    voice_leading: EfficientVoiceLeading,
    tolerance: Callable[[float], bool]
) -> Graph:
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
        graph: Graph
            Networkx Graph object.
    """
    # Adjacency list
    graph = Graph()
    # Add the chords as nodes in graph
    graph.add_nodes_from(
        generator.run()
    )
    # Compute edges
    vetoed_nodes = set()
    # Loop over all source nodes
    for source in graph.nodes:
        # Vetoed source
        vetoed_nodes.add(source)
        # Loop over all target nodes
        for target in graph.nodes:
            # Check node is vetoed
            if target in vetoed_nodes:
                continue
            # Compute distance of efficient leading voice
            _, distance = voice_leading(source, target)
            # If within tolerance add edge
            if tolerance(distance):
                graph.add_edge(
                    source,
                    target,
                    distance = distance
                )
    return graph


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

    Return
    ------
        edges : list
            List of graph edges.
        vertices : list
            List of vertices
    """
    nodes, adjacencies, weights = graph

    vertices= []
    edges = []

    for source in range(len(nodes)):
        node = nodes[source]
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
