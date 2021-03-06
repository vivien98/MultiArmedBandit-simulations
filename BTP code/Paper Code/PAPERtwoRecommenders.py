# BTP code for TWO ARMS ONLY
import numpy as np
import math
import matplotlib.pyplot as pl
import scipy as sp
import matplotlib as mpl

def simulateOPT(nSim,nTime,B,initUrn,initProp):
	randomArrPref = np.random.rand(nSim,nTime);
	randomArrRec = np.random.rand(nSim,nTime);
	randomArrRew = np.random.rand(nSim,nTime);
	avgProp = np.zeros(nTime)
	for i in range(nSim):
		print(str(i))
		urn = np.array([initUrn*initProp,initUrn*(1-initProp)])
		propT = np.zeros(nTime)
		p = float(B[0,0]+B[0,1]-1 > 0)
		q = float(B[1,1]+B[1,0]-1 < 0)
		for j in range(nTime):
			prop = urn/(initUrn+j)
			if prop[0] > randomArrPref[i,j]:   # generating user with some preference
				armPref = 0
			else:
				armPref = 1
			if armPref==0:
				if p > randomArrRec[i,j]:		# generating arm to be shown 
					armChosen = 0
				else:
					armChosen = 1
			else:
				if q > randomArrRec[i,j]:		# generating arm to be shown 
					armChosen = 1
				else:
					armChosen = 0
			if B[armPref,armChosen] > randomArrRew[i,j]: # generating reward
				rew = 1
			else:
				rew = 0
			urn[armChosen] += rew
			urn[1-armChosen] += 1-rew
			propT[j] = prop[0]

		avgProp += propT

	avgProp = avgProp/nSim

	return avgProp

def simulateOPT2(nSim,nTime,B,initUrn,initProp):
	randomArrPref = np.random.rand(nSim,nTime);
	randomArrRec = np.random.rand(nSim,nTime);
	randomArrRew = np.random.rand(nSim,nTime);
	randomArrPop = np.random.rand(nSim,nTime);
	avgProp = np.zeros(nTime)
	avgPopularity00 = np.zeros(nTime)
	avgPopularity11 = np.zeros(nTime)
	for i in range(nSim):
		print(str(i))
		urn = np.array([initUrn*initProp,initUrn*(1-initProp)])
		popMat = initUrn*np.ones((2,2))
		propT = np.zeros(nTime)
		popularity00 = np.zeros(nTime)
		popularity11 = np.zeros(nTime)
		p0 = float(B[0,0]+B[0,1]-1 > 0)
		q0 = float(B[1,1]+B[1,0]-1 < 0)
		p1 = float(B[0,0]+B[0,1]-1 < 0)
		q1 = float(B[1,1]+B[1,0]-1 > 0)
		for j in range(nTime):
			prop = urn/(initUrn+j)
			if prop[0] > randomArrPref[i,j]:   # generating user with some preference
				armPref = 0
			else:
				armPref = 1

			popularityWithS0 = popMat[armPref,0]/(popMat[armPref,1]+popMat[armPref,0])  # generating recommender
			if popularityWithS0 > randomArrPop[i,j]:
				recSys = 0
				p = p0
				q = q0
			else:
				recSys = 1
				p = p1
				q = q1

			if armPref==0:

				if p > randomArrRec[i,j]:		# generating arm to be shown 
					armChosen = 0
				else:
					armChosen = 1
			else:
				if q > randomArrRec[i,j]:		# generating arm to be shown 
					armChosen = 1
				else:
					armChosen = 0
			if B[armPref,armChosen] > randomArrRew[i,j]: # generating reward
				rew = 1
			else:
				rew = 0
			urn[armChosen] += rew
			urn[1-armChosen] += 1-rew
			popMat[armPref,recSys] += rew
			popMat[armPref,1-recSys] += 1-rew
			popularity00[j] = popMat[0,0]/(popMat[0,0]+popMat[0,1])
			popularity11[j] = popMat[1,1]/(popMat[1,0]+popMat[1,1])
			propT[j] = prop[0]


		avgProp += propT
		avgPopularity00 += popularity00
		avgPopularity11 += popularity11

	avgProp = avgProp/nSim
	avgPopularity00 = avgPopularity00/nSim
	avgPopularity11 = avgPopularity11/nSim

	return avgProp,avgPopularity00,avgPopularity11

