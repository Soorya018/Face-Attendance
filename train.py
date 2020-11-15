#import cognitive_face as CF
#import global_variables as global_var
import requests
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
ENDPOINT = 'https://recogination.cognitiveservices.azure.com/'
Key = '33511ab23d274155b6a06966bf896b19'
person_group_id='face1'
face_client = FaceClient(ENDPOINT,CognitiveServicesCredentials(Key))

#CF.Key.set(Key)

#BASE_URL = global_var.BASE_URL  # Replace with your regional Base URL
#CF.BaseUrl.set(BASE_URL)


res = face_client.person_group.train(person_group_id)
print(res)
