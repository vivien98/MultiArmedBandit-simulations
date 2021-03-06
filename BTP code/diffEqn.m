%% ODE solver for urn model %%

syms y(t);
m00 = 0.7;
m01 = 0.3;
m10 = 0.4;
m11 = 0.5;
p00 = 1;
p01 = 0;
p10 = 0;
p11 = 1;



ode = diff(y,t) == (((y(t))*(p00*m00 + p01*(1-m01)) + (1 - (y(t)))*(p10*m10 + p11*(1-m11))) - y(t))/(20 + t);
cond = y(0) == 0.5;

ySol(t) = dsolve(ode,cond);

pretty(ySol(t));                                
maxTime = 1000;

k = 1:maxTime ;
y1 = zeros(1,maxTime);
for i = 1:maxTime
    t = i;
    y1(i) = eval(ySol) ;
    
end


plot(k,y1)

mat2np(y1, "diffEqnOut.pkl", "float64")