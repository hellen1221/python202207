# ReDemo.py

import re

# result = re.search("[0-9]*th", "35th")
# print(result) 
# print(result.group())

# result = re.match("[0-9]*th", "35th")
# print(result)
# print(result.group())


result = re.search("[0-9]*th", "   35th")
print(result) 
print(result.group())

# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

print(bool(re.search("apple", "this is apple")))
print(bool(re.match("apple", "this is apple")))

result = re.search("\d{4}", "올해는 2022년입니다")
print(result.group())

result = re.search("\d{5}", "우리동네는 52100입니다")
print(result.group())
