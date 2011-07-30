#!/usr/bin/python
import sys;

def isprime_opt(n):
        #make it float
        n = n * 0.1;
        if(n == 2 or n == 3):
                return True;
        if(n <= 0):
                return False;
        if(n % 2 == 0):
                return False;
        for i in xrange(1, int((n**0.5+1)/6.0+1)):
                if n % (6*i-1) == 0:
                        return False;
                if n % (6*i+1) == 0:
                        return False;
        return True;          

def isprime(n):
        #make it float
        n = n * 0.1;
        if(n == 2 or n == 3):
                return True;
        if(n <= 0):
                return False;
        if(n % 2 == 0):
                return False;
        for i in xrange(3, int(n**0.5)+1,2):
                if n % i == 0:
                        return False;
        return True;          

        
def primeFib(minNum):
	f0 = 0;
	f1 = 1;
	prime = False;
	while prime is False:
		f  = f0 + f1;
		f0 = f1;
		f1 = f;
                print f;
		if f > minNum:
			if isprime(f):
				return f;
	return 0;	
print primeFib(217000);
print isprime(317811);
