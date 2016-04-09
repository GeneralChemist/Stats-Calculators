'''
This will calculate a bernoulli confidence interval for common confidence intervals
'''

import math as m

def main():
	print "This will calculate a Bernoulli confidence interval."
	print ''
	n = int(raw_input('Enter your sample size: '))
	x = float(raw_input('Enter the number of positive responses: '))
	ci = float(raw_input('Enter your confidence interval in %: '))
	print ''
	ci = ci/100

	p = prop(x,n)
	e = two_side_z(ci)*st_dev(p,n)
	print 'Mean: ' +str(p)
	print 'Sample standard dev: '+ str(st_dev(p,n))
	print "Confidence interval at " +str(ci*100) +"% ["+str(p-e)+', '+str(p+e)+']'

def prop(x,n):
	return x/n

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

def st_dev(p,n):
	return m.sqrt(p*(1-p))/m.sqrt(n)

main()