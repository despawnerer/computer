class UndefinedVariable(NameError):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "variable '%s' is not defined" % self.name


class UnsupportedOperation(ValueError):
    def __init__(self, node):
        self.node = node
        self.operation_name = node.__class__.__name__

    def __str__(self):
        return "%s operations are not supported" % self.operation_name


class BadExpression(ValueError):
    pass
