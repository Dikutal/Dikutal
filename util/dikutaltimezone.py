from datetime import datetime, tzinfo, timedelta

class TZUTC(tzinfo):
    '''
    UTC.
    '''
    def utcoffset(self, dt):
        return timedelta(hours=0)

    def dst(self, dt):
        return timedelta(hours=0)

    def tzname(self,dt):
        return "UTC"

class TZCopenhagen(tzinfo):
    '''
    Copenhagen timezone.
    '''
    def utcoffset(self, dt):
        return timedelta(hours=1) + self.dst(dt)

    def dst(self, dt):
        # DST starts last Sunday in March and ends last Sunday in October.
        d = datetime(dt.year, 4, 1)
        self.dston = d - timedelta(days=d.weekday() + 1)
        d = datetime(dt.year, 11, 1)
        self.dstoff = d - timedelta(days=d.weekday() + 1)
        if self.dston <= dt.replace(tzinfo=None) < self.dstoff:
            return timedelta(hours=1)
        else:
            return timedelta(0)

    def tzname(self,dt):
        return "Europe/Copenhagen"

utc = TZUTC()
copenhagen = TZCopenhagen()

