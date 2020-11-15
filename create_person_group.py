#import cognitive_face as CF
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType
#from global_variables import personGroupId
import sys

Key = '33511ab23d274155b6a06966bf896b19'
ENDPOINT = 'https://recogination.cognitiveservices.azure.com/'
person_group_id='face1'
#CF.Key.set(Key)
face_client = FaceClient(ENDPOINT,CognitiveServicesCredentials(Key))
personGroups = face_client.person_group_person.list(person_group_id)
for personGroup in personGroups:
    if person_group_id == personGroup['person_group_id']:
        print(person_group_id + " already exists.")
        sys.exit()

res = face_client.person_group.create(person_group_id=person_group_id,name=person_group_id)
print(res)
