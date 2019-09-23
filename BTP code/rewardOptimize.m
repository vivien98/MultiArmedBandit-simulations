b00 = 0.95;
b01 = 0.3;
b10 = 0.1;
b11 = 0.6;
lb = [0,0];
ub = [1,1];
A = [];
b = [];
Aeq = [];
beq = [];
x0 = [0.5,0.5];
x = fmincon(@rewardAvg,x0,A,b,Aeq,beq,lb,ub)

[X,Y] = meshgrid(0:0.05:1);
Z = -(((1-Y)*b10 + Y*(1-b11))./(X*b00 + (1-X)*(1-b01) - 1 - ((1-Y)*b10 + Y*(1-b11)))).*(X*b00 + (1-X)*b01) + (1+(((1-Y)*b10 + Y*(1-b11))./(X*b00 + (1-X)*(1-b01) - 1 - ((1-Y)*b10 + Y*(1-b11))))).*(Y*b11 + (1-Y)*b10);
surf(X,Y,Z)

% b00 = 0.7;
% b01 = 0.2;  
% b10 = 0.6;
% b11 = 0.6;