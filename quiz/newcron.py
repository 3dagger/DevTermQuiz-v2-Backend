import firebase_admin
from firebase_admin import messaging, credentials
from pyfcm import FCMNotification

# def send_to_firebase_cloud_messaging():
#     print('Enter this method')
#     registration_token = 'cwbKD1xMSYGobD4syT4u3I:APA91bGL0AlgN17nUxJJX3vv0X7YYdBURcII6n6qvmMoIS-Otr7yij2jpoPPS4w9v2CftIDCqFCab-tT5Ar4UV-MhN0khcowEtB7Agg8XN6ssSCbai_O-CspKdtznr8rfdjseGkjm7ze'
#
#     message = messaging.Message(
#         notification=messaging.Notification(
#             title='3dagger :: Title',
#             body='3dagger :: Body',
#         ),
#         token=registration_token,
#     )
#
#     response = messaging.send(message)
#
#     print('Successfully sent message:', response)
APIKEY = 'AAAAntqsfJ4:APA91bFdg7guIwGDWNptuqakgwxN90bTbGH7fhpkqavIpmZBtlgrakpcQetYZwhabIUgmk4I' \
         '-G7_zRZJl7Hco_TOpnDONmcovHYBAEseA1RlqwKH4wIXeHPYjuOSKRkFqrUakCHOeFLU '
# TOKEN = "cwbKD1xMSYGobD4syT4u3I:APA91bGL0AlgN17nUxJJX3vv0X7YYdBURcII6n6qvmMoIS-Otr7yij2jpoPPS4w9v2CftIDCqFCab
# -tT5Ar4UV-MhN0khcowEtB7Agg8XN6ssSCbai_O-CspKdtznr8rfdjseGkjm7ze"

push_service = FCMNotification(APIKEY)


def sendMessage():
    data_message = {
        "body": "zz",
        "title": "쿠폰도착"
    }
    result = push_service.notify_topic_subscribers(topic_name="3dagger", data_message=data_message)

    print(result)


def sendFirebaseMessage():
    topic = '3dagger'

    message = messaging.Message(
        data={
            'body': "right?",
            'title': "all",
        },
        topic=topic
    )

    response = messaging.send(message)
    print(response)
