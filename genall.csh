#!/bin/csh
set files=(??.tex)
echo $files
foreach f($files)
   sed 's/^\\include.*$/\\include{xyzzyxyzzy}/'  < single.tex | sed "s/xyzzyxyzzy/$f/" > s.tex
   pdflatex s
   pdflatex s
   pdflatex s
   set rf = `basename $f .tex`
   mv s.pdf $rf.pdf
end
rm s.tex
