#!/usr/bin/python
import string;
import sys;

def parseInput(fname):
        try:
                iFile   = open(fname, 'r');
                iBuffer = iFile.read();
                n       = len(iBuffer);
                maxlen  = 0;
                maxStr  = "";
                for basePos in xrange(0, n):
                        for i in xrange(basePos, n):
                                fwdStr = iBuffer[basePos:i];
                                revStr = fwdStr[::-1];
                                if ( fwdStr == revStr and
                                     maxlen < len(fwdStr)):
                                        maxlen = len(fwdStr);
                                        maxStr = fwdStr;

                print maxStr;
                                        
        except IOError:
		print "I/O error in file ";
parseInput("temp");
