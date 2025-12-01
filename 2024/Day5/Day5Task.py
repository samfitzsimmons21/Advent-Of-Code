# The notation X|Y means that if both page number X and page number Y are to be produced as part of an update, page number X must be printed at some point before page number Y.

import collections
def Part1Task(word_search):
    total = 0
    search = word_search[:(word_search.index(""))]
    graph = collections.defaultdict(list)
    for rule in search:
        src, dest = map(int, rule.split("|"))
        graph[src].append(dest)

    print(graph)

    return total



if __name__ == "__main__":
    with open("input.txt", "r") as f:
        word_search = f.read().splitlines()



    print(f"Amount in right order: {Part1Task(word_search)}")



