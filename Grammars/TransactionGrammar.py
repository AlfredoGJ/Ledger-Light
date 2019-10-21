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
        self.Date = elements[0]
        self.Sep = elements[1]
        self.NL = elements[3]
        self.SepPlus = elements[6]
        self.CompletePosting = elements[5]


class TreeNode2(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode2, self).__init__(text, offset, elements)
        self.Account = elements[0]
        self.SepDouble = elements[1]
        self.Amount = elements[2]
        self.NL = elements[4]


class TreeNode3(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode3, self).__init__(text, offset, elements)
        self.Account = elements[0]
        self.NL = elements[2]


class TreeNode4(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode4, self).__init__(text, offset, elements)
        self.AccountID = elements[0]


class TreeNode5(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode5, self).__init__(text, offset, elements)
        self.AccountID = elements[1]


class TreeNode6(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode6, self).__init__(text, offset, elements)
        self.Commodity = elements[0]
        self.Quantity = elements[1]


class TreeNode7(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode7, self).__init__(text, offset, elements)
        self.Quantity = elements[0]
        self.Commodity = elements[1]


class TreeNode8(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode8, self).__init__(text, offset, elements)
        self.Sep = elements[1]


class TreeNode9(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode9, self).__init__(text, offset, elements)
        self.Year = elements[0]
        self.Month = elements[2]


class TreeNode10(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode10, self).__init__(text, offset, elements)
        self.Day = elements[1]


class ParseError(SyntaxError):
    pass


FAILURE = object()


