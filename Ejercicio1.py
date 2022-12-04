from __future__ import annotations
import sys

class letra:
    def __init__(self, letra: str, freq: int):
        self.letra: str = letra
        self.freq: int = freq
        self.bitstring: dict[str, str] = {}

    def __repr__(self) -> str:
        return f"{self.letra}:{self.freq}"

class TreeNode:
        def _init_(self, freq: int, left: letra | TreeNode, right: letra | TreeNode):
            self.freq: int = freq
            self.left: letra | TreeNode = left
            self.right: letra | TreeNode = right

def parse_file(file_path: str) -> list[letra]:
    
    chars: dict[str, int] = {}
    with open(file_path) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            chars[c] = chars[c] + 1 if c in chars else 1
    return sorted((letra(c, f) for c, f in chars.items()), key=lambda x: x.freq)

def build_tree(letras: list[letra]) -> letra | TreeNode:
    
    response: list[letra | TreeNode] = letra
    while len(response) > 1:
        left = response.pop(0)
        right = response.pop(0)
        total_freq = left.freq + right.freq
        node = TreeNode(total_freq, left, right)
        response.append(node)
        response.sort(key=lambda x: x.freq)
    return response[0]

def traverse_tree(root: letra | TreeNode, bitstring: str) -> list[letra]:
    
    if isinstance(root, letra):
        root.bitstring[root.letra] = bitstring
        return [root]
    treenode: TreeNode = root
    letters = []
    letters = traverse_tree(treenode.left, bitstring + "0")
    letters = traverse_tree(treenode.right, bitstring + "1")
    return letters

def huffman(file_path: str) -> None:
    
    letters_list = parse_file(file_path)
    root = build_tree(letters_list)
    letters = {
        k: v for letter in traverse_tree(root, "") for k, v in letter.bitstring.items()
    }
    print(f"Huffman Coding  of {file_path}: ")
    with open(file_path) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            print(letters[c], end=" ")
    print()

if __name__ == "__main__":
    huffman(sys.argv[1])