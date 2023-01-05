#!/usr/bin/env python3
import sys  # importing as a separate namespace
from time import perf_counter # importing into a combined namespace
from sieve import getprimes # also combined namespace from custom module
import matplotlib.pyplot as plt # importing with renaming

def timer(f, *args):
    '''
    Simple function to measure the time taken
    '''
    tstart = perf_counter() # start a timer
    result = f(*args)       # call the function 
    tend   = perf_counter() # stop the timer
    telapsed = tend - tstart
    return result, telapsed

def main():
    # this function is only going to get exectued if we run the program
    # i.e. you can import timer from this module and main() will not run
    n = [10**x for x in range(1, 9)] # build list of N
    times = [timer(getprimes, x) for x in n] # get the times
    
    # matplotlib we used in interactive mode previously
    # but it is just a package with several modules
    # it's also a good example of how objects work 
    fig = plt.figure()        # we're creating a figure object here 
    ax1 = fig.add_subplot(111) # and an axis object 
    ax1.plot(n, [x[1] for x in times], 'k.')
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax2 = ax1.twinx() # create a second pplot with the same x-axis
    ax2.plot(n, [len(x[0]) for x in times], 'r.' )
    ax2.set_yscale('log')
    
    # label our axes
    ax1.set_xlabel('N')
    ax1.set_ylabel('Time to Evaluate Primes to N')
    ax2.set_ylabel('Number of Primes up to N')
    plt.show(fig)
    
if __name__ == '__main__':
    sys.exit(main())
    
    
    