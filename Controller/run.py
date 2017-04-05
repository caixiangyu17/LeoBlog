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
try:
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(unittest.makeSuite(TestManager))
    failedNumber = 0
    for index, fail in enumerate(result.failures, start=0):
        print(P + "Fail {} -----------> {}".format(index, fail[0]._testMethodName))
        print(O + fail[1])
        failedNumber += 1

    for index, error in enumerate(result.errors, start=0):
        print(P + "Error {} -----------> {}".format(index, error[0]._testMethodName))
        print(O + error[1])

    print(G + "Tests#: {}, Pass: {}, Fail: {}, Error: {}".format(result.testsRun,
                                                                 result.testsRun - len(result.errors) - failedNumber,
                                                                 failedNumber,
                                                                 len(result.errors)))
    output = p.stdout.read()
    # print(output)
except error:
    print(P + error)
finally:
    # print()
    print(stream.read())
    p.terminate()
