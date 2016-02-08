newcoloncancer
======

This repository contains the source code for a machine learning 
algorithm using scikit-learn and the SEER cancer data. 
The app asks for input from a user and outputs the predicted survival curve based on the input data.

The model in the COLONCLASSIFIER folder is a sklearn
 RandomForestClassifier object that implements the transformation of censored
 data to a form appropriate for machine learning algorithms as described here:

http://www.benkuhn.net/survival-trees

rf = RandomForestClassifier(n_estimators=25,min_samples_split=3,
                             max_depth = 10,
                            max_features = .5,
                             n_jobs=5,verbose=2,random_state=3)



# coloncancer
"# colocancerrferrors" 
