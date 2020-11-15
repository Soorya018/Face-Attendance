import sys
import os, time
#import global_variables as global_var
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType
import urllib
import sqlite3
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


KEY = '33511ab23d274155b6a06966bf896b19'

ENDPOINT = 'https://recogination.cognitiveservices.azure.com/'

face_client = FaceClient(ENDPOINT,CognitiveServicesCredentials(KEY))
person_group_id='face1'
def get_person_id():
    person_id = ''
    extractId = str(sys.argv[1])[-2:]
    connect = sqlite3.connect("Face-DataBase")
    c = connect.cursor()
    cmd = "SELECT * FROM Students WHERE ID = " + extractId
    c.execute(cmd)
    row = c.fetchone()
    person_id = row[3]
    connect.close()
    return person_id

if len(sys.argv) is not 1:
    currentDir = os.path.dirname(os.path.abspath(__file__))
    imageFolder = os.path.join(currentDir, "dataset/" + str(sys.argv[1]))
    person_id = get_person_id()
    for filename in os.listdir(imageFolder):
        if filename.endswith(".jpg"):
            print(filename)
            img_data = open(os.path.join(imageFolder,filename), 'r+b')
            res = face_client.face.detect_with_stream(img_data)
            if not res:
                print('No face detected from image {}'.format(filename))
                continue
            img_data = open(os.path.join(imageFolder,filename), 'r+b')
            res = face_client.person_group_person.add_face_from_stream(person_group_id, person_id,img_data)
            print(res)  
            time.sleep(6)
else:
    print("supply attributes please from dataset folder")