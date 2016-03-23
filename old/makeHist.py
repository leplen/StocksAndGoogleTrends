#!/usr/bin/python

import subprocess

plot=subprocess.Popen(['gnuplot','-persist'],stdin=subprocess.PIPE)

plot.stdin.write('set terminal postscript;\n')
plot.stdin.write("set output 'Histogram.ps';\n")
plot.stdin.write("set ylabel 'Counts';\n")
plot.stdin.write("set xlabel 'Stock Movement (H-L)/A for Trend increase of 2 times of more';\n")
plot.stdin.write("set style histogram clustered gap 1;\n")
plot.stdin.write("binwidth=0.05;\n")
plot.stdin.write("bin(x,width)=width*floor(x/width) + binwidth\n")
plot.stdin.write("set boxwidth binwidth\n")
plot.stdin.write("plot './Out2' u (bin($2,binwidth)):(1.0) smooth freq with boxes;\n")

