#! python3
import re

groups = re.match(r"^Hello (\w+)", "Hello world")  # help(re.match)
print(groups[0], groups[1], sep=", ")  # Por defecto sep=" "

groups = re.findall(r".[a|e|i|o|u].", "Hello world")  # help(re.findall)
print(groups)

groups = re.search(r"\w{3}$", "Hello world")  # help(re.search)
print(groups[0])
