#!/bin/csh
set f=$1
set rf = `basename $f .tex`
echo $rf
sed 's/^\\include.*$/\\include{xyzzyxyzzy}/'  < single.tex | sed "s/xyzzyxyzzy/$rf/" > s.tex
pdflatex s
pdflatex s
mv s.pdf $rf.pdf
#
#
rm s.tex
rm ??.aux
rm s.*
