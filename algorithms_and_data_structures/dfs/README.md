# Depth-First Search

## Structure
* Iterative

```


```
* Recursive

```


```

## Graph representation
* edge lists
* adjacency map
* object (node with children)

```
    graph = collections.defaultdict(list)
    for course, pre_course in prerequisites:
        graph[pre_course].append(course)
    seen, in_stack = set(), set()

```

## Data structures
* visited sets
* stack

## Return
* min depth length
* path between two nodes (if exists)
* sum between two nodes (if path exists)

## Design patterns

