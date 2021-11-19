class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, levol):
        if self.get_level() > levol:
            return
        spaces = '  ' * self.get_level() * 3
        prefix = spaces + "--"if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                 child.print_tree(levol)



def build_location_tree():
    a = TreeNode("gujarat")
    a.add_child(TreeNode("ahmedabad"))
    a.add_child(TreeNode("Baroda"))

    b = TreeNode("karnata")
    b.add_child(TreeNode("bangluru"))
    b.add_child(TreeNode("mysore"))

    c = TreeNode("india")
    c.add_child(a)
    c.add_child(b)

    d = TreeNode("New jersey")
    d.add_child(TreeNode("princeton"))
    d.add_child(TreeNode("Trenton"))

    e = TreeNode("california")
    e.add_child(TreeNode("san francisco"))
    e.add_child(TreeNode("Mountain view"))
    e.add_child(TreeNode("Palo Alto"))

    f = TreeNode("USA")
    f.add_child(d)
    f.add_child(e)

    root = TreeNode("Global")
    root.add_child(c)
    root.add_child(f)

    return root


if __name__ == '__main__':

    root = build_location_tree()
    level = int(input("enter level"))
    root.print_tree(level)






