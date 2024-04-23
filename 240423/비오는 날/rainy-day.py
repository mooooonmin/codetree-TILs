class Forecast():
    def __init__(self, date, weekday, whether):
        self.date = date
        self.weekday = weekday
        self.whether = whether

    def __repr__(self):
        return " ".join([self.date, self.weekday, self.whether])

n = int(input())
ans = Forecast('2101-12-31', '', '')

for _ in range(n):
    day, weekday, whether = input().split()
    f = Forecast(day, weekday, whether)
    if whether == 'Rain':
        if ans.date > f.date:
            ans = f

print(ans)