'''
Author: Heesook Choi (hc1645@att.com)
Edits: Phil Weir
Usage:
 python ecomp_mso_interim_parser.py ./<iodatafolder>/ yyyy-mm-dd month/week/day
Dependencies:
These libraries may be needed if errors occur

pip install pytz
pip install datetime
pip install numpy
pip install pandas<0.21
pip install parse
pip install iteration_utilities

Please update your splunk credentials on line 464
'''
import os
import sys
import re
import pytz
import os.path
import calendar, datetime, time
from time import sleep, time
from dateutil.relativedelta import relativedelta
from datetime import datetime, date, timedelta
from parse import search
import pandas as pd
import string
from pandas.io.json import json_normalize
import json

## if curl is used to pull the data from Splunk server,
## the following two import statements are not needed.
##import splunklib.client as client
##import splunklib.results as results

import json
from pandas.io.json import json_normalize
from iteration_utilities import duplicates

def flatten_dict(d):
    def expand(key, value):
        if isinstance(value, dict):
            return [ (key + '.' + k, v) for k, v in flatten_dict(value).items() ]
        else:
            return [ (key, value) ]

    items = [ item for k, v in d.items() for item in expand(k, v) ]

    return dict(items)


from dateutil import parser
def convertDateTime(timeString):
    # Fri, 03 Aug 2018 17:42:26 GMT
    if type(timeString) == float:
        return timeString
    else:
        ctime = datetime.strptime(timeString,"%a, %d %b %Y %H:%M:%S GMT")
        return ctime


import datetime
from datetime import datetime

def convert2iso(timestamp):
    regexp = re.compile('\d{4}-\d{2}-\d{2}')
    try:
        match = regexp.match(timestamp)
        if match:
            return timestamp[:19]
    except:
##        print("no match timestamp (epoch?):", timestamp)
        #return datetime.utcfromtimestamp(timestamp).isoformat()
        #datetime.datetime.fromtimestamp(ts_epoch).strftime('%Y-%m-%d %H:%M:%S')
        try:
            return datetime.fromtimestamp(timestamp/1000.0, pytz.utc).strftime('%Y-%m-%dT%H:%M:%S')
        except:
##            print("Error convert2iso: ", timestamp)
            return ''
        #return timestamp

def convert2epoch(isotime):
    ''' Convert datetime to epoch time '''
    ##epoch_time = timegm(utc_time)
    try:
        timestamp = datetime.strptime(isotime[:19], "%Y-%m-%dT%H:%M:%S")
        epoch = calendar.timegm(timestamp.utctimetuple())
    except:
 ##       print("Error convert2epoch: ", isotime)
        return isotime
    ##timestamp = (utctime - datetime(1970, 1, 1)).total_seconds()
    #timestamp = timegm(utctime)*1000
    return epoch


def calculateLatency(row):
    if row['startTime'] is None or row['endTime'] is None:
        return 0
    if row['startTime'] == 'nan' or row['endTime'] == 'nan':
        return 0

    try:
        start = convert2epoch(row['startTime'])
        end   = convert2epoch(row['endTime'])
        latency = (end-start)
        return latency
    except:
 ##       print(row['startTime'], row['endTime'])
        return 0

## NEW method by PHIL
def calculateRetries(row):
    if row['retryStatusMessage'] is None:
        return 0
    if row['retryStatusMessage'] == 'nan':
        return 0
##    retrymsg = row['retryStatusMessage']
	retries = 0 
	print(row['retryStatusMessage'])
    try:
        if 'Retry 5' in row['retryStatusMessage']:
            retries = 5
        elif 'Retry 4' in row['retryStatusMessage']:
			retries = 4 
        elif 'Retry 3' in row['retryStatusMessage']:
			retries = 3
        elif 'Retry 2' in row['retryStatusMessage']:
			retries = 2
        elif 'Retry 1' in row['retryStatusMessage']:
			retries = 1
        return retries
    except:
        print(row['retryStatusMessage'])
        return 0
##################################################################
        if 'COMPLETE' in xset or 'COMPLETED' in xset:
            return 'COMPLETED'
        elif 'FAILED' in xset:
            return 'FAILED'
        else:
            return '-'.join(xset)  

