import sys
#import cognitive_face as CF
#import global_variables as global_var
import sqlite3
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


Key = '33511ab23d274155b6a06966bf896b19'

#CF.Key.set(Key)

ENDPOINT  = 'https://recogination.cognitiveservices.azure.com/'# Replace with your regional Base URL
#CF.BaseUrl.set(BASE_URL)
face_client = FaceClient(ENDPOINT,CognitiveServicesCredentials(Key))
person_group_id='face1'
print("person_group_id = %s" %(person_group_id))
#face_client.person_group.delete(person_group_id)
if len(sys.argv) is not 1:
    res = face_client.person_group_person.create(person_group_id, str(sys.argv[1]))
    #print("res = {}".format(res)) 
    print(res)
    extractId = str(sys.argv[1])[-2:]
    connect = sqlite3.connect("Face-DataBase")
    cmd = "SELECT * FROM Students WHERE ID = " + extractId
    cursor = connect.execute(cmd)
    isRecordExist = 0
    for row in cursor:                                                          # checking wheather the id exist or not
        isRecordExist = 1
    if isRecordExist == 1:                                                      # updating name and roll no
        connect.execute("UPDATE Students SET personID = ? WHERE ID = ?",(res.person_id, extractId))
    connect.commit()                                                            # commiting into the database
    connect.close()
    print("Person ID successfully added to the database")
else:
    print("please specify parameters ie userId of person to add from database directory")
