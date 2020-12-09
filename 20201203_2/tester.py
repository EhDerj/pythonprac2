# WARNING! in .in file should be only 1 empty string in the end
from task import *
code = ""
while s := input():
    code = "\n".join((code, s))

exec(code)