##################################################################
def parseRawData(data, start_time, end_time):

    rgx_spans = re.compile(r'(\s|,\s)[a-zA-Z0-9_\-]+=')

    # Get the start-end positions of all matches.
    text = data.lstrip().lstrip('{').rstrip('}')
    spans = [m.span() for m in rgx_spans.finditer(text)]
   
    # Use those positions to break up the string into parsable chunks.
    try:
        items = {}
        for i, s1 in enumerate(spans):
            try:
                s2 = spans[i + 1]
            except IndexError:
                s2 = (None, None)
                continue
    
            start = s1[0]
            end = s2[0]
            key, val = text[start:end].lstrip(',').lstrip().split('=', 1)
    
            #print()
            #print(s1, s2)
            #print((key, val))
            if val.startswith("{"):
                val = json.loads(val)
            items[key]=val
        df = flatten_dict(items) ##json_normalize(items)
        ##columns = list(df)
        ##newColumns = [ 'p_'+ col.split('.')[-1] if len(col.split('.')) > 1 else col for col in columns]
        ##df.columns = newColumns
        ##df['requestURI']= df['requestId']
        ##print(df.shape)
        return df
    except:
        #print("Parsing errors...")
        #print(data)
        return None



##################################################################
    ## 1) read the input json file from curl, 2) parse json format and convert it to python dataframe
##################################################################
def parseRawJsonData(data, start_time, end_time):

    try:
        ##data = fields[2].split(':',1)
        requestList = None
        if data.strip().startswith('['):
            requestList = list(json.loads(data.strip()))
            #print("Number of transactions: ", fields[1], len(requestList))
        else:
            requestList = json.loads(data.strip())
        df = flatten_dict(requestList)  ##json_normalize(requestList)
        return df
    except:
        #print("Parsing errors...")
        #print(data)
        return None

##################################################################
    ## 1) read the input json file from curl, 2) parse json format and convert it to python dataframe
    ## 3) write the python dataframe into csv
##################################################################
def parseSplunkLogsFromJson(jobf, start_time, end_time):
    ''' 
    input: log data from splunk server
    output: generate a parsed row for each log event
    '''
    dfList = []
    with open(jobf) as f:
        for line in f:
            # rawString is formatted based on Splunk 
            j_content = json.loads(line)   
            mso_splunk_results = flatten_dict(j_content)
            fields=[]
            if 'lastrow' in mso_splunk_results:
                continue
            try:
                rawString = mso_splunk_results['result._raw'].rstrip('\n') 
                #print("rawString:", rawString)
                fields = rawString.split("|")
            # field11 = field[10] is the target
            except:
                continue

            ## ignore events out of time range
            event_time = datetime.strptime(fields[0][:23], '%Y-%m-%dT%H:%M:%S.%f')
            if event_time < start_time or event_time > end_time:
                #print(datetime.strftime(start_time,"%Y%m%d"), datetime.strftime(end_time,"%Y%m%d"))
                continue
            
            df = None
            m = []
            try:
                p = re.compile('{')
                m = fields[2][:p.search(fields[2]).span()[0]].split(':')
            except:
                print("Abnormal log:", fields[2])
                continue
            if len(m) < 3:
                data = fields[2].split(':',1)[1]
                df = parseRawJsonData(data, start_time, end_time)
                ## return dictionary
            else:
                data = fields[2].split(':',2)[2]
                df = parseRawData(data, start_time, end_time)

            if df is None:
                continue

 ##           print(df)
            dfList.append(df)
    print("number of dataframe: ", len(dfList))
    if len(dfList) < 1: #there is no data
        return
    
    parsedDf = json_normalize(dfList) ## pd.DataFrame.from_dict(dfList)  ##pd.concat(dfList)

    #print(list(parsedDf))
    #parsedDf['request.startTime'] = parsedDf['request.startTime'].apply(convertDateTime)
    #parsedDf['request.requestStatus.finishTime'] = parsedDf['request.requestStatus.finishTime'].apply(convertDateTime)

    return parsedDf  ##parsedDf.to_csv(outputFileName, header=True, index=False)







