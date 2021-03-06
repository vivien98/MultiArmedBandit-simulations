% Use the voter model to return the cumulative reward and user proportion
% at a time T
function [reward,prop] = rewardAndPropVoter(b00,b01,b10,b11,p,q,z0,T,A)
reward = 0;
rew = 0;
x = [p,q];
d1 = ((1-x(2))*b10 + x(2)*(1-b11));
d2 = (x(1)*(1-b00) + (1-x(1))*(b01) + d1);
t = 1:T;
zt = d1/d2 + (z0 - d1/d2)*exp(-d2*t/A); 
%rew = zt*(x(1)*b00 + (1-x(1))*b01) + (1-zt)*(x(2)*b11 + (1-x(2))*b10);
%cumRew = sum(rew);
%reward = cumRew;
prop = zt(T);