'''
the core part of the DE runner
Akond Rahman, Feb 23, 2017
'''
import de_utility, numpy as np
from DiffEvolOptimizer import DiffEvolOptimizer
from sklearn import decomposition
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
dataset_file="/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/dataset/SYNTHETIC_MOZ_FULL_DATASET.csv"
folds=10
no_features_to_use=5
prev_cart_auc = float(0)
prev_rf_auc   = float(0)

def evaluateCART(paramsForTuning):
  # reff: http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
  global prev_cart_auc
  # 1. read dataset from file
  full_dataset_from_csv = de_utility.getDatasetFromCSV(dataset_file)
  full_rows, full_cols = np.shape(full_dataset_from_csv)
  ## 2. we will skip the first column, as it has file names
  feature_cols = full_cols - 1  ## the last column is defect status, so one column to skip
  all_features = full_dataset_from_csv[:, 2:feature_cols]
  # 3. get labels
  dataset_for_labels = de_utility.getDatasetFromCSV(dataset_file)  ## unlike phase-1, the labels are '1' and '0', so need to take input as str
  label_cols = full_cols - 1
  all_labels  =  dataset_for_labels[:, label_cols]
  ## 4. do PCA, take all features for PCA
  feature_input_for_pca = all_features
  pcaObj = decomposition.PCA(n_components=15)
  pcaObj.fit(feature_input_for_pca)
  ## 5. trabsform daatset based on PCA
  pcaObj.n_components=no_features_to_use
  selected_features = pcaObj.fit_transform(feature_input_for_pca)
  ## 6. plugin model parameters
  #print "lol", paramsForTuning[0]
  if((paramsForTuning[0] <= de_utility.learnerDict['CART'][0][0] ) or (paramsForTuning[1] <= de_utility.learnerDict['CART'][1][0]) or (paramsForTuning[2] <= de_utility.learnerDict['CART'][2][0]) or (paramsForTuning[3] <= de_utility.learnerDict['CART'][3][0])):
    cart_area_under_roc = prev_cart_auc
  elif((paramsForTuning[0] > de_utility.learnerDict['CART'][0][1] ) or (paramsForTuning[1] > de_utility.learnerDict['CART'][1][1]) or (paramsForTuning[2] > de_utility.learnerDict['CART'][2][1]) or (paramsForTuning[3] > de_utility.learnerDict['CART'][3][1])):
    cart_area_under_roc = prev_cart_auc
  else:
    theCARTModel = DecisionTreeClassifier(max_features=paramsForTuning[0], min_samples_split=paramsForTuning[1],
                                        min_samples_leaf=paramsForTuning[2], max_depth=paramsForTuning[3]
                                       )
    cart_area_under_roc = de_utility.perform_cross_validation(theCARTModel, selected_features, all_labels, folds, 'CART')
    #print "asi mama:", cart_area_under_roc
    prev_cart_auc = cart_area_under_roc
  #print "current pointer to AUC:", cart_area_under_roc
  return cart_area_under_roc

def evaluateRF(paramsForTuning):
  #reff: http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
  global prev_rf_auc
  # 1. read dataset from file
  full_dataset_from_csv = de_utility.getDatasetFromCSV(dataset_file)
  full_rows, full_cols = np.shape(full_dataset_from_csv)
  ## 2. we will skip the first column, as it has file names
  feature_cols = full_cols - 1  ## the last column is defect status, so one column to skip
  all_features = full_dataset_from_csv[:, 2:feature_cols]
  only_pupp_features = full_dataset_from_csv[:, 2:14]
  # 3. get labels
  dataset_for_labels = de_utility.getDatasetFromCSV(dataset_file)  ## unlike phase-1, the labels are '1' and '0', so need to take input as str
  label_cols = full_cols - 1
  all_labels  =  dataset_for_labels[:, label_cols]
  ## 4. do PCA, take all features for PCA
  feature_input_for_pca = all_features
  #feature_input_for_pca  = only_pupp_features
  pcaObj = decomposition.PCA(n_components=15)
  pcaObj.fit(feature_input_for_pca)
  ## 5. trabsform daatset based on PCA
  pcaObj.n_components=no_features_to_use
  selected_features = pcaObj.fit_transform(feature_input_for_pca)
  ## 6. plugin model parameters
  #print "lol", paramsForTuning[0]
  if((paramsForTuning[0] <= de_utility.learnerDict['RF'][0][0] ) or (paramsForTuning[1] <= de_utility.learnerDict['RF'][1][0]) or (paramsForTuning[2] <= de_utility.learnerDict['RF'][2][0]) or (paramsForTuning[3] <= de_utility.learnerDict['RF'][3][0]) or (paramsForTuning[4] <= de_utility.learnerDict['RF'][4][0])):
    rf_area_under_roc = prev_rf_auc
  elif((paramsForTuning[0] > de_utility.learnerDict['RF'][0][1] ) or (paramsForTuning[1] > de_utility.learnerDict['RF'][1][1]) or (paramsForTuning[2] > de_utility.learnerDict['RF'][2][1]) or (paramsForTuning[3] > de_utility.learnerDict['RF'][3][1])  or (paramsForTuning[4] > de_utility.learnerDict['RF'][4][1])):
    rf_area_under_roc = prev_rf_auc
  else:
    the_RF_Model = RandomForestClassifier(max_features = paramsForTuning[0],    max_leaf_nodes = int(paramsForTuning[1]),
                                          min_samples_split=paramsForTuning[2], min_samples_leaf=paramsForTuning[3],
                                          n_estimators=int(paramsForTuning[4])
                                         )
    rf_area_under_roc = de_utility.perform_cross_validation(the_RF_Model, selected_features, all_labels, folds, 'RF')
    #print "asi mama:", rf_area_under_roc
    prev_rf_auc = rf_area_under_roc
  print "current pointer to AUC:", rf_area_under_roc
  return rf_area_under_roc

def giveMeFuncNameOfThisLearner(learnerNameP):
   if learnerNameP=='CART':
    func2ret = evaluateCART
   elif learnerNameP=='RF':
    func2ret = evaluateRF
   return func2ret

def evaluateLearners(learnerName):
    '''
    Two things are variable: the paramters to be tuned, and the function of the lewarner
    '''
    limits_of_params   = de_utility.giveMeLimitsOfThisLearner(learnerName)
    print "Loaded required parameter limits of:", learnerName
    fn_name_of_learner = giveMeFuncNameOfThisLearner(learnerName)
    print "Loaded required obj. func of:", learnerName
    '''
    '''
    ngen, npop = 100, 10
    ndim = len(limits_of_params)
    #print limits_of_params
    pop = np.zeros([ngen, npop, ndim])
    loc = np.zeros([ngen, ndim])
    de = DiffEvolOptimizer(fn_name_of_learner, limits_of_params, npop, maximize=True)
    for i, res in enumerate(de(ngen)):
      pop[i,:,:] = de.population.copy()
      loc[i,:] = de.location.copy()
    print "Learner: {}, solution:{}, optimized AUC:{}".format(learnerName, de.location, abs(de.value))
    print "="*100
