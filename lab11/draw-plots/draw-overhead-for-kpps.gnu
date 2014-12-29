# Create plot showing overhead (in seconds) for different traffic rates.
# Traffic is measured in kilopackets per second (kpps).
# We use a CSV file as input.
#
# Input file is memwalk-overhead-for-kpps.csv. Output file is
# overhead-for-kpps.pdf.
#
# Run using: gnuplot draw-overhead-for-kpps.gnu

set autoscale
unset log
unset label
unset key
set term pdf
set output 'overhead-for-kpps.pdf'
set datafile separator ','
set xlabel 'Kilopackets per Second (kpps)'
set ylabel 'Running Time Overhead (seconds)'
set title 'Overhead for Different Traffic Rates'
plot 'memwalk-overhead-for-kpps.csv' with linespoints
