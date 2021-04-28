from pyfcm import FCMNotification

APIKEY = 'AAAAntqsfJ4:APA91bFdg7guIwGDWNptuqakgwxN90bTbGH7fhpkqavIpmZBtlgrakpcQetYZwhabIUgmk4I' \
         '-G7_zRZJl7Hco_TOpnDONmcovHYBAEseA1RlqwKH4wIXeHPYjuOSKRkFqrUakCHOeFLU '

push_service = FCMNotification(APIKEY)


# FCM 전송
def sendMessage(body, title):
    # 메시지 (data 타입)
    data_message = {
        "body": body,
        "title": title
    }

    # 토큰값을 이용해 1명에게 푸시알림을 전송함
    result = push_service.notify_topic_subscribers(
        topic_name="4dagger",
        message_body="sd",
        message_title="good?")

    # 전송 결과 출력
    print(result)
