import matplotlib.pyplot as plt
import numpy as np



def show_10x() -> None:
    x = np.arange(1, 100)
    y = 10 * x

    plt.plot(x, x)
    plt.plot(x, y)
    plt.show()


def show_sin() -> None:
    x = np.arange(0, 2 * np.pi, 0.1)
    y = np.sin(x)

    plt.plot(x, y)
    plt.show()


def show_x_square() -> None:
    x = np.arange(-20, 21)
    y = np.square(x)

    plt.plot(x, y)
    plt.show()

# 차트에 제목 넣기
def show_chart_title() -> None:
    plt.title('plotting')  # 차트 제목을 'plotting'으로 정함
    plt.plot([10, 20, 30, 40])
    plt.show()


# shift + enter 치면 어느 위치에 있던 다음 줄로 넘어감
def show_chart_legend() -> None:
    plt.title('legend')
    plt.plot([10, 20, 30, 40], label = 'asc')
    plt.plot([40, 30, 20, 10], label = 'desc')
    plt.legend() # 범례 표시
    plt.show()


def change_color() -> None:
    plt.title('color') # 제목 설정

    # 그래프 그리기
    plt.plot([10, 20, 30, 40], color='skyblue', label='skyblue')
    plt.plot([40, 30, 20, 10], 'pink', label='pink')
    plt.legend() # 범례 표시
    plt.show()


def change_line() -> None:
    plt.title('linestyle')

    # 빨간색 dashed 그래프
    plt.plot([10, 20, 30, 40], color='r', linestyle='--', label='dashed')
    # 초록색 dotted 그래프
    plt.plot([40, 30, 20, 10], color='g', ls=':', label='dotted')
    plt.legend() # 범례 표시
    plt.show()


def change_marker():
    plt.title('marker')
    plt.plot([10, 20, 30, 40], 'r.', label='circle') # 빨간색 원형 마커 그래프 r : red, . : 점 모양의 마커
    # 초록색 삼각형 마커 그래프
    plt.plot([40, 30, 20, 10], 'g^', label='triangle up') # g : green, ^ : 삼각형 모양의 마커
    plt.legend() # 범례 표시
    plt.show()


def main() -> None:
    """"실행 함수"""
    # show_10x()
    # show_sin()
    # show_x_square()
    # show_chart_title()
    # show_chart_legend()
    # change_color()
    # change_line()
    change_marker()


if __name__ == "__main__":
    main()
