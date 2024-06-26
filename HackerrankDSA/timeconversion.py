#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    original_time = datetime.strptime(s, "%I:%M:%S%p")
    # convert
    conva = original_time.strftime("%H:%M:%S")
    return conva


if __name__ == "__main__":

    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = str(input())

    result = timeConversion(s)

    fptr.write(result + "\n")

    fptr.close()
