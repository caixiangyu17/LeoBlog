import subprocess
from io import StringIO
import unittest
from Test.TestManager import TestManager

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple

stream = StringIO()
p = subprocess.Popen(['python', 'Main.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
runner = unittest.TextTestRunner(stream=stream)
result = runner.run(unittest.makeSuite(TestManager))
failedNumber = 0
for index, fail in enumerate(result.failures, start=0):
    print(P + "Fail {} -----------> {}".format(index, fail[0]._testMethodName))
    print(O + fail[1])
    failedNumber += 1
if failedNumber == 0:
    print(G + "Wow, All Passed.")
else:
    print(P + "There are {} test(s) failed.".format(failedNumber))
p.terminate()
