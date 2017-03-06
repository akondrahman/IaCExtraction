'''
Akond Rahman
get author names
by processing a list
March 05, 2017
'''
import numpy as np, bug_git_util


def processAuthorNames(org_):
  theRepoFile=org_+'reponames.txt'
  authorListHolder = []
  list2ret         = []
  with open(theRepoFile) as f_:
    for repo_name in f_:
       repo_name = repo_name.replace('\n', '')
       authorFileToRead = org_+repo_name+'/'+'authorsForThisRepo.txt'
       with open(authorFileToRead) as author_file_:
          for author_name in author_file_:
            if '@' in author_name:
              author_name = author_name.replace('\n', '')
              authorListHolder.append(author_name)
  list2ret = np.unique(authorListHolder)
  return list2ret





def dumpAuthorList(listParam, orgP):
    str2ret=''
    file2save=orgP+'authorEmail.csv'
    for str_ in listParam:
        str2ret = str2ret + str_ + ',' + '\n'
    dump_stats = bug_git_util.dumpContentIntoFile(str2ret, file2save)
    print "Dumped a file of {} bytes".format(dump_stats)



# orgDir = '/Users/akond/PUPP_REPOS/wikimedia-downloads/'
# orgDir = '/Users/akond/PUPP_REPOS/openstack-downloads/'
orgDir = '/Users/akond/PUPP_REPOS/mozilla-releng-downloads/'
uniqueAuthors = processAuthorNames(orgDir)
#print uniqueAuthors
dumpAuthorList(uniqueAuthors, orgDir)
