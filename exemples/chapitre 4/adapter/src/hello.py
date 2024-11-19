from src.adapter import AbaqusAdapter, NastranAdapter
from src.mef import ModelElementsFinis, Node


class ExtractData:
    def __init__(self, nodes: dict[int, Node]):
        self.nodes = nodes

    def add_node(self, node: Node):
        self.nodes.update({node.id: node})

    def remove_node(self, node_id: int):
        del self.nodes[node_id]


def main():
    nodes_data = ExtractData({})
    nodes_data.add_node(Node(id=1, x=1, y=2, z=3))
    nodes_data.add_node(Node(id=2, x=4, y=5, z=6))

    model_elements = ModelElementsFinis(nodes=nodes_data.nodes)

    print(model_elements.compute())


def main2():
    adapter = AbaqusAdapter.from_file("data/abaqus.bl")
    print(adapter.get_nodes())

    model_elements = ModelElementsFinis(nodes=adapter.get_nodes())
    print(model_elements.compute())


def main3():
    adapter = NastranAdapter.from_file("data/nastran.dat")
    print(adapter.get_nodes())

    model_elements = ModelElementsFinis(nodes=adapter.get_nodes())
    print(model_elements.compute())


if __name__ == "__main__":
    main3()
