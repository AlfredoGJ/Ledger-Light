from collections import defaultdict
import re


class TreeNode(object):
    def __init__(self, text, offset, elements=None):
        self.text = text
        self.offset = offset
        self.elements = elements or []

    def __iter__(self):
        for el in self.elements:
            yield el


class TreeNode1(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode1, self).__init__(text, offset, elements)
        self.Sep = elements[1]


class TreeNode2(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode2, self).__init__(text, offset, elements)
        self.EOS = elements[1]


class TreeNode3(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode3, self).__init__(text, offset, elements)
        self.File = elements[0]


class TreeNode4(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode4, self).__init__(text, offset, elements)
        self.Sort = elements[0]


class TreeNode5(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode5, self).__init__(text, offset, elements)
        self.PriceDb = elements[0]


class TreeNode6(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode6, self).__init__(text, offset, elements)
        self.FileFlag = elements[0]
        self.Sep = elements[1]
        self.FilePath = elements[2]


class TreeNode7(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode7, self).__init__(text, offset, elements)
        self.SortFlag = elements[0]
        self.Sep = elements[1]
        self.SortCriteria = elements[2]


class TreeNode8(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode8, self).__init__(text, offset, elements)
        self.PriceDbFlag = elements[0]
        self.Sep = elements[1]
        self.FilePath = elements[2]


class ParseError(SyntaxError):
    pass


FAILURE = object()


