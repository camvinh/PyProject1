import numpy as np
from skfusion import fusion
from skfusion import datasets

R12 = np.random.rand(50, 100)
R13 = np.random.rand(50, 40)
R23 = np.random.rand(100, 40)

t1 = fusion.ObjectType('Type 1', 10)
t2 = fusion.ObjectType('Type 2', 20)
t3 = fusion.ObjectType('Type 3', 30)
relations = [fusion.Relation(R12, t1, t2),
                 fusion.Relation(R13, t1, t3),
                 fusion.Relation(R23, t2, t3)]
fusion_graph = fusion.FusionGraph()
fusion_graph.add_relations_from(relations)
fuser = fusion.Dfmf()
fuser.fuse(fusion_graph)
print(fuser.factor(t1).shape)


new_R12 = np.random.rand(10, 100)
new_R13 = np.random.rand(10, 40)
new_relations = [fusion.Relation(new_R12, t1, t2),
                     fusion.Relation(new_R13, t1, t3)]
new_graph = fusion.FusionGraph(new_relations)
transformer = fusion.DfmfTransform()
transformer.transform(t1, new_graph, fuser)
print(transformer.factor(t1).shape)


dicty = datasets.load_dicty()
print(dicty)

print(dicty.object_types)

print(dicty.relations)
