%% ODE solver for urn model %%

syms y(t);
m00 = 0.7;
m01 = 0.3;
m10 = 0.4;
m11 = 0.5;
p00 = 0.5;
p01 = 0.5;
p10 = 0;
p11 = 1;

ode = diff(y,t) == (((y(t))*(p00*m00 + p01*(1-m01)) + (1 - (y(t)))*(p10*m10 + p11*(1-m11))) - y(t))/(20 + t);
cond = y(0) == 0.5;

ySol(t) = dsolve(ode,cond);

pretty(ySol(t));                                

time = 1:1:100 ;
y = zeros(100);
for i = 1:100
   t = i;
   y(i) = subs(ySol) ;
end

plot(time,y)