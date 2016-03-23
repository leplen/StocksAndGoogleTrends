#!/usr/bin/python

import subprocess

plot=subprocess.Popen(['gnuplot','-persist'],stdin=subprocess.PIPE)

plot.stdin.write('set terminal postscript;\n')
plot.stdin.write("set output 'Plot1.ps';\n")
plot.stdin.write("set xlabel 'Google Trends Frequency Change';\n")
plot.stdin.write("set ylabel 'Stock Movement (H-L)/A';\n")
plot.stdin.write("plot './Out2' using 3:2;\n")