class Grammar(object):
    REGEX_1 = re.compile('^[a-zA-Z]')
    REGEX_2 = re.compile('^[a-zA-Z]')
    REGEX_3 = re.compile('^[0-9]')
    REGEX_4 = re.compile('^[0-9]')
    REGEX_5 = re.compile('^[0-9]')
    REGEX_6 = re.compile('^[0-9]')
    REGEX_7 = re.compile('^[1-9]')
    REGEX_8 = re.compile('^[0-2]')
    REGEX_9 = re.compile('^[1-9]')
    REGEX_10 = re.compile('^[1-2]')
    REGEX_11 = re.compile('^[0-9]')
    REGEX_12 = re.compile('^[0-1]')
    REGEX_13 = re.compile('^[a-zA-Z]')
    REGEX_14 = re.compile('^[a-zA-Z ]')
    REGEX_15 = re.compile('^[0-9]')

    def _read_Transaction(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Transaction'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_Date()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_Sep()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                index2 = self._offset
                address3 = self._read_Description()
                if address3 is FAILURE:
                    address3 = TreeNode(self._input[index2:index2], index2)
                    self._offset = index2
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    address4 = self._read_NL()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read_SepPlus()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                            address6 = FAILURE
                            address6 = self._read_CompletePosting()
                            if address6 is not FAILURE:
                                elements0.append(address6)
                                address7 = FAILURE
                                address7 = self._read_SepPlus()
                                if address7 is not FAILURE:
                                    elements0.append(address7)
                                    address8 = FAILURE
                                    remaining0, index3, elements1, address9 = 1, self._offset, [], True
                                    while address9 is not FAILURE:
                                        address9 = self._read_Posting()
                                        if address9 is not FAILURE:
                                            elements1.append(address9)
                                            remaining0 -= 1
                                    if remaining0 <= 0:
                                        address8 = TreeNode(self._input[index3:self._offset], index3, elements1)
                                        self._offset = self._offset
                                    else:
                                        address8 = FAILURE
                                    if address8 is not FAILURE:
                                        elements0.append(address8)
                                    else:
                                        elements0 = None
                                        self._offset = index1
                                else:
                                    elements0 = None
                                    self._offset = index1
                            else:
                                elements0 = None
                                self._offset = index1
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
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
            address0 = TreeNode1(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['Transaction'][index0] = (address0, self._offset)
        return address0

    def _read_Description(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Description'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        address0 = self._read_Text()
        self._cache['Description'][index0] = (address0, self._offset)
        return address0

    def _read_Posting(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Posting'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_CompletePosting()
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_HalfPosting()
            if address0 is FAILURE:
                self._offset = index1
        self._cache['Posting'][index0] = (address0, self._offset)
        return address0

    def _read_CompletePosting(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['CompletePosting'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_Account()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_SepDouble()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_Amount()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    index2 = self._offset
                    address4 = self._read_SepPlus()
                    if address4 is FAILURE:
                        address4 = TreeNode(self._input[index2:index2], index2)
                        self._offset = index2
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read_NL()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
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
            address0 = TreeNode2(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['CompletePosting'][index0] = (address0, self._offset)
        return address0

    def _read_HalfPosting(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['HalfPosting'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_Account()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            index2 = self._offset
            address2 = self._read_SepPlus()
            if address2 is FAILURE:
                address2 = TreeNode(self._input[index2:index2], index2)
                self._offset = index2
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_NL()
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
            address0 = TreeNode3(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['HalfPosting'][index0] = (address0, self._offset)
        return address0

    def _read_Account(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Account'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_AccountID()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index2, elements1, address3 = 0, self._offset, [], True
            while address3 is not FAILURE:
                index3, elements2 = self._offset, []
                address4 = FAILURE
                chunk0 = None
                if self._offset < self._input_size:
                    chunk0 = self._input[self._offset:self._offset + 1]
                if chunk0 == ':':
                    address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address4 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('":"')
                if address4 is not FAILURE:
                    elements2.append(address4)
                    address5 = FAILURE
                    address5 = self._read_AccountID()
                    if address5 is not FAILURE:
                        elements2.append(address5)
                    else:
                        elements2 = None
                        self._offset = index3
                else:
                    elements2 = None
                    self._offset = index3
                if elements2 is None:
                    address3 = FAILURE
                else:
                    address3 = TreeNode5(self._input[index3:self._offset], index3, elements2)
                    self._offset = self._offset
                if address3 is not FAILURE:
                    elements1.append(address3)
                    remaining0 -= 1
            if remaining0 <= 0:
                address2 = TreeNode(self._input[index2:self._offset], index2, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode4(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['Account'][index0] = (address0, self._offset)
        return address0

    def _read_Amount(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Amount'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_Commodity()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_Quantity()
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
            address0 = TreeNode6(self._input[index2:self._offset], index2, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            index3, elements1 = self._offset, []
            address3 = FAILURE
            address3 = self._read_Quantity()
            if address3 is not FAILURE:
                elements1.append(address3)
                address4 = FAILURE
                address4 = self._read_Commodity()
                if address4 is not FAILURE:
                    elements1.append(address4)
                else:
                    elements1 = None
                    self._offset = index3
            else:
                elements1 = None
                self._offset = index3
            if elements1 is None:
                address0 = FAILURE
            else:
                address0 = TreeNode7(self._input[index3:self._offset], index3, elements1)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
                address0 = self._read_Quantity()
                if address0 is FAILURE:
                    self._offset = index1
        self._cache['Amount'][index0] = (address0, self._offset)
        return address0

    def _read_Commodity(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Commodity'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_Text()
        if address0 is FAILURE:
            self._offset = index1
            chunk0 = None
            if self._offset < self._input_size:
                chunk0 = self._input[self._offset:self._offset + 1]
            if chunk0 == '$':
                address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"$"')
            if address0 is FAILURE:
                self._offset = index1
        self._cache['Commodity'][index0] = (address0, self._offset)
        return address0

    def _read_Quantity(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Quantity'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        remaining0, index2, elements1, address2 = 1, self._offset, [], True
        while address2 is not FAILURE:
            address2 = self._read_Num()
            if address2 is not FAILURE:
                elements1.append(address2)
                remaining0 -= 1
        if remaining0 <= 0:
            address1 = TreeNode(self._input[index2:self._offset], index2, elements1)
            self._offset = self._offset
        else:
            address1 = FAILURE
        if address1 is not FAILURE:
            elements0.append(address1)
            address3 = FAILURE
            index3 = self._offset
            index4, elements2 = self._offset, []
            address4 = FAILURE
            chunk0 = None
            if self._offset < self._input_size:
                chunk0 = self._input[self._offset:self._offset + 1]
            if chunk0 == '.':
                address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address4 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"."')
            if address4 is not FAILURE:
                elements2.append(address4)
                address5 = FAILURE
                remaining1, index5, elements3, address6 = 1, self._offset, [], True
                while address6 is not FAILURE:
                    address6 = self._read_num()
                    if address6 is not FAILURE:
                        elements3.append(address6)
                        remaining1 -= 1
                if remaining1 <= 0:
                    address5 = TreeNode(self._input[index5:self._offset], index5, elements3)
                    self._offset = self._offset
                else:
                    address5 = FAILURE
                if address5 is not FAILURE:
                    elements2.append(address5)
                else:
                    elements2 = None
                    self._offset = index4
            else:
                elements2 = None
                self._offset = index4
            if elements2 is None:
                address3 = FAILURE
            else:
                address3 = TreeNode(self._input[index4:self._offset], index4, elements2)
                self._offset = self._offset
            if address3 is FAILURE:
                address3 = TreeNode(self._input[index3:index3], index3)
                self._offset = index3
            if address3 is not FAILURE:
                elements0.append(address3)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['Quantity'][index0] = (address0, self._offset)
        return address0

    def _read_AccountID(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['AccountID'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 1, self._offset, [], True
        while address1 is not FAILURE:
            index2 = self._offset
            chunk0 = None
            if self._offset < self._input_size:
                chunk0 = self._input[self._offset:self._offset + 1]
            if chunk0 is not None and Grammar.REGEX_1.search(chunk0):
                address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address1 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[a-zA-Z]')
            if address1 is FAILURE:
                self._offset = index2
                index3, elements1 = self._offset, []
                address2 = FAILURE
                chunk1 = None
                if self._offset < self._input_size:
                    chunk1 = self._input[self._offset:self._offset + 1]
                if chunk1 == ' ':
                    address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address2 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('" "')
                if address2 is not FAILURE:
                    elements1.append(address2)
                    address3 = FAILURE
                    chunk2 = None
                    if self._offset < self._input_size:
                        chunk2 = self._input[self._offset:self._offset + 1]
                    if chunk2 is not None and Grammar.REGEX_2.search(chunk2):
                        address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                        self._offset = self._offset + 1
                    else:
                        address3 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('[a-zA-Z]')
                    if address3 is not FAILURE:
                        elements1.append(address3)
                    else:
                        elements1 = None
                        self._offset = index3
                else:
                    elements1 = None
                    self._offset = index3
                if elements1 is None:
                    address1 = FAILURE
                else:
                    address1 = TreeNode(self._input[index3:self._offset], index3, elements1)
                    self._offset = self._offset
                if address1 is FAILURE:
                    self._offset = index2
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['AccountID'][index0] = (address0, self._offset)
        return address0

    def _read_SepDouble(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['SepDouble'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_Sep()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_Sep()
            if address2 is not FAILURE:
                elements0.append(address2)
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
        self._cache['SepDouble'][index0] = (address0, self._offset)
        return address0

    def _read_Sep(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Sep'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 == ' ':
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('" "')
        if address0 is FAILURE:
            self._offset = index1
            chunk1 = None
            if self._offset < self._input_size:
                chunk1 = self._input[self._offset:self._offset + 1]
            if chunk1 == '\t':
                address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"\\t"')
            if address0 is FAILURE:
                self._offset = index1
        self._cache['Sep'][index0] = (address0, self._offset)
        return address0

    def _read_SepPlus(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['SepPlus'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 1, self._offset, [], True
        while address1 is not FAILURE:
            address1 = self._read_Sep()
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['SepPlus'][index0] = (address0, self._offset)
        return address0

    def _read_NL(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['NL'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 == '\n':
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"\\n"')
        self._cache['NL'][index0] = (address0, self._offset)
        return address0

    def _read_Year(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Year'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 is not None and Grammar.REGEX_3.search(chunk0):
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('[0-9]')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            chunk1 = None
            if self._offset < self._input_size:
                chunk1 = self._input[self._offset:self._offset + 1]
            if chunk1 is not None and Grammar.REGEX_4.search(chunk1):
                address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[0-9]')
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                chunk2 = None
                if self._offset < self._input_size:
                    chunk2 = self._input[self._offset:self._offset + 1]
                if chunk2 is not None and Grammar.REGEX_5.search(chunk2):
                    address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('[0-9]')
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    chunk3 = None
                    if self._offset < self._input_size:
                        chunk3 = self._input[self._offset:self._offset + 1]
                    if chunk3 is not None and Grammar.REGEX_6.search(chunk3):
                        address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                        self._offset = self._offset + 1
                    else:
                        address4 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('[0-9]')
                    if address4 is not FAILURE:
                        elements0.append(address4)
                    else:
                        elements0 = None
                        self._offset = index1
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
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['Year'][index0] = (address0, self._offset)
        return address0

    def _read_Month(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Month'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 == '0':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'0\'')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            chunk1 = None
            if self._offset < self._input_size:
                chunk1 = self._input[self._offset:self._offset + 1]
            if chunk1 is not None and Grammar.REGEX_7.search(chunk1):
                address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[1-9]')
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
            address0 = TreeNode(self._input[index2:self._offset], index2, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            index3, elements1 = self._offset, []
            address3 = FAILURE
            chunk2 = None
            if self._offset < self._input_size:
                chunk2 = self._input[self._offset:self._offset + 1]
            if chunk2 == '1':
                address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address3 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'1\'')
            if address3 is not FAILURE:
                elements1.append(address3)
                address4 = FAILURE
                chunk3 = None
                if self._offset < self._input_size:
                    chunk3 = self._input[self._offset:self._offset + 1]
                if chunk3 is not None and Grammar.REGEX_8.search(chunk3):
                    address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address4 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('[0-2]')
                if address4 is not FAILURE:
                    elements1.append(address4)
                else:
                    elements1 = None
                    self._offset = index3
            else:
                elements1 = None
                self._offset = index3
            if elements1 is None:
                address0 = FAILURE
            else:
                address0 = TreeNode(self._input[index3:self._offset], index3, elements1)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
        self._cache['Month'][index0] = (address0, self._offset)
        return address0

    def _read_Day(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Day'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 == '0':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('\'0\'')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            chunk1 = None
            if self._offset < self._input_size:
                chunk1 = self._input[self._offset:self._offset + 1]
            if chunk1 is not None and Grammar.REGEX_9.search(chunk1):
                address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[1-9]')
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
            address0 = TreeNode(self._input[index2:self._offset], index2, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            index3, elements1 = self._offset, []
            address3 = FAILURE
            chunk2 = None
            if self._offset < self._input_size:
                chunk2 = self._input[self._offset:self._offset + 1]
            if chunk2 is not None and Grammar.REGEX_10.search(chunk2):
                address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address3 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[1-2]')
            if address3 is not FAILURE:
                elements1.append(address3)
                address4 = FAILURE
                chunk3 = None
                if self._offset < self._input_size:
                    chunk3 = self._input[self._offset:self._offset + 1]
                if chunk3 is not None and Grammar.REGEX_11.search(chunk3):
                    address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address4 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('[0-9]')
                if address4 is not FAILURE:
                    elements1.append(address4)
                else:
                    elements1 = None
                    self._offset = index3
            else:
                elements1 = None
                self._offset = index3
            if elements1 is None:
                address0 = FAILURE
            else:
                address0 = TreeNode(self._input[index3:self._offset], index3, elements1)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
                index4, elements2 = self._offset, []
                address5 = FAILURE
                chunk4 = None
                if self._offset < self._input_size:
                    chunk4 = self._input[self._offset:self._offset + 1]
                if chunk4 == '3':
                    address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address5 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('\'3\'')
                if address5 is not FAILURE:
                    elements2.append(address5)
                    address6 = FAILURE
                    chunk5 = None
                    if self._offset < self._input_size:
                        chunk5 = self._input[self._offset:self._offset + 1]
                    if chunk5 is not None and Grammar.REGEX_12.search(chunk5):
                        address6 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                        self._offset = self._offset + 1
                    else:
                        address6 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('[0-1]')
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
                    address0 = TreeNode(self._input[index4:self._offset], index4, elements2)
                    self._offset = self._offset
                if address0 is FAILURE:
                    self._offset = index1
        self._cache['Day'][index0] = (address0, self._offset)
        return address0

    def _read_Date(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Date'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_Year()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            chunk0 = None
            if self._offset < self._input_size:
                chunk0 = self._input[self._offset:self._offset + 1]
            if chunk0 == '-':
                address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('\'-\'')
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_Month()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    index2 = self._offset
                    index3, elements1 = self._offset, []
                    address5 = FAILURE
                    chunk1 = None
                    if self._offset < self._input_size:
                        chunk1 = self._input[self._offset:self._offset + 1]
                    if chunk1 == '-':
                        address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                        self._offset = self._offset + 1
                    else:
                        address5 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('\'-\'')
                    if address5 is not FAILURE:
                        elements1.append(address5)
                        address6 = FAILURE
                        address6 = self._read_Day()
                        if address6 is not FAILURE:
                            elements1.append(address6)
                        else:
                            elements1 = None
                            self._offset = index3
                    else:
                        elements1 = None
                        self._offset = index3
                    if elements1 is None:
                        address4 = FAILURE
                    else:
                        address4 = TreeNode10(self._input[index3:self._offset], index3, elements1)
                        self._offset = self._offset
                    if address4 is FAILURE:
                        address4 = TreeNode(self._input[index2:index2], index2)
                        self._offset = index2
                    if address4 is not FAILURE:
                        elements0.append(address4)
                    else:
                        elements0 = None
                        self._offset = index1
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
            address0 = TreeNode9(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['Date'][index0] = (address0, self._offset)
        return address0

    def _read_Text(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Text'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 is not None and Grammar.REGEX_13.search(chunk0):
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('[a-zA-Z]')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index2, elements1, address3 = 0, self._offset, [], True
            while address3 is not FAILURE:
                chunk1 = None
                if self._offset < self._input_size:
                    chunk1 = self._input[self._offset:self._offset + 1]
                if chunk1 is not None and Grammar.REGEX_14.search(chunk1):
                    address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('[a-zA-Z ]')
                if address3 is not FAILURE:
                    elements1.append(address3)
                    remaining0 -= 1
            if remaining0 <= 0:
                address2 = TreeNode(self._input[index2:self._offset], index2, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['Text'][index0] = (address0, self._offset)
        return address0

    def _read_Num(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['Num'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 is not None and Grammar.REGEX_15.search(chunk0):
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('[0-9]')
        self._cache['Num'][index0] = (address0, self._offset)
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
        tree = self._read_Transaction()
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
