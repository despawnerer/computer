import ast

from .exceptions import UndefinedVariable, UnsupportedOperation
from .operations import (
    operators,
    comparisons,
    boolean_operators,
    unary_operators,
)


__all__ = ['evaluate']


def evaluate(expr, **variables):
    """
    >>> evaluate('2**6')
    64
    >>> evaluate('1 + 2*3**(2 + 2) / (6 + -7)')
    -161.0
    >>> evaluate('5 < 4')
    False
    >>> evaluate('5 < a < 10', a=6)
    True
    """
    module = ast.parse(expr)  # Module(body=[Expr(value=...)])
    return _eval(module.body[0].value, variables)


def _eval(node, context):
    # types, we only support numbers
    if isinstance(node, ast.Num):
        return node.n

    # operators: binary, unary, comparisons, boolean
    elif isinstance(node, ast.operator):
        try:
            return operators[type(node)]
        except KeyError:
            raise UnsupportedOperation(node)
    elif isinstance(node, ast.cmpop):
        try:
            return comparisons[type(node)]
        except KeyError:
            raise UnsupportedOperation(node)
    elif isinstance(node, ast.boolop):
        try:
            return boolean_operators[type(node)]
        except KeyError:
            raise UnsupportedOperation(node)
    elif isinstance(node, ast.unaryop):
        try:
            return unary_operators[type(node)]
        except KeyError:
            raise UnsupportedOperation(node)

    # operation nodes
    elif isinstance(node, ast.BinOp):
        # <left> <operator> <right>
        return _eval(node.op, context)(
            _eval(node.left, context),
            _eval(node.right, context)
        )
    elif isinstance(node, ast.Compare):
        # <left> (<cmpop> <comparator> <cmpop> <comparator>...)
        left = _eval(node.left, context)
        for op, comparator in zip(node.ops, node.comparators):
            right = _eval(comparator, context)
            value = _eval(op, context)(left, right)
            if value is False:
                return False
            left = right
        return True
    elif isinstance(node, ast.BoolOp):
        values = [_eval(value, context) for value in node.values]
        return _eval(node.op, context)(*values)
    elif isinstance(node, ast.UnaryOp):
        return _eval(node.op, context)(_eval(node.operand, context))

    # variables
    elif isinstance(node, ast.Name):
        try:
            return context[node.id]
        except KeyError:
            raise UndefinedVariable(node.id)

    # get out if it's anything we don't support
    else:
        raise UnsupportedOperation(node)
