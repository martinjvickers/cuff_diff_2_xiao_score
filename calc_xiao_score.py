#!/usr/bin/python
import os, sys, shutil, string
import subprocess
from operator import itemgetter, attrgetter
import math
 
 
 
def main( afile ):
 
   f_in = open( afile )
 
   lno = 0
   for line in f_in :
      line = line.strip()
      vars = line.split()
      if lno == 0 :
         line += "\tXiaoScore"
      else :
         #print vars
         LFC = float(vars[9])
         pval = float(vars[11])
         #print LFC,pval
         lp = math.log10(pval)
         xscore = -1 * lp * LFC
         line += "\t"+str(xscore)
      print line
 
      lno += 1
 
 
   f_in.close()
 
 
 
def doit( argv ) :
 
    if len(argv) < 2:
       print "Reads diff exp table from cuff diff and gets p-value x LFC"
       print "USAGE: $0 <cuff diff file e.g. vickers_gene_exp.diff>"
       exit(0)
 
    afile = argv[1]
    main( afile )
 
#
# Argument: file.fasta minSize
#
doit(sys.argv)
