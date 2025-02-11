"""1344. Angle Between Hands of a Clock"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        '''
        We need to find the angle of hour and minute hand. For minute hand, we can take the complete 360 deg
        to be divided by 60 that gives us 6 deg for 1 minute and for hour hand, we can take the complete
        360 deg by 12 (hours) which gives us 30 deg for each hour and we need to add the hour hand that is
        moved according to the minute hand,
        '''
        hour_angle = (hour % 12) * 30 + minutes / 2
        minutes_angle = minutes * 6
        res = abs(hour_angle - minutes_angle)
        if res > 180:
            return abs(360 - res)
        return res
