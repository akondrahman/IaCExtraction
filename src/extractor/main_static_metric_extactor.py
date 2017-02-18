'''
Akond , Feb 17, 2017
Placeholder for all metric extraction: static, process, chrun
'''
from SmellDetector import SmellDectector
def getAllStaticMetric(full_path_param):
  puppet_specific_metric_for_file = SmellDectector.getQualGenratedMetricForFile(full_path_param)
  print puppet_specific_metric_for_file




test_hg_file=''
test_git_file='/Users/akond/PUPP_REPOS/wikimedia-downloads/cdh4/manifests/pig.pp'
getAllStaticMetric(test_git_file)
