import igraph
import json

if __name__ == '__main__':
    with open("./data/OClinks_w.dl") as f:
        graph = igraph.Graph.Read_DL(f)
        seq_dict = graph.to_dict_dict()
        print(seq_dict)

    with open("./output/output.json", "w") as f:
        f.write(json.dumps(seq_dict))
