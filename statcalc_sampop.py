'''
This program will calculate the desired population size given a 
desired confidence interval error and standard deviation.
'''
import math as m

def two_side_z(ci):
	if ci == 0.8:
		z = 1.28
	elif ci == 0.9:
		z = 1.645
	elif ci == 0.95:
		z = 1.96
	elif ci == 0.98:
		z = 2.33
	elif ci == 0.99:
		z = 2.58
	return z

def population(z,e,s):
	return (z*s/e)**2

def main():
	e = float(raw_input('Enter your margin of error: '))
	s = float(raw_input('Enter your standard deviation: '))
	ci = float(raw_input('Enter your confidence interval in %: '))
	ci = ci/100
	print ''

	print "Your sample size should be: " + str(m.ceil(population(two_side_z(ci),e,s)))
	


main()