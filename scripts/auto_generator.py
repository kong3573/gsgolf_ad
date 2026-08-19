import json, os, datetime, random

TEMPLATES_PATH = 'weekly_templates.json'

THEMES = [
    {
        'channel': 'band',
        'title': '주말 필드 전 3타 줄이기! 어프로치 특훈 혜택',
        'bandMode': 'my_band',
        'theme': 'style1',
        'data': {
            'targetBand': '광산골프 네이버 밴드',
            'shop': '광산골프 어프로치 숏게임 연습장',
            'subHead': '주말 실전 라운딩 완벽 대비 프로모션',
            'head': '주말 라운딩 3타 줄이기!
어프로치 단독 특훈 혜택',
            'topBadge': 'WEEKEND SPECIAL',
            'discRate': '25%',
            'disc': '주말 오전 타임 25% 특별 할인',
            'discSub': '밴드 회원 인증 시 전 코스 특가 적용',
            'eventBadge': '1 + 1',
            'event': '어프로치볼 1박스 + 퍼팅그린 30분 무료',
            'eventSub': '동반자와 함께 오시면 추가 혜택 증정',
            'bonus': '네이버 영수증 리뷰 작성 시 30분 무료 연장!',
            'hours': '월~토 08:00 ~ 24:00 (자정까지) / 일 08:00 ~ 18:00',
            'phone': '062-454-7878',
            'addr': '광산구 동곡상정길 42',
            'toggles': {'disc': True, 'event': True, 'bonus': True}
        }
    },
    {
        'channel': 'band',
        'title': '광주·전남 골프동호회 연합 단체 제휴 우대',
        'bandMode': 'other_band',
        'theme': 'style2',
        'data': {
            'targetBand': '광주전남 골프 매니아',
            'shop': '광산골프 어프로치 숏게임 연습장',
            'subHead': '[광주전남 골프 매니아] 회원 전용 특별 제휴',
            'head': '[광주전남 골프 매니아]
회원님 전용 단독 VIP 우대 혜택!',
            'topBadge': 'PARTNER VIP',
            'discRate': '30%',
            'disc': '동호회/밴드 회원 단체 30% 제휴 할인',
            'discSub': '밴드 회원 확인 시 전원 즉시 우대 적용',
            'eventBadge': 'FREE GIFT',
            'event': '3인 이상 방문 시 1인 전액 무료!',
            'eventSub': '동호회 정기 모임 & 번개 라운딩 환영',
            'bonus': '포토리뷰 작성 시 프리미엄 볼마커 세트 증정!',
            'hours': '월~토 08:00 ~ 24:00 (자정까지) / 일 08:00 ~ 18:00',
            'phone': '062-454-7878',
            'addr': '광산구 동곡상정길 42',
            'toggles': {'disc': True, 'event': True, 'bonus': True}
        }
    },
    {
        'channel': 'insta',
        'title': '밤 12시까지 열리는 감성 나이트 숏게임장',
        'theme': 'insta2',
        'data': {
            'page': '01 / 05',
            'tag': 'NIGHT GOLF ACADEMY',
            'main': '퇴근하고 즐기는
야간 12시 숏게임 파라다이스',
            'sub': '환한 LED 조명 아래 실제 천연잔디 어프로치',
            'p1': '⛳ 10~70m 실전 천연잔디 & 벙커 훈련 코스',
            'p2': '🌙 밤 12시까지 여유롭게 즐기는 나이트 라운딩',
            'p3': '🎁 밴드 회원 20% 할인 & 1+1 동반자 무료',
            'acc': '@gwangsan_golf | ☎ 062-454-7878'
        }
    },
    {
        'channel': 'influencer',
        'title': '골프 인플루언서 VIP 초청 & 전 코스 무료 협찬',
        'data': {
            'name': '@golf_creator',
            'title': 'VIP 골프 크리에이터 무료 체험 초청장',
            'greeting': '골퍼들의 숏게임 성지 광산골프에서 인플루언서 님을 전 코스 무료 VIP로 초대합니다.',
            'b1': '💎 광산골프 전 코스 무제한 VIP 무료 이용권',
            'b2': '👥 동반 1인 전액 무료 라운딩 지원',
            'b3': '☕ 최고급 음료 및 간식 전액 무료 제공',
            'mission': '인스타그램 릴스/피드 숏게임 연습 영상 1회 업로드',
            'contact': 'DM 회신 또는 ☎ 062-454-7878 로 일정 예약'
        }
    }
]

def generate():
    now = datetime.datetime.now()
    week_num = now.isocalendar()[1]
    date_str = now.strftime('%Y-%m-%d %H:%M')
    selected = random.sample(THEMES, 4) if len(THEMES) >= 4 else THEMES
    result = []
    for idx, item in enumerate(selected):
        tpl = {
            'id': f'auto_w{week_num}_{idx}_{int(now.timestamp())}',
            'title': f'✨ [추천] {item["title"]}',
            'date': date_str,
            'channel': item['channel'],
            'data': item['data']
        }
        if 'bandMode' in item: tpl['bandMode'] = item['bandMode']
        if 'theme' in item: tpl['theme'] = item['theme']
        result.append(tpl)
    with open(TEMPLATES_PATH, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f'Generated {len(result)} templates')

if __name__ == '__main__':
    generate()
