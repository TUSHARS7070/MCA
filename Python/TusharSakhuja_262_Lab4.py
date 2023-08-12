# multiple inheritence

class Tool:
    def __init__(self, name):
        self.name = name

    def use(self):
        pass


class Colorable:
    def __init__(self, color):
        self.color = color

    def set_color(self, color):
        pass


class DrawingTool(Tool, Colorable):
    def __init__(self, name, color):
        Tool.__init__(self, name)
        Colorable.__init__(self, color)

    def use(self):
        pass


class Pencil(DrawingTool):
    def __init__(self, name, color, hardness):
        DrawingTool.__init__(self, name, color)
        self.hardness = hardness

    def use(self):
        return f"Using a {self.color} pencil with hardness {self.hardness}"


class Brush(DrawingTool):
    def __init__(self, name, color, size):
        DrawingTool.__init__(self, name, color)
        self.size = size

    def use(self):
        return f"Using a {self.color} brush of size {self.size}"


class Eraser(Tool):
    def __init__(self, name, softness):
        Tool.__init__(self, name)
        self.softness = softness

    def use(self):
        return f"Using an eraser with softness {self.softness}"


class SketchBook(Pencil, Eraser):
    def __init__(self, pencil_color, eraser_softness):
        Pencil.__init__(self, "Pencil", pencil_color, "Medium")
        Eraser.__init__(self, "Eraser", eraser_softness)

    def create_artwork(self):
        pencil_result = self.use()
        eraser_result = self.use()
        return f"Creating artwork: {pencil_result} and {eraser_result}"


if __name__ == "__main__":
    pencil = Pencil("Pencil", "Black", "Soft")
    brush = Brush("Brush", "Blue", "Large")
    sketchbook = SketchBook("Gray", "Very Soft")

    print(pencil.use())
    print(brush.use())
    print(sketchbook.create_artwork())


# multilevel inheritence

class Tool:
    def __init__(self, name):
        self.name = name

    def use(self):
        pass


class Colorable:
    def __init__(self, color):
        self.color = color

    def set_color(self, color):
        pass


class DrawingTool(Tool, Colorable):
    def __init__(self, name, color):
        Tool.__init__(self, name)
        Colorable.__init__(self, color)

    def use(self):
        pass


class Pencil(DrawingTool):
    def __init__(self, name, color, hardness):
        DrawingTool.__init__(self, name, color)
        self.hardness = hardness

    def use(self):
        return f"Using a {self.color} pencil with hardness {self.hardness}"


class Brush(DrawingTool):
    def __init__(self, name, color, size):
        DrawingTool.__init__(self, name, color)
        self.size = size

    def use(self):
        return f"Using a {self.color} brush of size {self.size}"


class Eraser(Tool):
    def __init__(self, name, softness):
        Tool.__init__(self, name)
        self.softness = softness

    def use(self):
        return f"Using an eraser with softness {self.softness}"


class Canvas(DrawingTool):
    def __init__(self, name, color, dimensions):
        DrawingTool.__init__(self, name, color)
        self.dimensions = dimensions

    def use(self):
        return f"Creating a canvas with dimensions {self.dimensions}"


if __name__ == "__main__":
    pencil = Pencil("Pencil", "Black", "Soft")
    brush = Brush("Brush", "Blue", "Large")
    canvas = Canvas("Canvas", "White", "16x20")

    print(pencil.use())
    print(brush.use())
    print(canvas.use())

# Hierarchical Inheritances

class Tool:
     def __init__(self, name):
        self.name = name

     def use(self):
        pass


class Colorable:
     def __init__(self, color):
        self.color = color

     def set_color(self, color):
        pass


class DrawingTool(Tool, Colorable):
    def __init__(self, name, color):
        Tool.__init__(self, name)
        Colorable.__init__(self, color)

    def use(self):
        pass


class Pencil(DrawingTool):
    def __init__(self, name, color, hardness):
        DrawingTool.__init__(self, name, color)
        self.hardness = hardness

    def use(self):
        return f"Using a {self.color} pencil with hardness {self.hardness}"


class Brush(DrawingTool):
    def __init__(self, name, color, size):
        DrawingTool.__init__(self, name, color)
        self.size = size

    def use(self):
        return f"Using a {self.color} brush of size {self.size}"


class Eraser(Tool):
    def __init__(self, name, softness):
        Tool.__init__(self, name)
        self.softness = softness

    def use(self):
        return f"Using an eraser with softness {self.softness}"


class ArtToolbox:
    def __init__(self):
        self.tools = []

    def add_tool(self, tool):
        self.tools.append(tool)

    def list_tools(self):
        tool_list = "\n".join(tool.name for tool in self.tools)
        return f"Art toolbox contains:\n{tool_list}"


if __name__ == "__main__":
    pencil = Pencil("Pencil", "Black", "Soft")
    brush = Brush("Brush", "Blue", "Large")
    eraser = Eraser("Eraser", "Soft")

    toolbox = ArtToolbox()
    toolbox.add_tool(pencil)
    toolbox.add_tool(brush)
    toolbox.add_tool(eraser)

    print(pencil.use())
    print(brush.use())
    print(eraser.use())

    print(toolbox.list_tools())
