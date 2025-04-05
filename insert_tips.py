import json

from app import create_app
from app.database import db
from app.models import Tips  # 반드시 Tips 모델이 등록되어 있어야 해

app = create_app()

json_data = [
    {
        "title": "정기권",
        "content": "학생\n 50000원/학기 \n 15000원/월 \n 교직원 \n 50000원/학기 \n 15000원",
        "link": "https://www.khu.ac.kr/kor/user/contents/view.do?menuNo=200088",
        "building_id": "0"
    },
    {
        "title": "노트북 대여",
        "content": "대여 절차\n 경희대 포털 로그인 / 대여 신청 / 접수 대기 / 대여 / 반납 \n 대여 방식 \n 대여 기간: 4박 5일 \n 대여 시 신분증(학생증) 지참, 학생지원 센터 제증명 방문문",
        "link": "https://news.khu.ac.kr/kor/user/contents/view.do?menuNo=200186",
        "building_id": "0"
    },
    {
        "title": "도서관 열람실 좌석 이용",
        "content": "열람실 좌석 이용 시간\n 최초 발권시 4시간 배정 (집중열람실은 최초 발권시 6시간) 연장 4시간 6회 \n 외출 : 이용시간 내 출구게이트 통과 후 90분 이내 입구게이트 통과 (외출 후 90분 초과 시 좌석은 자동반납됨)",
        "link": "https://lib.khu.ac.kr/)(https://lib.khu.ac.kr/webcontent/info/79",
        "building_id": "0"
    },
    {
        "title": "학생지원센터",
        "content": "장학, 심리상담, 제증명, 학생복지",
        "link": "(https://janghak.khu.ac.kr/janghak/user/main/view.do",
        "building_id": "0"
    },
    {
        "title": "장애학생지원센터",
        "content": "교수학습지원을 통하여 장애학생의 수업편의 및 학습능력 향상을 위한 제도 마련, 장애 학생의 성공적인 대학생활과 학습보장을 위하여 노력. \n 주요 업무 : 상담, 인식 개선 프로그램, 시험 보조 및 대필 지원, 생활 도우미 지원 등 ",
        "link": "https://great.khu.ac.kr/great/user/main/view.do",
        "building_id": "0"
    },
    {
        "title": "전자증명서 발급",
        "content": "인터넷을 통해 성적증명서, 재학증명서, 졸업증명서, 졸업예정증명서, 휴학증명서, 교직이수증명서, 수료증명서를 발급받을 수 있다. \n 교내 각 건물에 설치된 증명발급기를 이용하면 된다. 개인 컴퓨터로 인터넷증명발급센터에 접속해 증명서를 출력할 수도 있다.",
        "link": "https://kyunghee.certpia.com/",
        "building_id": "0"
    },
    {
        "title": "공학관",
        "content": "공대 지하 주차장이 큼 \n 필드하키장은 공대앞에 위치하고 있지만 체육대학에서 관리하고 있다.\n 교육용 원자로를 전국에서 유일하게 교내에 보유하고 있다.",
        "link": "",
        "building_id": "25"
    },
    {
        "title": "외국어대학관",
        "content": "수화기의 모습을 본떠서 지었다고 하며 원형의 건물이 2개 있음 \n 로봇이 커피 만들어 줬음",
        "link": "",
        "building_id": "11"
    },
    {
        "title": "체육대학관",
        "content": "대한민국 최초의 체육대학 \n 2024 파리 올림픽 남자 -58kg급 금메달리스트 박태권 선수 졸업 \n 체육대학관은 중앙도서관이 완공되기 전까지는 본관으로 쓰였던 건물. 도서관과 맞먹는 크기와 웅장함을 자랑한다",
        "link": "",
        "building_id": "16"
    },
    {
        "title": "생명과학대학관",
        "content": "생대생들을 비롯 타대생들이 부르는 별명은 목욕탕 \n 학생회관을 가려면 생명과학대학 정류장에서 내려서 계단을 내려가는 것이 사색의 광장에서 내리는 것보다 빠르다.",
        "link": "",
        "building_id": "9"
    },
    {
        "title": "전자정보대학관관",
        "content": "전자정보대학관 : 전자정보대학/소프트웨어융합대학/응용과학대학관 \n 건물 뒷쪽에 증축된 신관이 보임임",
        "link": "",
        "building_id": "6"
    },
    {
        "title": "예술디자인대학관관",
        "content": "1,2층을 제외하면 과 하나 당 한 층이 주어진다. \n 지하 1층에 여자 휴게실이 있음.",
        "link": "",
        "building_id": "8"
    },
    {
        "title": "국제경영대학관",
        "content": "1층 정문을 기준으로 왼쪽은 국제학부 학생들, 오른쪽은 대학원이 쓴다. \n 후문의 산 쪽에 조그만 오솔길이 있는데, 국제대 옆길로 나가 멀관까지도 갈 수 있다. ",
        "link": "",
        "building_id": "10"
    }
]


def add_tips():
    with app.app_context():
        for item in json_data:
            tip = Tips(
                title=item["title"],
                content=item["content"],
                link=item.get("link", None),
                building_id=int(item["building_id"]) if item["building_id"].isdigit() else None
            )
            db.session.add(tip)
        db.session.commit()
        print("✅ 모든 Tips 항목이 데이터베이스에 추가되었습니다.")


if __name__ == "__main__":
    add_tips()
