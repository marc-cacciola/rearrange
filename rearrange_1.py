#!/usr/bin/env python3
import re
def rearrange_name(name):
  result = re.search(r"^(\w*), (\w*) (.*)$", name)
  if result == None:
    return name
  return "{} {} {}".format(result[2], result[3], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)
