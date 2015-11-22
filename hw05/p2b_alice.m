c = [1; 0; 0; 0; 0; 0; 0; 0; 0];
A = [1, 4, 4, -6, -6, -4, -4, 2, 2;
     1, 4, 4, -6, -6, -6, -4, -6, -4;
     1, -2, 4, -2, 4, -4, -4, 2, 2;
     1, -2, 4, -2, 4, -6, -4, -6, -4;
     0, 1, 1, 1, 1, 1, 1, 1, 1];
b = [0; 0; 0; 0; 1]
lb = [-Inf, 0, 0, 0, 0, 0, 0, 0, 0];
ub = [];
ctype = "UUUUS";
vartype = "CCCCCCCCC";
sense = -1; % maximization
[xmax, fmax, status, extra] = glpk(c, A, b, lb, ub, ctype, vartype, sense)
