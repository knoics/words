import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
from datetime import datetime
from firebase_admin import auth

def read_words(file_path):
    with open(file_path) as f:
        while True:
            line = f.readline()
            if not line:
                break
            items = line.split(',')
            assert len(items) == 4, 'expected 4 items, having %s' % len(items)
            yield items
    
cred=credentials.Certificate('./dingn-193716-firebase-adminsdk-xhr2d-dfb86f7040.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
user = auth.get_user_by_email('ligangwangs@gmail.com')
uid = user.uid
print(uid)

for items in read_words(r'./word_numbers.txt'):
    doc_ref = db.collection(u'words').document(items[1])
    doc_ref.set({u'ipa_en': items[2], u'number': items[3], 
    u'updated_time': datetime.now(), u'updated_by': uid})