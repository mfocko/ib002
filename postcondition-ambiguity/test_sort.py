from hypothesis import given, settings
from hypothesis.strategies import integers, lists
import pytest

import itertools


def compare_by_value(pair):
    index, value = pair
    return value


def maximum(arr, n):
    """
    Finds index of maximum element of first n elements in list.

    Args:
        arr (List): List of values.
        n (int): Upper bound of index where to search for maximum (inclusive).

    Returns:
        Index of a maximum element in `arr[:n]`.
    """
    first_n_elements = itertools.islice(enumerate(arr), n)
    index, value = max(first_n_elements, key=compare_by_value)
    return index


def select_sort(arr, n):
    """
    Sorts list `arr` using select sort algorithm.

    Args:
        arr (List): List of values.
        n (int): Size of the list.

    Returns:
        Sorted list `arr`.
    """
    check_invariant(arr, n, n)

    for i in reversed(range(1, n)):
        j = maximum(arr, i + 1)
        arr[i], arr[j] = arr[j], arr[i]

        check_invariant(arr, n, i)

    return arr


def broken_select_sort(arr, n):
    if not arr:
        return

    max_value = max(arr)

    check_invariant(arr, n, n)

    for i in reversed(range(n)):
        arr[i] = max_value + i

        check_invariant(arr, n, i)

    return arr


# Precondition: n = |A|
# Loop invariant:
#     A[i + 1 : n] is sorted AND
#     all elements of A[i + 1 : n] are bigger or equal to the other elements
# Postcondition: A is sorted


def check_invariant(arr, n, i):
    # A[i + 1 : n] is sorted
    for x, y in zip(itertools.islice(arr, i + 1, n), itertools.islice(arr, i + 2, n)):
        assert x <= y

    # all elements of A[i + 1 : n] are bigger or equal to the other elements
    if i + 1 >= n:
        # in case there are no elements
        return

    # otherwise, since it's sorted, we can assume that it is enough to check the
    # other elements to the smallest value
    smallest = min(itertools.islice(arr, i + 1, n))
    for element in itertools.islice(arr, i + 1):
        assert smallest >= element


def check_vague_postcondition(original_arr, arr):
    if not arr:
        return

    for x, y in zip(arr, itertools.islice(arr, 1, len(arr))):
        assert x <= y


def check_postcondition(original_arr, arr):
    if not arr:
        return

    for x, y in zip(arr, itertools.islice(arr, 1, len(arr))):
        assert x <= y

    original_counts = {}
    for value in original_arr:
        original_counts[value] = 1 + original_counts.get(value, 0)

    counts = {}
    for value in arr:
        counts[value] = 1 + counts.get(value, 0)

    assert counts == original_counts


@given(lists(integers()))
@settings(max_examples=1000)
@pytest.mark.parametrize(
    "postcondition", [check_vague_postcondition, check_postcondition]
)
@pytest.mark.parametrize("sorting_function", [select_sort, broken_select_sort])
def test_select_sort(sorting_function, postcondition, numbers):
    result = sorting_function(numbers[:], len(numbers))
    postcondition(numbers, result)
