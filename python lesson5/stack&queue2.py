#queue work in frist in frist out
from collections import deque
bank=deque(["c++","c","java","python","ios","cyber","html","css","js"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
bank.popleft()
bank.popleft()
bank.popleft()
bank.popleft()
bank.popleft()
bank.popleft()
print(bank)
bank.popleft()
if not  bank:
    print("not nay parsons left//")

