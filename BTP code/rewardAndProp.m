% Use the polya urn model to return the cumulative reward and user proportion
% at a time T
function [reward,prop] = rewardAndProp(b00,b01,b10,b11,p,q,z0,T,A)
reward = 0;
x = [p,q];
c = ((1-x(2))*b10 + x(2)*(1-b11));
a = (x(1)*b00 + (1-x(1))*(1-b01) - 1 - c);
t = 1:T;

zt = -c/a + (z0 + c/a)*(1 + t/A).^(a);     %% Uncomment this to get prop time series
%rew = zt*(x(1)*b00 + (1-x(1))*b01) + (1-zt)*(x(2)*b11 + (1-x(2))*b10);
%cumRew = sum(rew);
%reward = cumRew;
prop = zt(T);