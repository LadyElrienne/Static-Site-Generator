import unittest

from htmlnode import LeafNode, ParentNode, HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single_attribut(self):
        node = HTMLNode(props={"href": "https://boot.dev"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://boot.dev"')
    
    def test_props_to_html_multiple_attributes(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://example.com" target="_blank"')
    
    def test_props_to_html_none(self):
        node = HTMLNode(props=None)
        result = node.props_to_html()
        self.assertEqual(result, "")
    
    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        result = node.props_to_html()
        self.assertEqual(result, "")
    
    def test_props_to_html_number(self):
        node = HTMLNode(props={"pagenum": 5})
        result = node.props_to_html()
        self.assertEqual(result, ' pagenum="5"')
    
    def test_props_to_html_boolean(self):
        node = HTMLNode(props={"enabled": True})
        result = node.props_to_html()
        self.assertEqual(result, ' enabled="True"')

    def test_props_to_html_special_characters(self):
        node = HTMLNode(props={"data-info": 'He said "Bye!" & left.'})
        result = node.props_to_html()
        self.assertEqual(result, ' data-info="He said \"Bye!\" & left."')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Here!", {"href": "https://www.awebsite.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.awebsite.com">Click Here!</a>')
    
    def test_leaf_to_html_b(self):
        node = LeafNode("b", "This is a bold statement")
        self.assertEqual(node.to_html(), "<b>This is a bold statement</b>")
    
    def test_leaf_to_html_i(self):
        node = LeafNode("i", "This is an italic statement")
        self.assertEqual(node.to_html(), "<i>This is an italic statement</i>")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_with_properties(self):
        child = LeafNode("span", "hello")
        parent = ParentNode("div", [child], {"class": "container"})
        self.assertEqual(parent.to_html(), '<div class="container"><span>hello</span></div>')

    def test_multiple_levels_of_nesting(self):
        inner_child = LeafNode("b", "text")
        middle_child = ParentNode("span", [inner_child])
        outer_child = LeafNode("i", "italic")
        parent = ParentNode("div", [middle_child, outer_child])
        self.assertEqual(parent.to_html(), "<div><span><b>text</b></span><i>italic</i></div>")
    
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )  


if __name__ == "__main__":
    unittest.main()