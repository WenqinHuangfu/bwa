#!/bin.python
import os

os.system("perf record -e cycles,instructions,LLC-load-misses,LLC-load ./bwa mem -t 8 /home/shuangchenli/aegilops.fna /home/shuangchenli/1e7_1.fastq > results")
os.system("./bwa mem -t 8 /home/shuangchenli/aegilops.fna /home/shuangchenli/1e7_1.fastq > results")

