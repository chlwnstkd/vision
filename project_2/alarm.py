import requests
import time

def get_seats_summary() -> None:
    url = "https://ticket.melon.com/tktapi/product/block/summary.json?v=1"

    body = {
        'prodId': '210341',
        'pocCode': 'SC0002',
        'scheduleNo': '100003',
        'perfDate': '',
        'seatGradeNo': '10054',
        'corpCodeNo': ''
    }

    header = {
        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '_T_ANO=eph4CjGXeUA3pu+ZQcYZxhENF++JLvhe+BhEypSXEUPqvoIVSX1S10elcuguVjtczDOgFZmfMzSmNCU6nSz/KgQBUQQFmazGE+8tFKfRRyaPt/UoaYHe3Futz8NR90sugBTWmYu7ze8J67xYUBpYPygWnNchqqnGWTt2HTCBJScBDFtGouMRKIBe1UBCpfpeZQ2zARNvrBzHGY6z4bjQu7e7gcw/VudCT4gOebpyPPZ81uv8fruIgF1R7kcVR20/Z83o71r6TjRGMywrLTKhJ/m/YVoRVMTSJmpKxOKOA8L4T8swikOtR1VheYg9/4eOPk/5GmR1XWfWiZQAQznr/g==; PCID=17275360663663320986879; _fwb=175aR76lXB2V0JiYLyBMVYv.1727536066491; TKT_POC_ID=WP15; NetFunnel_ID=WP15; PC_PCID=17275360663663320986879; MAC=Pt6+Iea7kVhP4Go6T4wFdWf3BwEBRLG1EOFew+/sWyhjdmmHzITqJfgSo27fWWmv; MLCP=NDI5NDg3MzYlM0IlMjNrYWthb19qdW40NzU1JTNCJTNCMCUzQmV5SmhiR2NpT2lKSVV6STFOaUo5LmV5SnBjM01pT2lKdFpXMWlaWEl1YldWc2IyNHVZMjl0SWl3aWMzVmlJam9pYldWc2IyNHRhbmQwSWl3aWFXRjBJam94TnpJM05UTTJNVEF6TENKdFpXMWlaWEpMWlhraU9pSTBNamswT0Rjek5pSXNJbUYxZEc5TWIyZHBibGxPSWpvaVRpSjkuaTI4QjBCcTZsanRraXBpYXRCMm9jem1NWVBMMEJ4WHFtZHNvTGlKcHVQdyUzQiUzQjIwMjQwOTI5MDAwODIzJTNCJUVDJUE0JTgwJUVDJTgzJTgxJTNCMSUzQmp1bjQ3NTUlNDBkYXVtLm5ldCUzQjIlM0I=; MUS=943693463; keyCookie=42948736; MTR=MTR; store_melon_cupn_check=42948736; performance_layer_alert=%2C210341; wcs_bt=s_585b06516861:1727536111; JSESSIONID=66197FD20B2B78A8624CC53F621FFE98',
        'Host': 'ticket.melon.com',
        'Referer': 'https://ticket.melon.com/reservation/popup/stepBlock.htm',
        'User-Agent': 'X'
    }

    response = requests.post(url,headers=header,data=body)
    return response.json()

def check_remaining_seats(seats: list) -> list:
    result = []

    for seat in seats:
        if seat['realSeatCntlk'] > 0:
            print('남은 좌석 발생!')

# 위 함수는 아래처럼 호출합니다.
# 먼저 좌석 데이터를 가져오고
seats = get_seats_summary()

# 좌석 데이터에서 summary(좌석 배열) 값을 잔여좌석 체크 함수의 매개변수로 넘깁니다.
check_remaining_seats(seats['summary'])

# 메세지 출력 시 generate_message 함수를 호출하도록 변경합니다.
def check_remaining_seats(seats: list) -> list:
    result = []

    for seat in seats:
        if seat['realSeatCntlk'] > 0:
            print(generate_message(seat))

# 정확히 어느 위치에 몇 자리가 발생했는지 메세지를 작성해서 반환합니다.
def generate_message(seat: dict) -> str:
    return seat['seatGradeName'] + ", " + seat['floorNo'] + seat['floorName'] + " " + seat['areaNo'] + seat['areaName'] + "에 잔여좌석 " + str(seat['realSeatCntlk']) + "개 발생! "

# 메세지를 출력하는 대신 배열에 저장한 뒤 반환합니다.
def check_remaining_seats(seats: list) -> list:
    result = []

    for seat in seats:
        if seat['realSeatCntlk'] > 0:
            result.append(generate_message(seat))

    return result

# 메세지 목록을 받아 Slack Webhook URL로 메세지를 전달합니다.
def send_message(messages: list) -> None:
    slack_webhook_url = "https://hooks.slack.com/services/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"
    for message in messages:
        response = requests.post(slack_webhook_url, json={'text' : message})

# 위 함수는 아래처럼 호출합니다.
# 좌석 데이터를 받아옵니다.
seats = get_seats_summary()

# 좌석 중 잔여 좌석 정보에 대한 메세지 배열을 받아옵니다.
messages = check_remaining_seats(seats['summary'])

# 메세지 목록을 매개변수로 전달합니다.
send_message(messages)

def main() -> None:
    for i in range(150):
        seats = get_seats_summary()
        messages = check_remaining_seats(seats['summary'])
        send_message(messages)
        time.sleep(2)