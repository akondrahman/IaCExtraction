'''
Akond, Jan 04, 2016
Extract reviews for mozilla releng repos
'''

import requests



def giveValidIDs(f_):
  list_ = []
  f = open(f_, 'rU')
  for id_ in f:
    if (len(id_) > 0):
        list_.append(int(id_))
  print "Total valid Ids", list_
  return list_
def getAllReviewRequests():
  #r = requests.get('https://reviewboard.mozilla.org/api/review-requests/')
  allStuff = 'https://reviewboard.mozilla.org/api/review-requests/?start=21800&max-results=22000'
  #allStuff = 'https://reviewboard.mozilla.org/api/review-requests/?sort=repository%2C-last_updated&datagrid-id=datagrid-0&columns=star%2Csummary%2Csubmitter%2Ctime_added%2Clast_updated_since%2Crepository&page=5'
  r = requests.get(allStuff)
  revAsJSON = r.json()
  return revAsJSON

def getRelevantRevReq(allRevReqP, fP):
  holderStr=''
  validIDList = giveValidIDs(fP)
  infoToExtract = [ 'summary', 'bugs_closed', 'reviews', 'target_groups', 'absolute_url', 'approved', 'issue_open_count', 'time_added',
                    'testing_done', 'target_people', 'description', 'status',
                    'id', 'ship_it_count', 'depends_on', 'last_updated', 'submitter' ]
  infoToExtract.sort()
  # for validID in validIDList:
  #   for key_ in infoToExtract:
  #     url_ = 'https://reviewboard.mozilla.org/api/review-requests/' + str(8) + '/' + 'changes'
  #     r_ = requests.get(url_)
  #     revAsJSON = r_.json()
  #     print revAsJSON
  #     print "="*50
  # print "Info pieces to extract:", infoToExtract
  # print "="*50
  allReqs = allRevReqP['review_requests']

  for indiReq in allReqs:
    print indiReq
    print "="*50
  print "total review_requests:", len(allReqs)
  print "="*50


allRevReq = getAllReviewRequests()
#print allRevReq
print "Done loading all requests"
print "="*100
validIDFileName='/Users/akond/Desktop/code-review-raw/mozilla/build-puppet/changeID.txt'
getRelevantRevReq(allRevReq, validIDFileName)
print "="*100
