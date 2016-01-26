import ast
import operator


__all__ = ['operators', 'comparisons', 'boolean_operators', 'unary_operators']


def _and(*args):
    for arg in args:
        if not arg:
            return arg
    return arg


def _or(*args):
    for arg in args:
        if arg:
            return arg
    return arg


operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}


comparisons = {
    ast.Eq: operator.eq,
    ast.NotEq: operator.ne,
    ast.Lt: operator.lt,
    ast.LtE: operator.le,
    ast.Gt: operator.gt,
    ast.GtE: operator.ge,
}


boolean_operators = {
    ast.And: _and,
    ast.Or: _or,
}


unary_operators = {
    ast.Not: operator.not_,
}
