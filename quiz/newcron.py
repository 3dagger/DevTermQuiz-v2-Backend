from pyfcm import FCMNotification

APIKEY = 'AAAAntqsfJ4:APA91bFdg7guIwGDWNptuqakgwxN90bTbGH7fhpkqavIpmZBtlgrakpcQetYZwhabIUgmk4I' \
         '-G7_zRZJl7Hco_TOpnDONmcovHYBAEseA1RlqwKH4wIXeHPYjuOSKRkFqrUakCHOeFLU '
TOKEN = 'dUlIlwkOR5Om5UsIrPajV9:APA91bFD-LUzxO68bv2TgRx9xL2so8g1yNBeUewO48jgyzlTMVyTadQYO41P6jzQqOt3k-hfPHp9DMXF6C48PNi-aXUVKjY_ktDT7Dv2AMABDfjSvMJmXbp0CVy_N1T9sntI_LYnbQoi'

push_service = FCMNotification(APIKEY)


def sendMessage(body, title):
    # 메시지 (data 타입)

    data_message = {
        "body": body,
        "title": title
    }

    # 토큰값을 이용해 1명에게 푸시알림을 전송함
    result = push_service.notify_topic_subscribers(topic_name="3dagger", message_body="sd", message_title="good?")

    # 전송 결과 출력
    print(result)
