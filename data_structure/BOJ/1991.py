n = int(input())

edges = [input().split() for _ in range(n)]

tree = {}
for edge in edges:
    if edge[0] not in tree:
        node = edge[0]
        left = edge[1]
        right = edge[2]

        if left == '.':
            left = None

        if right == '.':
            right = None

        if node not in tree:
            tree[node] = [left, right]

# print(tree)

def pre_traversal(nd):
    if not nd:
        return
    print(nd, end='')
    pre_traversal(tree[nd][0])
    pre_traversal(tree[nd][1])

def mid_traversal(nd):
    if not nd:
        return
    mid_traversal(tree[nd][0])
    print(nd, end='')
    mid_traversal(tree[nd][1])

def post_traversal(nd):
    if not nd:
        return
    post_traversal(tree[nd][0])
    post_traversal(tree[nd][1])
    print(nd, end='')

pre_traversal('A')
print()
mid_traversal('A')
print()
post_traversal('A')