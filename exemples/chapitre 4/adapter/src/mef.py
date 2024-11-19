from pydantic import BaseModel
import numpy as np


class Node(BaseModel):
    id: int
    x: float
    y: float
    z: float

    def to_vector(self) -> np.ndarray:
        return np.array([self.x, self.y, self.z])

    def norm(self) -> float:
        return np.linalg.norm(self.to_vector())


class ModelElementsFinis(BaseModel):
    nodes: dict[int, Node]

    def compute(self) -> float:
        return sum(node.norm() for node in self.nodes.values())
