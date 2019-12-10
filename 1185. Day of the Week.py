# https://leetcode.com/problems/day-of-the-week/

class Solution:
    def f_check_leap_year(self,year):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return 1
        else:
            return 0

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        m_day_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        m_day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def f_days_since(day,month,year):
            num_days = 0
            for x in range(year - 1, 1970, -1):
                num_days += 365 + self.f_check_leap_year(x)
            num_days += sum(m_day_in_month[:month-1])
            num_days += day
            if month > 2:
                num_days += self.f_check_leap_year(year)
            return num_days

        start = f_days_since(14,9,2019)
        d = f_days_since(day,month,year)
        return m_day_of_week[(d - start) % 7]