def simulateGEN2(nSim,nTime,B,initUrn,initProp,p0,q0,p1,q1):
	randomArrPref = np.random.rand(nSim,nTime);
	randomArrRec = np.random.rand(nSim,nTime);
	randomArrRew = np.random.rand(nSim,nTime);
	randomArrPop = np.random.rand(nSim,nTime);
	avgProp = np.zeros(nTime)
	avgPopularity00 = np.zeros(nTime)
	avgPopularity11 = np.zeros(nTime)
	for i in range(nSim):
		print(str(i))
		urn = np.array([initUrn*initProp,initUrn*(1-initProp)])
		popMat = initUrn*np.ones((2,2))
		propT = np.zeros(nTime)
		popularity00 = np.zeros(nTime)
		popularity11 = np.zeros(nTime)
		
		for j in range(nTime):
			prop = urn/(initUrn+j)
			if prop[0] > randomArrPref[i,j]:   # generating user with some preference
				armPref = 0
			else:
				armPref = 1

			popularityWithS0 = popMat[armPref,0]/(popMat[armPref,1]+popMat[armPref,0])  # generating recommender
			if popularityWithS0 > randomArrPop[i,j]:
				recSys = 0
				p = p0
				q = q0
			else:
				recSys = 1
				p = p1
				q = q1

			if armPref==0:

				if p > randomArrRec[i,j]:		# generating arm to be shown 
					armChosen = 0
				else:
					armChosen = 1
			else:
				if q > randomArrRec[i,j]:		# generating arm to be shown 
					armChosen = 1
				else:
					armChosen = 0
			if B[armPref,armChosen] > randomArrRew[i,j]: # generating reward
				rew = 1
			else:
				rew = 0
			urn[armChosen] += rew
			urn[1-armChosen] += 1-rew
			popMat[armPref,recSys] += rew
			popMat[armPref,1-recSys] += 1-rew
			popularity00[j] = popMat[0,0]/(popMat[0,0]+popMat[0,1])
			popularity11[j] = popMat[1,1]/(popMat[1,0]+popMat[1,1])
			propT[j] = prop[0]


		avgProp += propT
		avgPopularity00 += popularity00
		avgPopularity11 += popularity11

	avgProp = avgProp/nSim
	avgPopularity00 = avgPopularity00/nSim
	avgPopularity11 = avgPopularity11/nSim

	return avgProp,avgPopularity00,avgPopularity11




def simulateTHO2(nSim,nTime,B,initUrn,initProp):
	randomArrPref = np.random.rand(nSim,nTime);
	randomArrRec = np.random.rand(nSim,nTime);
	randomArrRew = np.random.rand(nSim,nTime);
	randomArrReci = np.random.rand(nSim,nTime);
	randomArrRewi = np.random.rand(nSim,nTime);
	randomArrPop = np.random.rand(nSim,nTime)
	avgProp = np.zeros(nTime)
	avgReg = np.zeros(nTime)
	avgPopularity00 = np.zeros(nTime)
	avgPopularity11 = np.zeros(nTime)
	for i in range(nSim):
		print(str(i))
		urn = np.array([initUrn*initProp,initUrn*(1-initProp)])
		propT = np.zeros(nTime)
		regT = np.zeros(nTime)
		popMat = initUrn*np.ones((2,2))
		popularity00 = np.zeros(nTime)
		popularity11 = np.zeros(nTime)
		prevReg = 0
		p = 0.5
		q = 0.5
		pi = float(B[0,0]+B[0,1]-1 > 0) # p and q were the matrix known
		qi = float(B[1,1]+B[1,0]-1 < 0)
		alpha0 = np.ones((2,2))
		beta0 = np.ones((2,2))
		alpha1 = np.ones((2,2))
		beta1 = np.ones((2,2))
		for j in range(nTime):
			prop = urn/(initUrn+j)
			if prop[0] > randomArrPref[i,j]:   # generating user with some preference
				armPref = 0
			else:
				armPref = 1

			popularityWithS0 = popMat[armPref,0]/(popMat[armPref,1]+popMat[armPref,0])  # generating recommender
			if popularityWithS0 > randomArrPop[i,j]:
				recSys = 0
				sampleMat = np.random.beta(alpha0,beta0)  # sampling a matrix
				if(sampleMat[0,0] + sampleMat[0,1] - 1 > 0):
					p = 1
				else:
					p = 0
				if(sampleMat[1,1] + sampleMat[1,0] - 1 < 0):
					q = 1
				else:
					q = 0
			else:
				recSys = 1
				sampleMat = np.random.beta(alpha1,beta1)  # sampling a matrix
				if(sampleMat[0,0] + sampleMat[0,1] - 1 < 0):
					p = 1
				else:
					p = 0
				if(sampleMat[1,1] + sampleMat[1,0] - 1 > 0):
					q = 1
				else:
					q = 0

			
			

			if armPref==0:
				if p > randomArrRec[i,j]:		# generating arm to be shown 
					armChosen = 0
				else:
					armChosen = 1

				if pi > randomArrReci[i,j]:		# generating arm to be shown for known B case
					armChoseni = 0
				else:
					armChoseni = 1

			else:
				if q > randomArrRec[i,j]:		# generating arm to be shown 
					armChosen = 1
				else:
					armChosen = 0

				if qi > randomArrReci[i,j]:		# generating arm to be shown for known B case
					armChoseni = 1
				else:
					armChoseni = 0
			if B[armPref,armChosen] > randomArrRew[i,j]: # generating reward
				rew = 1
			else:
				rew = 0

			if B[armPref,armChoseni] > randomArrRewi[i,j]: # generating reward
				rewi = 1
			else:
				rewi = 0

			thompsonFactor = 2
			if recSys == 0:
				alpha0[armPref,armChosen] += thompsonFactor*rew
				beta0[armPref,armChosen] += thompsonFactor*(1 - rew)
			else:
				alpha1[armPref,armChosen] += thompsonFactor*rew
				beta1[armPref,armChosen] += thompsonFactor*(1 - rew)

			popMat[armPref,recSys] += rew
			popMat[armPref,1-recSys] += 1-rew
			popularity00[j] = popMat[0,0]/(popMat[0,0]+popMat[0,1])
			popularity11[j] = popMat[1,1]/(popMat[1,0]+popMat[1,1])

			urni = [0.0,0.0]
			prevZ = urn[0]
			prevZi = urni[0]
			urn[armChosen] += rew
			urn[1-armChosen] += 1-rew
			urni[armChoseni] += rewi
			urni[1-armChoseni] += 1-rewi
			delZ = urn[0] - prevZ
			delZi = urni[0] - prevZi
			propT[j] = prop[0]
			regT[j] = prevReg + delZi - delZ
			prevReg = regT[j]

		avgProp += propT
		avgReg += regT
		avgPopularity00 += popularity00
		avgPopularity11 += popularity11


	avgProp = avgProp/nSim
	avgReg = avgReg/nSim
	avgPopularity00 = avgPopularity00/nSim
	avgPopularity11 = avgPopularity11/nSim

	return avgProp,avgReg,avgPopularity00,avgPopularity11


