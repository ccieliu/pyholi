# pyholi
The holiday checker, return if a date is a holiday in China/Japan/Korea

```python
myresult=pyholi.pyholi(mydate,"ZH")
if myresult == 0:
    print("Not a Zh-Cn legal holidays")
elif myresult==1:
    print("legal holidays")
elif myresult==2:
    print("legal holidays but need work")

print("Weekend:",pyholi.checkweekend(mydate))
country can be "ZH" "JP" "KR"  (ignore case)
mydate can be "2017-01-01" or "2017-1-1"
```