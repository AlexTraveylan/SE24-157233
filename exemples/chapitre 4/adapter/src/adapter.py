from __future__ import annotations

from src.mef import Node
from abc import ABC, abstractmethod


class Adapter(ABC):
    @abstractmethod
    def get_nodes(self) -> dict[int, Node]:
        raise NotImplementedError


class AbaqusAdapter(Adapter):
    def __init__(self, nodes: dict[int, Node]):
        self.nodes = nodes

    def get_nodes(self) -> dict[int, Node]:
        return self.nodes

    @classmethod
    def from_file(cls, file_name: str) -> AbaqusAdapter:
        nodes = {}
        with open(file_name, "r") as file:
            lines = file.readlines()

        for line in filter(lambda x: x[0].isnumeric(), lines):
            node_id, x, y, z = line.split(",")
            nodes.update(
                {
                    int(node_id): Node(
                        id=int(node_id),
                        x=float(x),
                        y=float(y),
                        z=float(z),
                    )
                }
            )

        return cls(nodes)


class NastranAdapter(Adapter):
    def __init__(self, nodes: dict[int, Node]):
        self.nodes = nodes

    def get_nodes(self) -> dict[int, Node]:
        return self.nodes

    @classmethod
    def from_file(cls, file_name: str) -> NastranAdapter:
        nodes = {}
        with open(file_name, "r") as file:
            lines = file.readlines()

        for line in filter(lambda x: x[0].isnumeric(), lines):
            node_id, x, y, z = line.split()
            nodes.update(
                {
                    int(node_id): Node(
                        id=int(node_id),
                        x=float(x),
                        y=float(y),
                        z=float(z),
                    )
                }
            )

        return cls(nodes)
