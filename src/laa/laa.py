"""
Lazy replacements for Python's `any` and `all` functions.
This combines the principle of short circuit evaluation with the advantages of any and all.

Details (german):
https://juergen.rocks/art/python-any-all-lazy-short-circuit-evaluation.html


License:
========

Copyright 2016 Juergen Edelbluth

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import types


__author__ = 'Jürgen Edelbluth'
__version__ = '0.1.2'


def lazy_all(list_of_conditions: list) -> bool:
    """
    Replaces the all method. Can be used with lambdas (for lazy evaluation) or boolean values.

    Examples:

    >>> lazy_all([
    ...     1 == 1,
    ...     True,
    ...     lambda: 0 == 0,
    ... ])
    True

    Or within If-Clause:

    >>> if lazy_all([
    ...     lambda: 1 == 0,
    ...     1 == 1,
    ... ]):
    ...     print('ok')
    ... else:
    ...     print('nah')
    nah

    Empty lists lead to `False`:

    >>> lazy_all([])
    False

    Only booleans or lambdas are evaluated:

    >>> lazy_all([ 5 ])
    False

    >>> lazy_all([ 5, True, True, True ])
    True

    >>> lazy_all([ True, 5 ])
    True

    Type Handling from Lambdas:

    >>> lazy_all([ lambda: 5 ])
    True

    >>> lazy_all([ lambda: 5, lambda: 0 ])
    False

    :param list list_of_conditions: List containing boolean expressions or lambdas (for lazy evaluation)
    :return: Evaluation result
    :rtype: bool
    """
    evaluated = 0
    for condition in list_of_conditions:
        if isinstance(condition, bool):
            evaluated += 1
            condition_value = condition
        elif isinstance(condition, types.FunctionType):
            evaluated += 1
            condition_value = condition()
        else:
            continue  # pragma: no cover
        if not condition_value:
            return False
    return evaluated > 0


def lazy_any(list_of_conditions: list) -> bool:
    """
    Replaces the any method. Can be used with lambdas (for lazy evaluation) or boolean values.

    Examples:

    >>> lazy_any([
    ...     1 == 1,
    ...     True,
    ...     lambda: 0 == 0,
    ... ])
    True

    >>> lazy_any([
    ...     0 == 1,
    ...     True,
    ...     lambda: 1 == 0,
    ... ])
    True

    Within If-Clause:

    >>> if lazy_any([
    ...     lambda: 1 == 0,
    ...     1 == 1,
    ... ]):
    ...     print('ok')
    ... else:
    ...     print('nah')
    ok

    Empty lists lead to `False`:

    >>> lazy_any([])
    False

    Only booleans or lambdas are evaluated:

    >>> lazy_any([ 5 ])
    False

    >>> lazy_any([ 5, 3, 6, False, True ])
    True

    >>> lazy_any([ True, 5 ])
    True

    >>> lazy_any([ False, 5 ])
    False

    Type Handling from Lambdas:

    >>> lazy_any([ lambda: 5 ])
    True

    >>> lazy_any([ lambda: 5, lambda: 0 ])
    True

    :param list list_of_conditions: List containing boolean expressions or lambdas (for lazy evaluation)
    :return: Evaluation result
    :rtype: bool
    """
    for condition in list_of_conditions:
        if isinstance(condition, bool):
            condition_value = condition
        elif isinstance(condition, types.FunctionType):
            condition_value = condition()
        else:
            continue  # pragma: no cover
        if condition_value:
            return True
    return False
