'''
Akond , Feb 17, 2017
Placeholder for all metric extraction: static, process, chrun
'''
from SmellDetector import SmellDectector
import lint_metric_extractor, git_churn_extractor, hg_churn_extractor, static_metric_utility
MOZFLAG='moz'


def getAllStaticMetric(full_path_param, repo_path_param, full_file_map_dict_param):
  # get the file's defect status
  defect_status_of_file           =  full_file_map_dict_param[full_path_param]
  puppet_specific_metric_for_file =  SmellDectector.getQualGenratedMetricForFile(full_path_param)
  print puppet_specific_metric_for_file
  print "Generated the Puppet specific metrics ... "
  print "-"*100
  lint_specific_metric_for_file   =  lint_metric_extractor.getLintMetrics(full_path_param)
  print lint_specific_metric_for_file
  print "Generated the Puppet lint metrics ... "
  print "-"*100
  if(MOZFLAG in full_path_param):
   relative_churn_metrics         =  hg_churn_extractor.getRelativeChurnMetrics(full_path_param, repo_path_param)
  else:
   relative_churn_metrics         =  git_churn_extractor.getRelativeChurnMetrics(full_path_param, repo_path_param)
  print relative_churn_metrics
  print "Generated the relative churn metrics ... "
  print "-"*100




test_hg_file  = '/Users/akond/PUPP_REPOS/mozilla-releng-downloads/relabs-puppet/manifests/site.pp'
test_git_file = '/Users/akond/PUPP_REPOS/wikimedia-downloads/cdh4/manifests/pig.pp'
git_repo_path = '/Users/akond/PUPP_REPOS/wikimedia-downloads/cdh4/'
hg_repo_path  = '/Users/akond/PUPP_REPOS/mozilla-releng-downloads/relabs-puppet/'
fullPuppMap   = static_metric_utility.getPuppetFileDetails()
print fullPuppMap
getAllStaticMetric(test_git_file, git_repo_path, fullPuppMap)
