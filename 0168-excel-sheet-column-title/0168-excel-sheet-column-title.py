class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""

        while columnNumber > 26:
            if columnNumber % 26 == 0:
                columnNumber = columnNumber // 26
                columnNumber -= 1
                res = 'Z' + res
            else:
                rem = columnNumber % 26
                res = chr(64 + rem) + res
                columnNumber = columnNumber // 26

        res = chr(64 + columnNumber) + res

                




        # if columnNumber > 26 and columnNumber % 26 == 0:
        #     columnNumber = columnNumber // 26
        #     columnNumber -= 1
        #     res = 'Z' + res
        #     while columnNumber > 26:
        #         rem = columnNumber % 26
        #         res = chr(64 + rem) + res
        #         columnNumber = columnNumber // 26
        #     res = chr(64 + columnNumber) + res
        # else:
        #     while columnNumber > 26:
        #         rem = columnNumber % 26
        #         res = chr(64 + rem) + res
        #         columnNumber = columnNumber // 26
        #     res = chr(64 + columnNumber) + res

        return res
    