'''
Akond, Jan 04, 2016
Extract reviews for mozilla releng repos
'''

import requests



def getAllReviewRequests():
  r = requests.get('https://reviewboard.mozilla.org/api/review-requests/')
  revAsJSON = r.json()
  return revAsJSON

def getRelevantRevReq(allRevP):
  holderStr=''
  infoToExtract = [ 'summary', 'bugs_closed', 'reviews', 'target_groups', 'absolute_url', 'approved', 'issue_open_count', 'time_added',
                    'testing_done', 'target_people', 'description', 'status',
                    'id', 'ship_it_count', 'depends_on', 'last_updated', 'submitter' ]
  infoToExtract.sort()
  print "Info pieces to extract:", infoToExtract
  print "="*50
  if 'review_requests' in allRevP:
    onlyReqs = allRevP['review_requests']
    for indiReq in onlyReqs:
      idOfIndiReq = indiReq['id']
      if idOfIndiReq in validIDList:
        indiHolderStr=''
        for key_ in infoToExtract:
            tempForKey = ''
            if key_ in indiReq:
                tempForKey = indiReq[key_]
            else:
                tempForKey='NA'
            indiHolderStr= indiHolderStr + ',' + tempForKey
        holderStr = holderStr + indiHolderStr + '\n'
      #print indiReq
      #print "-"*25
  print "String to dump"
  print holderStr
  print "="*50
allRevReq = getAllReviewRequests()
#print allRevReq
print "Done loading all requests"
print "="*100
getRelevantRevReq(allRevReq)
print "="*100
