class UndefinedVariable(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "variable '%s' is not defined" % self.name


class UnsupportedOperation(Exception):
    def __init__(self, node):
        self.node = node
        self.operation_name = node.__class__.__name__

    def __str__(self):
        return "%s operations are not supported" % self.operation_name
