c = [1; 1; 3; 2; 4];
A = [1 , 0 , 1 , 0 , 1;
       0 , 0 , -1 , 1 , 0;
       -1 , 1 , 0 , 0 , 0;
       0 , 1 , 0 , 1 , 1;]
b = [2; 1; -1; 2];
lb = [];
ub = [1, 2, 1, 3, 2];
ctype = "SSSS";
vartype = "CCCCC";
sense = 1;
[xmax, fmax, status, extra] = glpk(c, A, b, lb, ub, ctype, vartype, sense)
