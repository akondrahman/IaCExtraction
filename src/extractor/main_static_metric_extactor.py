'''
Akond , Feb 17, 2017
Placeholder for all metric extraction: static, process, chrun
'''
from SmellDetector import SmellDectector
import lint_metric_extractor



def getAllStaticMetric(full_path_param):
  puppet_specific_metric_for_file = SmellDectector.getQualGenratedMetricForFile(full_path_param)
  print puppet_specific_metric_for_file
  lint_specific_metric_for_file     = lint_metric_extractor.getLintMetrics(full_path_param)
  print lint_specific_metric_for_file






test_hg_file='/Users/akond/PUPP_REPOS/mozilla-releng-downloads/relabs-puppet/manifests/site.pp'
test_git_file='/Users/akond/PUPP_REPOS/wikimedia-downloads/cdh4/manifests/pig.pp'
getAllStaticMetric(test_hg_file)
