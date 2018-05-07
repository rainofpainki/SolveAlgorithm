#!/usr/bin/env python
import sys

def get_min_avg(data, n, l):
    """
    공연일자별 공연 비용 중에서 최소 평균 대여 비용을 반환한다
    :param data: 공연 비용 list
    :param n: 공연장을 대여할 수 있는 날들의 수
    :param l: 이미 섭외한 공연 팀의 수
    :return: 최소 평균 대여 비용
    """
    min = None
    # 이미 섭외한 공연 팀의 수에서 공연장을 대여할수 있는 날들의 수만큼 배열을 순회한다.
    for i in range(l, n+1):
        for j in range(0, (n - (i-1))):
            chap = data[j:j + i]
            avg = float(sum(chap, 0.0) / i)
            # 최소값이 없거나 최소값보다 평균값이 더 작은 경우
            if min is None or min > avg:
                min = avg
    return min


if __name__ == "__main__":
    # 테스트 케이스의 값
    c = int(input("테스트 케이스의 수를 입력하세요 : "))

    # 테스트 케이스의 입력 필터를 지정한다.
    if  c > 100:
        print('테스트 케이스의 수는 100 이하여야 합니다.')
        sys.exit(-1)

    # 테스트 케이스의 수 만큼 실행한다
    for i in range(0, c):
        line = input("공연장을 대여할 수 있는 날들의 수와 이미 섭외한 공연팀의 수를 입력하세요 : ")
        (n , l) = map(lambda x: int(x), line.split(" "))

        if n < 1 or n > 1000:
            print("공연장을 대여할 수 있는 날들의 수는 1~1000 이여야 합니다.")
            sys.exit(-1)

        if l < 1 or l > 1000:
            print("이미 섭외한 공연 팀의 수는 1~1000 이여야 합니다.")
            sys.exit(-1)

        if l > n:
            print("이미 섭외한 공연 팀의 수는 공연장을 대여할 수 있는 날들의 수 보다 작아야 합니다.")
            sys.exit(-1)

        print("공연장을 대여할 수 있는 날들의 수 : ", n)
        print("이미 섭외한 공연 팀의 수 : ", l)

        cost_line = input("날짜별 공연장 대여 비용(총 "+ str(n) + "일) : ")
        cost_list = list(map(lambda x: int(x), cost_line.split(" ")))

        if len(cost_list) != n:
            print("입력한 대여 비용의 수와 공연장을 대여할 수 있는 날들의 수가 다릅니다.")
            sys.exit(-1)

        # 배열을 순회하며 (최소) 평균 대여비용을 반환한다
        min = get_min_avg(cost_list, n, l)
        print("최소 평균 대여 비용 : ", min)