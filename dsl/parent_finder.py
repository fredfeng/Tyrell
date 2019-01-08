from typing import List, Dict, Optional
from .node import Node


class ParentFinder:
    '''
    A utility class providing mapping between AST Node and its parent.
    '''

    _parent_map: Dict[Node, Node]

    def __init__(self, prog: Node):
        self._parent_map = dict()
        stack = [prog]
        while len(stack) > 0:
            node = stack.pop()
            for child in node.children:
                self._parent_map[child] = node
                stack.append(child)

    def get_parent(self, node: Node) -> Optional[Node]:
        '''Get the parent of the node, or None if the parent cannot be found.'''
        return self._parent_map.get(node, None)

    def get_parent_or_raise(self, node: Node) -> int:
        '''Get the parent of the node, or raise `KeyError` if the parent cannot be found.'''
        return self._parent_map[node]
