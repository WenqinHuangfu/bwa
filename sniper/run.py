#!/bin/python
import os
import sys
import subprocess

PATH_sniper = "/home/shuangchenli/Sniper/"

num_threads = 1
exe = "/home/shuangchenli/workspace/bwa/bwa mem -t " + str(num_threads) + " /home/shuangchenli/workspace/bwa/data/GRCh38.fna /home/shuangchenli/workspace/bwa/data/simu.fastq"
#var = ''
var = '_LLCinf'

#os.system(exe) # warm up tlb...
#os.system("rm -rf ./results" + var)
#os.system("mkdir -p ./results" + var)
os.chdir("./results" + var)

#os.system(PATH_sniper + "/run-sniper -c ../E5-2680v3" + var + ".cfg -n " + str(num_threads) + " --roi --no-cache-warming -- " + exe)
#os.system(PATH_sniper + "/run-sniper -c ../E5-2680v3" + var + ".cfg -n " + str(num_threads) + " --roi-script --no-cache-warming -s roi-iter:1:50:100 -s markers:stats " + exe)
#os.system(PATH_sniper + "/run-sniper -c ../E5-2680v3" + var + ".cfg -n " + str(num_threads) + " --roi --no-cache-warming -s markers:stats " + exe)
#os.system(PATH_sniper + "/run-sniper -c ../E5-2680v3" + var + ".cfg -n 16 --roi --no-cache-warming -s markers:stats " + exe)

os.system("cp " + PATH_sniper + "/tools/sniper_stats.py " + PATH_sniper + "/tools/sniper_stats.py.orig")
os.system("cp ../sniper_stats.py " + PATH_sniper + "/tools/sniper_stats.py")
os.system("cp " + PATH_sniper + "/tools/sniper_stats_sqlite.py " + PATH_sniper + "/tools/sniper_stats_sqlite.py.orig")
os.system("cp ../sniper_stats_sqlite.py " + PATH_sniper + "/tools/sniper_stats_sqlite.py")

os.system(PATH_sniper + "/tools/cpistack.py --partial=marker-1-90:marker-1-90 --time | tee \"cpi.out\"")
#os.system(PATH_sniper + "/tools/cpistack.py --time --aggregate -o cpi-stack-agg")
os.system(PATH_sniper + "/tools/mcpat.py --partial=marker-1-90:marker-1-90 | tee \"power.out\"")
os.system("grep -inr \'load_instructions\' ./power.xml | tee \"tmp\"")
f = open('tmp', 'r')
for line in f:
  if(int(line.split("\"")[3]) > 0):
    print "================================="
    print "instruction stats"
    os.system("sed -n "+ str(int(line.split(":")[0]) - 5) + "," + str(int(line.split(":")[0]) + 4) + "p ./power.xml | tee \"instruction.out\"")
    break
os.system("rm -rf ./tmp")
os.system("cp " + PATH_sniper + "/tools/sniper_stats.py.orig " + PATH_sniper + "/tools/sniper_stats.py")
os.system("cp " + PATH_sniper + "/tools/sniper_stats_sqlite.py.orig " + PATH_sniper + "/tools/sniper_stats_sqlite.py")
os.chdir("../")