##################################################################
#curl -k -u user:password https://dsvtxvcspks01-eth2.infra.aic.att.net:8089/services/search/jobs/export --data-urlencode search='search index=mso sourcetype=*audit*  NOT getSiteStatus NOT getNodesRequest NOT getFeatureRequest NOT UNKNOWN NOT GetAicNodesRequest NOT ASDCStatusCallBack' -d output_mode=json -d earliest_time=2018-05-31T12:00:00.000-00:00 -d latest_time=2018-06-02T12:00:00.000-00:00 -o mso_2018_06_01.json;

def getStatus(msgs):

    cleanedList = [x for x in msgs if str(x) != 'nan']
    xset = list(set(cleanedList))
    if len(xset) < 1:
        return 'UNKNOWN'
    try:
        if 'COMPLETE' in xset or 'COMPLETED' in xset:
            return 'COMPLETED'
        elif 'FAILED' in xset:
            return 'FAILED'
        else:
            return '-'.join(xset)        
    except:
        print("getStatus:", xset)
        return 'UNKNOWN'


def getVnfType(vnftypes):
    for x in vnftypes:
        if str(x) != 'nan' and x != u'' and x != 'None' and x is not None:
 ##PHIL           print('vnfType', x)
            return x
##PHIL    print('vnfType: UNKNOWN', vnftypes)
    return 'UNKNOWN'

def getValue(ids):
    for x in ids:
        if str(x) != 'nan' and x != '' and x is not None:
            return x
    return 'UNKNOWN'

    
         
            
class RequestBody(dict):
    def __init__(self):
        self['modelType'] =  ''
        self['modelName'] =  ''
        self['instanceName'] =  ''
        self['productFamilyId'] =  ''

def processingRequestBody(rbd):

    bd = RequestBody()

    if rbd == '' or rbd == 'nan'  or rbd is None:
        return pd.Series( {'rbd_modelType':bd['modelType'],\
                      'rbd_modelName':bd['modelName'],\
                      'rbd_instanceName':bd['instanceName'],\
                      'rbd_productFamilyId':bd['productFamilyId'] })
    try:
        rbdDict = flatten_dict(json.loads(rbd))
        if 'requestDetails.modelInfo.modelName' in rbdDict:
            bd['modelName'] = rbdDict['requestDetails.modelInfo.modelName']
        if 'requestDetails.modelInfo.modelType' in rbdDict:
            bd['modelType'] = rbdDict['requestDetails.modelInfo.modelType']
        if 'requestDetails.requestInfo.instanceName' in rbdDict:
            bd['instanceName'] = rbdDict['requestDetails.requestInfo.instanceName']
        if 'requestDetails.requestInfo.productFamilyId' in rbdDict:
 ##Phil FIX spelling on next line 
##			bd['productFamilyId'] = rbdDict['requestDetails.requestInfo.productFamilyId']
			bd['productFaimlyId'] = rbdDict['requestDetails.requestInfo.productFamilyId']
        return pd.Series( {'rbd_modelType':bd['modelType'],\
                      'rbd_modelName':bd['modelName'],\
                      'rbd_instanceName':bd['instanceName'],\
                      'rbd_productFamilyId':bd['productFamilyId'] })
    except:
        print("Error processRequestBody ...:", rbd)
        return pd.Series( {'rbd_modelType':bd['modelType'],\
                      'rbd_modelName':bd['modelName'],\
                      'rbd_instanceName':bd['instanceName'],\
                      'rbd_productFamilyId':bd['productFamilyId'] })
    #print(rbdDict)
    #print(bd)

def aggregateMsg(x):
## Updated by Phil to not add newline for first field in list.
    msgList = list(set(x))
    tmp = ''
    for x in msgList:
        if isinstance(x, float):
##Added by Phil 
 ##		    print("x is not string", x)
            x= str(x)
        if x != 'nan' and x != '' and x is not None and x != 'null':
            if tmp!='' :
                tmp = tmp + '\n'+ x
            else:
                tmp = tmp + x
    return tmp
  
