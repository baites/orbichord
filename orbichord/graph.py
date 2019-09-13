"""Create a graph with chords as nodes."""

from orbichord.chordinate import EfficientVoiceLeading
from orbichord.generator import Generator
from music21.scale import ConcreteScale
from typing import Callable


def createGraph(
    generator: Generator,
    voice_leading: EfficientVoiceLeading,
    tolerance: Callable[[float], bool]
) -> tuple:
    """Create a graph as adjacency list of chords.

    Parameters:
        generator (Generator): An orbichord generator
        voice_leading (EfficientVoiceLeading): A voice leading object
        tolerance (Callable[[float], bool]): Tolerance function
    Return:
        tuple: containing graph node, adjacency, and strength lists
    """
    # Adjacency list
    nodes = []
    adjacencies = []
    strengths = []
    # Loop over all chords
    for chord in generator.run():
        # Add the first node
        if len(nodes) == 0:
            nodes.append(chord)
            adjacencies.append([])
            strengths.append([])
            continue
        # Loop over the nodes
        adjacency = []
        strength = []
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
                # Add node strength
                strength.append(distance)
                # Add chord distance to the node
                strengths[index].append(distance)
        # Add chrod as a node
        nodes.append(chord)
        # Add new adjacency
        adjacencies.append(adjacency)
        # Add new strength
        strengths.append(strength)
    return nodes, adjacencies, strengths
