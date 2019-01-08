#!/bin/python
import os

for i in range(1,101):
  os.system("~/Sniper/tools/gen_simout.py --partial=marker-1-" + str(i) + ":marker-1-" + str(i) + " | tee -a \"simall.out\"")
