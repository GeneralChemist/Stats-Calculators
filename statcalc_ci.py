'''

This program will solve various statistical tasks, given the sample size,
standard deviation, mean and level of confidence.

'''
import math as m

# calculates sample standard dev
def samp_st_dev(n,s):
	return s/m.sqrt(n)

#calculate desired 2 tailed z score
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


def st_er(sx,z):
	return sx*z
	
def interval(x,e):
	print str('Your confidence interval is: [' + str(x-e) + ', ' + str(x+e) + ']')

def main():
	n = int(raw_input('Enter your sample size: '))
	x = float(raw_input('Enter your mean: '))
	s = float(raw_input('Enter your standard deviation: '))
	ci = float(raw_input('Enter your confidence interval in %: '))
	ci = ci/100

	
	interval(x,(st_er(samp_st_dev(n,s),two_side_z(ci)))) 


main()