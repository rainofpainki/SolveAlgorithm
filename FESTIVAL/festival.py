#!/usr/bin/env python
import sys

if __name__ == "__main__":
    # 테스트 케이스의 값
    c = int(input())

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

        cost_line = input("날짜별 공연장 대여 비용("+ str(n) + ") : ")
        cost_list = list(map(lambda x: int(x), cost_line.split(" ")))

        if len(cost_list) != n:
            print("입력한 대여 비용의 수와 공연장을 대여할 수 있는 날들의 수가 다릅니다.")
            sys.exit(-1)
