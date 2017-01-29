'''
Akond, Jan 04, 2016
Extract reviews for mozilla releng repos
'''

import requests, time, bug_git_util
infoToExtract = [ 'summary', 'bugs_closed', 'reviews', 'target_groups', 'absolute_url', 'approved', 'issue_open_count', 'time_added',
                    'testing_done', 'target_people', 'description', 'status',
                    'id', 'ship_it_count', 'depends_on', 'last_updated', 'submitter', 'changes' ]


def giveValidIDs(f_):
  list_ = []
  f = open(f_, 'rU')
  for id_ in f:
    if (len(id_) > 0):
        list_.append(int(id_))
  print "Total valid Ids", list_
  print "="*50
  return list_
def getAllReviewRequests(urlParam):
  #r = requests.get('https://reviewboard.mozilla.org/api/review-requests/')
  #allStuff = 'https://reviewboard.mozilla.org/api/review-requests/?start=21800&max-results=22000'
  #allStuff = 'https://reviewboard.mozilla.org/api/review-requests/?sort=repository%2C-last_updated&datagrid-id=datagrid-0&columns=star%2Csummary%2Csubmitter%2Ctime_added%2Clast_updated_since%2Crepository&page=5'
  allStuff = urlParam
  r = requests.get(allStuff)
  revAsJSON = r.json()
  return revAsJSON




def processIndiReq(revReqObjParam):
  infoToExtract.sort()
  indiHolder=''
  for k_ in infoToExtract:
    temp_key=''
    if k_ in revReqObjParam:
        temp_key = revReqObjParam[k_]
        if ((k_=='target_groups') or (k_=='target_people') or (k_=='depends_on') or (k_=='reviews') or (k_=='changes')):
          temp_key = len(temp_key)
        if ((k_=='description') or (k_=='summary')):
          temp_key = temp_key.replace('\n', ' ')
        if (type(temp_key) is str):
          temp_key = temp_key
        else:
          temp_key = str(temp_key)
    else:
        temp_key = 'NA'
    indiHolder = indiHolder +',' + temp_key
  return indiHolder
def getRelevantRevReq(fP):
  holderStr=''
  validIDList = giveValidIDs(fP)
  incre_ = 150 # at what values hsould I increment ?
  #urlextractorList = [x_ for x_ in xrange(incre_, 22000, incre_)]
  #urlextractorList = [x_ for x_ in xrange(7800, 22000, incre_)]
  urlextractorList = [x_ for x_ in xrange(16300, 22000, incre_)]    
  #print urlextractorList
  #urlextractorList = [21000, 20000, 100550]
  for index_ in urlextractorList:
    start_ = index_ - incre_
    last_ =  index_
    if start_ <= 0:
        start_ = start_ + 1 #handling the corner case
    theUrl =  'https://reviewboard.mozilla.org/api/review-requests/?start='+str(start_)+'&max-results='+str(last_)
    print "The url we will use:", theUrl
    print "="*50
    allRevReqP  = getAllReviewRequests(theUrl)
    allReqs = allRevReqP['review_requests']
    for indiReq in allReqs:

      id_ = indiReq['id']
      if id_ in validIDList:
        print "*"*25
        print "Found relevant rev-req#", id_
        validIndiContent  = processIndiReq(indiReq)
        holderStr = holderStr + validIndiContent + '\n'
        print holderStr
        print "*"*25
        print indiReq
        print "*"*25
      #print "="*50
    print "total review_requests (this batch):", len(allReqs)
    print "="*50
    print "total review_requests (so far):", last_
    print "="*50
    print "Time for a power nap ..."
    print "="*50
    time.sleep(120)
  return holderStr
print "Started at:", bug_git_util.giveTimeStamp()
print "="*100
validIDFileName='/Users/akond/Desktop/code-review-raw/mozilla/build-puppet/changeID.txt'
outputFileName ='/Users/akond/Desktop/code-review-raw/mozilla/build-puppet/fullContent.csv'
fullContent = getRelevantRevReq(validIDFileName)
print "="*100
st = bug_git_util.dumpContentIntoFile(fullContent, outputFileName)
print "Dumped a file of {} bytes".format(st)
print "="*100
print "For headers"
print infoToExtract
print "="*100
print "Ended at:", bug_git_util.giveTimeStamp()
