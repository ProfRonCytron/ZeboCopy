#!/bin/csh
set files=(??.tex ???.tex)
echo $files
foreach f($files)
   csh ./genone.csh $f
end
rm s.tex
rm ??.aux
rm s.*
