import time

try:
    num = 1;
    while True:
        # 무한 루프 코드
        print(num)
        time.sleep(1)
        num=num+2
        pass

except KeyboardInterrupt:
    print("사용자가 프로그램을 종료했습니다.")