#___________________________________________________________MAIN___________________________________________________________#

b00 = 0.7 # initialise bernoulli reward matrix # 7568
b01 = 0.1
b10 = 0.3
b11 = 0.9
B = np.matrix([[b00,b01],[b10,b11]])

nSim = 100
nTime = 1000
initUrn = 20
initProp = 0.5
tThresh = 150

out1 = simulateOPT(nSim,nTime,B,initUrn,initProp)
out2,pop00,pop11 = simulateOPT2(nSim,nTime,B,initUrn,initProp)
#out3,reg3,popth00,popth11 = simulateTHO2(nSim,nTime,B,initUrn,initProp)
out3,popth00,popth11 = simulateGEN2(nSim,nTime,B,initUrn,initProp,0.5,0.5,1,1)


pl.subplot(1,2,1)
pl.plot(out1 , 'r-',label='Optimal policy with 1 RS',linewidth = 2.5)				# POPULATION PROPORTION PLOTTING # NORMAl
pl.plot(out2 ,'b',label='Optimal policy with 2 RS',linewidth = 2.5)
pl.plot(out3 ,'g--',label='TS policy with 2 RS',linewidth = 2.5)
pl.legend(loc='upper right',frameon=True,prop={"size":20})
pl.xlabel('Time',fontsize=20)
pl.ylabel('Proportion of Type 1 users',fontsize=20)
pl.tick_params(labelsize=20);
pl.subplot(1,2,2)
pl.plot(pop00 ,'r',label='Popularity of S1 with type 1',linewidth = 2.5)			# REGRET PLOTTING
pl.plot(pop11 ,'b',label='Popularity of S2 with type 2',linewidth = 2.5)
pl.plot(popth00 ,'c--',label='ThPopularity of S1 with type 1',linewidth = 2.5)			# REGRET PLOTTING
pl.plot(popth11 ,'g-.',label='ThPopularity of S2 with type 2',linewidth = 2.5)
pl.legend(loc='upper right',frameon=True,prop={"size":20})
pl.xlabel('Time',fontsize=20)
pl.ylabel('Popularity',fontsize=20)
pl.tick_params(labelsize=20);
pl.show()

# pl.subplot(1,2,1)
# pl.plot(out1 , 'r-',label='Optimal policy',linewidth = 2.5)				# POPULATION PROPORTION PLOTTING #LOG
# pl.plot(out2 ,'b--',label='ETC policy',linewidth = 2.5)
# pl.plot(out3 ,'g-.',label='TS policy',linewidth = 2.5)
# pl.legend(loc='lower right',frameon=True,prop={"size":20})
# pl.xlabel('Time',fontsize=20)
# pl.ylabel('Proportion of Type 1 users',fontsize=20)
# pl.tick_params(labelsize=20);
# pl.subplot(1,2,2)
# pl.plot(reg2 ,'b-',label='Regret for ETC policy',linewidth = 2.5)			# REGRET PLOTTING LOG
# pl.plot(reg3 ,'g--',label='Regret for TS policy',linewidth = 2.5)
# pl.legend(loc='upper left',frameon=True,prop={"size":20})
# pl.xscale("log")
# pl.xlabel('Time',fontsize=20)
# pl.ylabel('Cumulative Regret',fontsize=20)
# pl.tick_params(labelsize=20);
# pl.show()
