c = [0; 0; 0; 1];
A = [1, 2, 0.5, -1; 3, 2, 1, -1; 1, 1, 1, 0];
b = [0, 0, 1];
lb = [0, 0, 0, -Inf];
ub = [];
ctype = "UUS";
vartype = "CCCC";
sense = 1;
[xmax, fmax, status, extra] = glpk(c, A, b, lb, ub, ctype, vartype, sense)