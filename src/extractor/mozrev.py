'''
Akond, Jan 04, 2016
Extract reviews for mozilla releng repos
'''

import requests, time
infoToExtract = [ 'summary', 'bugs_closed', 'reviews', 'target_groups', 'absolute_url', 'approved', 'issue_open_count', 'time_added',
                    'testing_done', 'target_people', 'description', 'status',
                    'id', 'ship_it_count', 'depends_on', 'last_updated', 'submitter' ]


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
    else:
        temp_key = 'NA'
    indiHolder = indiHolder +',' + temp_key
  return indiHolder
def getRelevantRevReq(fP):
  holderStr=''
  validIDList = giveValidIDs(fP)

  urlextractorList = [x_ for x_ in xrange(200, 22000, 150)]
  #print urlextractorList
  #urlextractorList = [12000, 15000, 16000]
  for index_ in urlextractorList:
    start_ = index_ - 200
    last_ =  index_
    if start_ <= 0:
        start_ = start_ + 1 #handling the corner case
    theUrl =  'https://reviewboard.mozilla.org/api/review-requests/?start='+str(start_)+'&max-results='+str(last_)
    print "The url we will use:", theUrl
    print "="*50
    allRevReqP  = getAllReviewRequests(theUrl)
    allReqs = allRevReqP['review_requests']
    for indiReq in allReqs:
      #print indiReq
      id_ = indiReq['id']
      if id_ in validIDList:
        print "*"*25
        print "Found relevant rev-req#", id_
        validIndiContent  = processIndiReq(indiReq)
        holderStr = holderStr + validIndiContent + '\n'
        print holderStr
        print "*"*25
      #print "="*50
    print "total review_requests:", len(allReqs)
    print "="*50
    print "Time for a power nap ..."
    print "="*50
    time.sleep(120)


validIDFileName='/Users/akond/Desktop/code-review-raw/mozilla/build-puppet/changeID.txt'
getRelevantRevReq(validIDFileName)
print "="*100
