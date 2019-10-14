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
    tolerance: Callable[[float], bool],
    label: Callable[[Chord], str] =\
        lambda chord: chord.identity
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
        labed

    Return
    ------
        graph: Graph
            Networkx Graph object.
    """
    # Adjacency list
    graph = Graph()
    # Chord to id map
    node_to_chord = {}
    # Add node to the graph usign
    # chord identity
    for chord in generator.run():
        node = label(chord)
        node_to_chord[node] = chord
        graph.add_node(node)
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
            _, distance = voice_leading(
                node_to_chord[source],
                node_to_chord[target]
            )
            # If within tolerance add edge
            if tolerance(distance):
                graph.add_edge(
                    source,
                    target,
                    distance = distance
                )
    return graph, node_to_chord


def convertGraphToData(
    graph: Graph
):
    """Convert a chord graph to columnal dataset.

    Parameters
    ----------
        graph : Graph
            A graph of chords.

    Return
    ------
        edges : list
            List of graph edges.
        vertices : list
            List of vertices
    """
    vertices= []
    edges = []

    index = 0
    node_to_index = {}
    for node, neighbors in graph.adjacency():
        vertices.append({
            'name': node,
            'group': 1
        })
        node_to_index[node] = index
        index += 1

    for node, neighbors in graph.adjacency():
        for neighbor, edge in neighbors.items():
            edges.append({
                'source': node_to_index[node],
                'target': node_to_index[neighbor],
                'value': edge['distance']
            })
    return edges, vertices
