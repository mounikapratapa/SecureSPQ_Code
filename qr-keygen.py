import sys
from miller_rabin_test import is_prime
import time
start_time = time.time()
# f() is the function to implement
# The convention we'll use is that f(i)=0 denotes a quadratic residue
# (1), and f(i)=1 denotes a non-residue (-1)
f = [0] * 35 + [1] * 6
a = 11
b = 42
k = 41

'''a = 151
b = 168
k = 100
'''
'''k =256 
a=53
b=378'''
'''a = 31
b = 1938
k = 128'''
sequence = [a + i * b for i in range(k)]


# The power of an factor a in integer b
# Returns an integer n where b=a^n*c
def compute_power(a, b):
    power = 0
    while gcd(a, b) > 1:
        b = int(b / a)
        power += 1
    return power


# Convert elements from function codomain to Legendre symbols
def map_fn_to_symbol(x):
    if x == 0:
        return 1
    elif x == 1:
        return -1


# Return the index of the first non-zero element in a vector a
def find_first_nonzero(a_row):
    for i in range(len(a_row)):
        if a_row[i] != 0:
            return i


# Given a symbol s\in {1,-1} and a prime p, return a random element in
# Z^*_p with symbol s
def find_random_element_with_symbol(s, p):
    while True:
        x = randint(1, p - 1)
        if kronecker(x, p) == s:
            return x


# Determine the set of unique prime factors seen across a sequence
# Ignores prime factors of even power
def compute_factor_base():
    factor_base = []
    for sequence_value in sequence:
        for prime_factor in factor(sequence_value):
            if prime_factor[1] % 2 == 1:
                if prime_factor[0] not in factor_base:
                    factor_base.append(prime_factor[0])
    return factor_base


# Returns a matrix A of the sequence expressed as a linear system in
# GF(2). Rows represent each element of the sequence. Columns represent
# the presence or absence of each prime factor in that sequence number.
# The last column represents the intented function output at that
# sequence number s, i.e. f(s)
def compute_linear_system(factor_base):
    # Build the linear system.
    system_of_congruences = []

    # For each element i of seq, create a binary vector corresponding to
    # whether j is an odd factor of i
    for i in range(len(sequence)):
        sequence_value = sequence[i]

        # For prime factor of the factor base, check whether it is present
        # in the given sequence number
        for prime_factor in factor_base:
            if compute_power(prime_factor, sequence_value) % 2 == 1:
                system_of_congruences.append(1)
            else:
                system_of_congruences.append(0)
        # Append function value
        system_of_congruences.append(f[i])

    M = MatrixSpace(GF(2), k, len(factor_base) + 1)
    return M(system_of_congruences)


# Return a squre-free prime number satisfying the system of congruence
# specified in li and factor_base
def compute_prime(li, factor_base):
    p = crt(li, factor_base)
    x = prod(factor_base)

    while not is_prime(p) or (p % 4 != 1):
        p = p + x

    return p


# ------------------------------------------------------------
def run():
    factor_base = compute_factor_base()

    if 2 in factor_base:
        print "ERROR: Factor base contains 2, which may lead to inconsistant results. Please select a sequence containing only odd integers"
        return

    A = compute_linear_system(factor_base)

    # Row-reduce echelon A
    A_reduced = A.echelon_form()
    
    

    print ""
    print "Here's the factored elements of the sequence:"
    #for i in sequence:
        #print factor(i)
    print ""
    print "Here are the unique odd-powered factors of the elements of the sequence"
    print factor_base
    print ""
    print "Here's a GF(2) matrix showing the system of equations."
    print "Each row is a sequence number. Each column is a prime factor, except for the last column, which is what the function should evaluate to."
    #print A
    print ""
    print "Here's the matrix in row-reduced echelon form"
    #print A_reduced
    print("system to matrix space--- %s seconds ---" % (time.time() - start_time))
    

    # Check is system is inconsistant
    for row in A_reduced.rows():

        # Check if all elements of the row (except for the last column) are
        # zero. If so, there's no solution for this variable and the system
        # is inconsistant
        if row[0:-1].is_zero():
            inconsistant = True
            print "ERROR: System is inconsistent. Pick a different a,b"
            return
    
    print("Checkinf for consistency--- %s seconds ---" % (time.time() - start_time))
    

    prime_factor_symbols = [1] * len(factor_base)

    # For each row, find the index of the first non-zero element.
    for row in A_reduced.rows():
        # Set the symbol of that factor to the function value
        # Symbol of -1 if row[-1]=0, and Symbol of 1 if row[-1]=1
        prime_factor_symbols[find_first_nonzero(row)] = map_fn_to_symbol(
            int(row[-1]))

    print ""
    #for i in range(len(factor_base)):
        #print str(factor_base[i]) + " needs Legendre symbol " + str(
         #int(prime_factor_symbols[i]))
    print ""
    print "ai = " + str(factor_base)

    # Find random elements mod each of the factors of the factor base with
    # the required symbols
    li = []
    for i in range(len(factor_base)):
        li.append(
            find_random_element_with_symbol(prime_factor_symbols[i],
                                            factor_base[i]))
    #print "li = " + str(li)
    
    print("Finding b_i--- %s seconds ---" % (time.time() - start_time))
    

    p = compute_prime(li, factor_base)

    print "p = " + str(p)
    
    print("CRT--- %s seconds ---" % (time.time() - start_time))

    print ""
    print(sequence)
    print "Testing symbols of sequence modulo p:"
    for i in range(len(sequence)):
        print kronecker(sequence[i], p)
        if map_fn_to_symbol(f[i]) != kronecker(sequence[i], p):
            print "ERROR: symbols of sequence not implement function f"
            return
    print "SUCCESS: Symbols of sequence modulo p implement function f"


# ---------
run()
