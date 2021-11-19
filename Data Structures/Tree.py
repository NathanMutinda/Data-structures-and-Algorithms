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

    def print_tree(self):
        spaces = '  ' * self.get_level() * 3
        prefix = spaces + "--"if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                 child.print_tree()




def build_product_tree():
    root = TreeNode('Electronics')

    laptop = TreeNode("laptop")

    laptop.add_child(TreeNode("mac"))
    laptop.add_child(TreeNode("surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode('cellphone')
    cellphone.add_child(TreeNode('iphone'))
    cellphone.add_child(TreeNode('Google Pixel'))
    cellphone.add_child(TreeNode('Vivo'))

    tv = TreeNode('TV')
    tv.add_child(TreeNode('samsung'))
    tv.add_child(TreeNode('LG'))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    #print(root.get_level())






class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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

    def print_tree(self, p_name):
        if p_name == 'both':
            value = self.name + "(" + self.designation + ")"
        elif p_name == 'name':
            value = self.name
        else:
            value = self.designation

        spaces = '  ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(p_name)


def build_management_tree():
    low = TreeNode("vishwas", 'infrastructure head')
    low.add_child(TreeNode('dhaval', 'cloud manager'))
    low.add_child(TreeNode('abhijit', 'App manager'))

    cto = TreeNode("chinmay", "CTO")
    cto.add_child(TreeNode("Aamir", "Application head"))
    cto.add_child(low)

    gel = TreeNode("Gel", " HR head")
    gel.add_child(TreeNode("peter","Recruitment Manager"))
    gel.add_child(TreeNode("waqas", "policy manager"))

    root_node = TreeNode("NilPul", "CEO")
    root_node.add_child(cto)
    root_node.add_child(gel)

    return root_node


if __name__ == '__main__':
    root = build_management_tree()
    root.print_tree("name")
    root.print_tree("both")
    root.print_tree("designation")
    #print(root.get_level())