def aggregateData(df):

    vfcolumns = ['vnfType', 'vnfName', 'vnfId', 'vfModuleType', 'vfModuleName', 'vfModuleModelName', 'vfModuleId']

    grouped = df.groupby('requestId') 

    columns = list(df)
    new_df = pd.DataFrame(columns = columns)
    for vcol in vfcolumns:
        new_df[vcol] = grouped[vcol].apply(getValue)

    new_df['vnfType'] = grouped['vnfType'].apply(getVnfType)
    new_df['requestStatus'] = grouped['requestStatus'].apply(getStatus) #lambda x: "{%s}" % '-'.join(x)) 

    statusMsgColumns = ['retryStatusMessage','rollbackStatusMessage','statusMessage'] 
    for col in statusMsgColumns:
        new_df[col] = grouped[col].apply(aggregateMsg)


    vfcolumns = vfcolumns + ['requestStatus'] + statusMsgColumns

    for col in columns:
        if col in vfcolumns:
            continue
        #print("concatenated column: ", col)
        new_df[col] = grouped[col].first()
    # since a list events are sorted by descening, last is the first event and its name is flow name

    #grouped = df.groupby('vnfId')
    #tdf = pd.DataFrame(columns = ['vnfId','vnfType'])
    #tdf['vnfId'] = grouped['vnfId'].first()
    #tdf['vnfType'] = grouped['vnfType'].apply(getVnfType)
    #tuples = tdf.to_dict('records')
    #for t in tuples:
    #    new_df.loc[new_df['vnfId'] == t['vnfId'],['vnfType']] = t['vnfType']

    #requestbd = new_df['requestBody'].apply(processingRequestBody)
    tdf = pd.concat([new_df, new_df['requestBody'].apply(processingRequestBody)], axis=1)
    
    return tdf


