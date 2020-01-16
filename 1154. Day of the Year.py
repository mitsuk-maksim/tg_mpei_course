# https://leetcode.com/problems/day-of-the-year/

import datetime
class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        return int((datetime.datetime(year,month,day) - datetime.datetime(year,1,1)).days + 1)
