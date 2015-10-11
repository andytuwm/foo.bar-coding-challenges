class Node:

    def __init__(self, char=None):
        self.endString = False;
        self.letter = None;
        self.nextNode = [];
        if char:
            self.letter = char;

    def checkExistingNode(self, charMatch):
        for i, node in enumerate(self.nextNode):
            if node.letter == charMatch:
                return i;
        return False;

    def debugprint(self):
        for n in self.nextNode:
            print(n.letter);


count = 0;
headNode = Node();


def insertCode(code, currentNode=headNode, indexCount=0):
    nextNode = addNode(currentNode, code[indexCount]);
    indexCount += 1;
    if indexCount >= len(code):
        nextNode.endString = True;
    else:
        insertCode(code, nextNode, indexCount);
    return;


def addNode(node, char):
    index = node.checkExistingNode(char);
    if not index:
        node.nextNode.append(Node(char));
        return node.nextNode[-1];
    return node.nextNode[index];


def checkCode(headNode, code, i=0):
    if len(code) == 0:
        if headNode.endString:
            return True;
        return False;
    for node in headNode.nextNode:
        if node.letter == code[i]:
            i += 1;
            if i < len(code):
                return checkCode(node, code, i);
            if node.endString:
                print("matched", code);
                return True;
    return False;


def addWord(head, word):
    global count;
    if len(word) == 0:
        if head.endString:
            return;
        count += 1;
        head.endString = True;
        return;
    if not checkCode(head, word):
        count += 1;
        insertCode(word, head);
        reverse = word[::-1];
        insertCode(reverse, head);


def answer(x):
    for code in x:
        addWord(headNode, code);
    return count;