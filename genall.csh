#!/bin/csh
set files=(??.tex)
echo $files
foreach f($files)
   set rf = `basename $f .tex`
   sed 's/^\\include.*$/\\include{xyzzyxyzzy}/'  < single.tex | sed "s/xyzzyxyzzy/$rf/" > s.tex
   pdflatex s
   pdflatex s
   pdflatex s
   mv s.pdf $rf.pdf
end
rm s.tex
rm ??.aux
rm s.*
