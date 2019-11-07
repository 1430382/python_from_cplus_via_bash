## automatic execute
NombreProgramaFuente=runpython
rm $NombreProgramaFuente
g++ $NombreProgramaFuente.cpp -o $NombreProgramaFuente -lm -Wall -O3 -w
./$NombreProgramaFuente
