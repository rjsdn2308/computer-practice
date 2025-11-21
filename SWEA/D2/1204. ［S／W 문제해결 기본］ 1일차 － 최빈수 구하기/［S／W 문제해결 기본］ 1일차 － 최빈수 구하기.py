T = int(input())

for _ in range(T):
    tc_num = int(input())        # 테스트 케이스 번호
    scores = list(map(int, input().split()))

    count = [0] * 101            # 0~100 점수 빈도 테이블

    # 점수 빈도수 계산
    for s in scores:
        count[s] += 1

    # 최빈수 찾기 (동점이면 높은 점수를 선택)
    max_freq = max(count)
    mode = 0
    for score in range(101):
        if count[score] == max_freq:
            mode = score     # 가장 큰 점수를 선택하도록 계속 갱신됨

    print(f"#{tc_num} {mode}")
