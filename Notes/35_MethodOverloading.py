class Example:
    def add(self, *args):
        return sum(args)

obj = Example()
print(obj.add(2, 3))         # Uses 2 arguments
print(obj.add(2, 3, 4))      # Uses 3 arguments