class Grammar(object):
    def _read_LedgerCall(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['LedgerCall'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 6]
        if chunk0 == 'Ledger':
            address1 = TreeNode(self._input[self._offset:self._offset + 6], self._offset)
            self._offset = self._offset + 6
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"Ledger"')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_Sep()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                remaining0, index3, elements1, address4 = 0, self._offset, [], True
                while address4 is not FAILURE:
                    address4 = self._read_Options()
                    if address4 is not FAILURE:
                        elements1.append(address4)
                        remaining0 -= 1
                if remaining0 <= 0:
                    address3 = TreeNode(self._input[index3:self._offset], index3, elements1)
                    self._offset = self._offset
                else:
                    address3 = FAILURE
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode1(self._input[index2:self._offset], index2, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            index4, elements2 = self._offset, []
            address5 = FAILURE
            chunk1 = None
            if self._offset < self._input_size:
                chunk1 = self._input[self._offset:self._offset + 6]
            if chunk1 == 'Ledger':
                address5 = TreeNode(self._input[self._offset:self._offset + 6], self._offset)
                self._offset = self._offset + 6
            else:
                address5 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"Ledger"')
            if address5 is not FAILURE:
                elements2.append(address5)
                address6 = FAILURE
                address6 = self._read_EOS()
                if address6 is not FAILURE:
                    elements2.append(address6)
                else:
                    elements2 = None
                    self._offset = index4
            else:
                elements2 = None
                self._offset = index4
            if elements2 is None:
                address0 = FAILURE
            else:
                address0 = TreeNode2(self._input[index4:self._offset], index4, elements2)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
        self._cache['LedgerCall'][index0] = (address0, self._offset)
        return address0

    def _read_Options(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Options'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_File()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            index3 = self._offset
            address2 = self._read_Sep()
            if address2 is FAILURE:
                self._offset = index3
                address2 = self._read_EOS()
                if address2 is FAILURE:
                    self._offset = index3
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode3(self._input[index2:self._offset], index2, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            index4, elements1 = self._offset, []
            address3 = FAILURE
            address3 = self._read_Sort()
            if address3 is not FAILURE:
                elements1.append(address3)
                address4 = FAILURE
                index5 = self._offset
                address4 = self._read_Sep()
                if address4 is FAILURE:
                    self._offset = index5
                    address4 = self._read_EOS()
                    if address4 is FAILURE:
                        self._offset = index5
                if address4 is not FAILURE:
                    elements1.append(address4)
                else:
                    elements1 = None
                    self._offset = index4
            else:
                elements1 = None
                self._offset = index4
            if elements1 is None:
                address0 = FAILURE
            else:
                address0 = TreeNode4(self._input[index4:self._offset], index4, elements1)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
                index6, elements2 = self._offset, []
                address5 = FAILURE
                address5 = self._read_PriceDb()
                if address5 is not FAILURE:
                    elements2.append(address5)
                    address6 = FAILURE
                    index7 = self._offset
                    address6 = self._read_Sep()
                    if address6 is FAILURE:
                        self._offset = index7
                        address6 = self._read_EOS()
                        if address6 is FAILURE:
                            self._offset = index7
                    if address6 is not FAILURE:
                        elements2.append(address6)
                    else:
                        elements2 = None
                        self._offset = index6
                else:
                    elements2 = None
                    self._offset = index6
                if elements2 is None:
                    address0 = FAILURE
                else:
                    address0 = TreeNode5(self._input[index6:self._offset], index6, elements2)
                    self._offset = self._offset
                if address0 is FAILURE:
                    self._offset = index1
        self._cache['Options'][index0] = (address0, self._offset)
        return address0

    def _read_File(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['File'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_FileFlag()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_Sep()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_FilePath()
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode6(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['File'][index0] = (address0, self._offset)
        return address0

    def _read_FileFlag(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['FileFlag'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 6]
        if chunk0 == '--file':
            address0 = TreeNode(self._input[self._offset:self._offset + 6], self._offset)
            self._offset = self._offset + 6
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"--file"')
        if address0 is FAILURE:
            self._offset = index1
            chunk1 = None
            if self._offset < self._input_size:
                chunk1 = self._input[self._offset:self._offset + 2]
            if chunk1 == '-f':
                address0 = TreeNode(self._input[self._offset:self._offset + 2], self._offset)
                self._offset = self._offset + 2
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"-f"')
            if address0 is FAILURE:
                self._offset = index1
        self._cache['FileFlag'][index0] = (address0, self._offset)
        return address0

    def _read_Sort(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Sort'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_SortFlag()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_Sep()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_SortCriteria()
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode7(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['Sort'][index0] = (address0, self._offset)
        return address0

    def _read_SortFlag(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['SortFlag'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 6]
        if chunk0 == '--sort':
            address0 = TreeNode(self._input[self._offset:self._offset + 6], self._offset)
            self._offset = self._offset + 6
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"--sort"')
        if address0 is FAILURE:
            self._offset = index1
            chunk1 = None
            if self._offset < self._input_size:
                chunk1 = self._input[self._offset:self._offset + 2]
            if chunk1 == '-S':
                address0 = TreeNode(self._input[self._offset:self._offset + 2], self._offset)
                self._offset = self._offset + 2
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"-S"')
            if address0 is FAILURE:
                self._offset = index1
        self._cache['SortFlag'][index0] = (address0, self._offset)
        return address0

    def _read_SortCriteria(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['SortCriteria'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 == 'd':
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"d"')
        if address0 is FAILURE:
            self._offset = index1
            chunk1 = None
            if self._offset < self._input_size:
                chunk1 = self._input[self._offset:self._offset + 1]
            if chunk1 == 'a':
                address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"a"')
            if address0 is FAILURE:
                self._offset = index1
        self._cache['SortCriteria'][index0] = (address0, self._offset)
        return address0

    def _read_PriceDb(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['PriceDb'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_PriceDbFlag()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_Sep()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_FilePath()
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode8(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['PriceDb'][index0] = (address0, self._offset)
        return address0

    def _read_PriceDbFlag(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['PriceDbFlag'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 10]
        if chunk0 == '--price-db':
            address0 = TreeNode(self._input[self._offset:self._offset + 10], self._offset)
            self._offset = self._offset + 10
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"--price-db"')
        self._cache['PriceDbFlag'][index0] = (address0, self._offset)
        return address0

    def _read_FilePath(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['FilePath'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 0, self._offset, [], True
        while address1 is not FAILURE:
            if self._offset < self._input_size:
                address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address1 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('<any char>')
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['FilePath'][index0] = (address0, self._offset)
        return address0

    def _read_Sep(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Sep'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 1, self._offset, [], True
        while address1 is not FAILURE:
            chunk0 = None
            if self._offset < self._input_size:
                chunk0 = self._input[self._offset:self._offset + 1]
            if chunk0 == ' ':
                address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address1 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('" "')
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['Sep'][index0] = (address0, self._offset)
        return address0

    def _read_EOS(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['EOS'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        if self._offset < self._input_size:
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('<any char>')
        self._offset = index1
        if address0 is FAILURE:
            address0 = TreeNode(self._input[self._offset:self._offset], self._offset)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['EOS'][index0] = (address0, self._offset)
        return address0


class Parser(Grammar):
    def __init__(self, input, actions, types):
        self._input = input
        self._input_size = len(input)
        self._actions = actions
        self._types = types
        self._offset = 0
        self._cache = defaultdict(dict)
        self._failure = 0
        self._expected = []

    def parse(self):
        tree = self._read_LedgerCall()
        if tree is not FAILURE and self._offset == self._input_size:
            return tree
        if not self._expected:
            self._failure = self._offset
            self._expected.append('<EOF>')
        raise ParseError(format_error(self._input, self._failure, self._expected))


def format_error(input, offset, expected):
    lines, line_no, position = input.split('\n'), 0, 0
    while position <= offset:
        position += len(lines[line_no]) + 1
        line_no += 1
    message, line = 'Line ' + str(line_no) + ': expected ' + ', '.join(expected) + '\n', lines[line_no - 1]
    message += line + '\n'
    position -= len(line) + 1
    message += ' ' * (offset - position)
    return message + '^'

def parse(input, actions=None, types=None):
    parser = Parser(input, actions, types)
    return parser.parse()
