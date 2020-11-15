#import cognitive_face as CF
#import global_variables as global_var
import requests
import sys
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import time
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
Key = '33511ab23d274155b6a06966bf896b19'
ENDPOINT = 'https://recogination.cognitiveservices.azure.com/'
face_client = FaceClient(ENDPOINT,CognitiveServicesCredentials(Key))
person_group_id='face1'
#face_client.person_group.train(person_group_id)

#CF.Key.set(Key)

#BASE_URL = global_var.BASE_URL  # Replace with your regional Base URL
#

res = face_client.person_group.get_training_status(person_group_id)
#if (res.status is TrainingStatusType.succeeded):
	#sys.exit('Successfully trained')
#elif (res.status is TrainingStatusType.failed):
	#sys.exit('Training the person group has failed.')
print(res)