if __name__ == '__main__':

    if len(sys.argv) < 4:
        print("Wrong Format")
        print("python ecomp_log_interim_parser.py <io_data_path> <date>")
        print("e.g.: python ecomp_log_interim_parser.py ./ 2018-08-15 month/week")
        exit(1) 
    dpath = sys.argv[1]
    #today = datetime.strptime(sys.argv[2],"%Y-%m-%d")
    today = None ##datetime.strptime(sys.argv[2],"%Y-%m")
    opt = sys.argv[3]

    if opt == 'month':
        first_day = sys.argv[2]+'-01'
        today = datetime.strptime(first_day,"%Y-%m-%d")
        fday = today

        last_day = today + relativedelta(months=+1)
        print("last day =", last_day)
    elif opt == 'week':
        today = datetime.strptime(sys.argv[2],"%Y-%m-%d")
        last_day = today + relativedelta(days=+7)
        print("last day =", last_day)
    else: # default is one day
        today = datetime.strptime(sys.argv[2],"%Y-%m-%d")
        last_day = today + relativedelta(days=+1)
        print("last day =", last_day)
    
    dfList = []
    while today < last_day:
        print("Today:", datetime.strftime(today,"%Y-%m-%d"))
        ## Splunk timestamp is local for the user. 
        ## In order to pull the data safely covering the date of interest,
        ## we will pull the data within 12 hour before the interest datae and after the next date of interest date
        ## The following start_time and end_time are used this window.
        start_time = today - timedelta(hours=12)
        end_time = today + timedelta(hours=24)


        inputFileName = dpath + 'mso_' + datetime.strftime(today,"%Y%m%d")+".json"

        ## build a curl command
        ## kgm1b  action  "o.onap.so.logging.jaxrs.filter.SpringClientFilter - Response body" "Vlcma1213V1Vf..base_LCMA..module-0" createInstance OR deleteInstance
        #curl_command ="curl -k -u user:password https://dsvtxvcspks01-eth2.infra.aic.att.net:8089/services/search/jobs/export --data-urlencode search=\'search index=mso sourcetype=*debug* kgm1b  action  \"o.onap.so.logging.jaxrs.filter.SpringClientFilter - Response body\" \"Vlcma1213V1Vf..base_LCMA..module-0\" createInstance OR deleteInstance \' -d output_mode=json -d earliest_time="+datetime.strftime(start_time,"%Y-%m-%d")+"T12:00:00.000-00:00"+ " -d latest_time="+datetime.strftime(end_time,"%Y-%m-%d")+"T12:00:00.000-00:00"+" -o "+inputFileName
        #curl_command ="curl -k -u user:password https://dsvtxvcspks01-eth2.infra.aic.att.net:8089/services/search/jobs/export --data-urlencode search=\'search index=mso sourcetype=*debug* VID  \"o.onap.so.logging.jaxrs.filter.SpringClientFilter - Response body\" OR \"org.onap.so.bpmn.common.scripts.CatalogDbUtils - Response\" OR \"Received MSO startProcessInstanceByKey with processKey\" OR createInstance OR deleteInstance \' -d output_mode=json -d earliest_time="+datetime.strftime(start_time,"%Y-%m-%d")+"T12:00:00.000-00:00"+ " -d latest_time="+datetime.strftime(end_time,"%Y-%m-%d")+"T12:00:00.000-00:00"+" -o "+inputFileName
        # o.onap.so.logging.jaxrs.filter.SpringClientFilter - Response body:
        jobf = inputFileName 
        if os.path.isfile(inputFileName) != True:
            curl_command ="curl -k -u userid:passwd https://dsvtxvcspks01-eth2.infra.aic.att.net:8089/services/search/jobs/export --data-urlencode search=\'search index=mso sourcetype=*debug* VID NOT GetAicNodesRequest \"o.onap.so.logging.jaxrs.filter.SpringClientFilter - Response body\" OR \"org.onap.so.bpmn.common.scripts.CatalogDbUtils - Response\" OR \"Received MSO startProcessInstanceByKey with processKey\" \' -d output_mode=json -d earliest_time="+datetime.strftime(start_time,"%Y-%m-%d")+"T12:00:00.000-00:00"+ " -d latest_time="+datetime.strftime(end_time,"%Y-%m-%d")+"T12:00:00.000-00:00"+" -o "+inputFileName
            os.system(curl_command)

            print(inputFileName)
            print(curl_command)
        
        ## 1) read the input json file from curl, 2) parse json format and convert it to python dataframe
        ## 3) write the python dataframe into csv
        df = parseSplunkLogsFromJson(jobf, today, end_time)
        dfList.append(df)
        today = today + timedelta(days=1)


    outputFileName = dpath + "mso_parsed_vid_"+sys.argv[2]+"_"+opt+".csv"
    if len(dfList) < 1:
        print("There is no day to process")
    else:
        print("Writing csv to: ", outputFileName)
        new_df = pd.concat(dfList)
        new_df['requestURI'].fillna(new_df['requestId'],inplace=True)
        new_df['requestId'].fillna(new_df['requestURI'],inplace=True)

        ##new_df.to_csv("test1.csv", header=True, index=False) 

        parsedDf = aggregateData(new_df) #pd.concat(dfList))
        ##parsedDf['vnfType'].fillna(parsedDf['rbd_modelName'],inplace=True)
        parsedDf['startTime'] = parsedDf['startTime'].apply(convert2iso)
        parsedDf['endTime'] = parsedDf['endTime'].apply(convert2iso)
        parsedDf['latency'] = parsedDf.apply(calculateLatency, axis=1)
## Code added by PHIL
## Define new column 'retrycount' = how many retries for this request
        parsedDf['retryCount'] = parsedDf.apply(calculateRetries, axis=1)
## END New Code PHIL 
        parsedDf.dropna(axis=1, how='all', inplace=True)
## Code Added by Phil to filter csv output based on a fixed set of columns
## Edit the vfcolumns list to add/remove as needed
## Uncomment next 2 lines to revert to original csv with all columns
        vfcolumns1 = ['startTime', 'requestAction', 'requestScope', 'requestStatus', 'flowStatus', 'retryStatusMessage', 'rollbackStatusMessage', 'statusMessage', 'retryCount', 'requestorId', 'mso-request-id', 'bpmnRequest.requestDetails.requestInfo.suppressRollback', 'bpmnRequest.requestDetails.requestParameters.testApi']
##        parsedDf.drop(vfcolumns1, axis=1, inplace = True)
## uncomment one of the next 2 lines as needed
        parsedDf.filter(items=vfcolumns1).to_csv(outputFileName, header=True, index=False)
##		parsedDf.to_csv(outputFileName, header=True, index=False)
# End Code Addition 



