"""

Given an PreOrder Traversal Of a Binary tree Find the PostOrder Traversal

"""


import itertools
import functools


def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls


@count_calls
def postorder(preorder):
    if not preorder:
        return []
    else:
        root = preorder[0]
        left = list(itertools.takewhile(lambda x: x < root, preorder[1:]))
        right = preorder[len(left) + 1:]
        print(left, right)
        return postorder(left) + postorder(right) + [root]


print(postorder([15, 10, 5, 0, 13, 11, 14, 20]))
