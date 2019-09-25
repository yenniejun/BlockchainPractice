'''
	Practicing implementing/learning Bootstrap technique in statistics
	And also practicing Python
	Also it's really hot in Dallas today so I'm just chilling
	With way too much coffee
	But at least there's A/C

	Used https://machinelearningmastery.com/a-gentle-introduction-to-the-bootstrap-method/
'''


import random

import numpy as np 
from sklearn.utils import resample # This is to test if what I have works correctly

# These are variables I can tinker with
sampleSize = 10
numRepeat = 10

# The stat calculation I want to estimate i.e. mean, std dev, whatever
calculation = lambda list: sum(list) / len(list)


# This is a mock dataset
dataset = np.arange(0,20,0.5)
statOnEntireDataset = calculation(dataset)
bootstrapCalculationList = []
oobCalculationList = []
accuracyErrorList = [] # Accuracy error of bootstrap and oob calculations

for repeat in range(numRepeat):

	# Create sample of size sampleSize, with replacement
	bootstrap = []
	for sample in range(sampleSize):
		randomIndex = random.randint(0, len(dataset) - 1)
		bootstrap.append(dataset[randomIndex])

	# Calculate and store the calculation done on the sample
	bootstrapCalc = calculation(bootstrap)
	bootstrapCalculationList.append(bootstrapCalc)

	# Estimate the skill of model on out-of-bag sample
	oob = [x for x in dataset if x not in bootstrap]
	oobCalc = calculation(oob)
	oobCalculationList.append(oobCalc)

	# Calculate error difference between oob and bootstrap calc
	# For now, this will just be the squared difference error
	error = (bootstrapCalc - oobCalc) ** 2
	accuracyErrorList.append(error)


avgBootstrapEstimate = sum(bootstrapCalculationList) / len(bootstrapCalculationList)
avgOobEstimate = sum(oobCalculationList) / len(oobCalculationList)
avgAccuracyError = sum(accuracyErrorList) / len(accuracyErrorList)

print ('The stat on the full dataset is                : %s' % statOnEntireDataset)
print ('The avg estimate using samples of size %s is   : %s' % (sampleSize, avgBootstrapEstimate))
print ('The avg estimate for OOB samples is.           : %s' % avgOobEstimate)
print ('The avg error rate between the two estimates is: %s' % avgAccuracyError)


# Now, use scikit-learn
# Note: I am only doing this once, but ideally should repeat numRepeat times
boot_skl = resample(dataset, replace=True, n_samples = sampleSize)
oob_skl = [x for x in dataset if x not in boot_skl]
print ('----- Using scikit-learn-------')
print ('Bootstrap Sample avg                           : %s' % str(sum(boot_skl) / len(boot_skl)))
print ('OOB Sample                                     : %s' % str(sum(oob_skl) / len(oob_skl)))

