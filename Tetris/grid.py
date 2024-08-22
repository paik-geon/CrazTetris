import pygame
from colors import Colors

# 위의 코드는 게임 실행을 위한 라이브러리 호출

class Grid:  # 게임판 관련 코드를 위해 Grid라는 클래스 선언
    def __init__(self): # 게임판의 행과 열의 수 및 셀의 크기를 설정
        self.num_rows = 20  # 게임판의 행 수를 20으로 설정
        self.num_cols = 10  # 게임판의 열 수를 10으로 설정
        self.cell_size = 30  # 각 셀의 크기를 30 픽셀로 설정
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] # 게임판 그리드를 설정
        self.colors = Colors.get_cell_colors() # Colors 클래스에서 색상 배열을 가져와 저장

    def print_grid(self):
        # 게임판의 현재 상태를 콘솔에 출력
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")  # 각 셀의 값을 출력
            print()  # 행의 끝에서 줄 바꿈

    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols: # 주어진 행과 열이 게임판의 범위 내에 있는지 확인
            return True  # 게임판 범위 내에 있으면 True 반환
        return False  # 범위를 벗어나면 False 반환

    def is_empty(self, row, column):
        # 주어진 위치의 셀이 비어있는지 확인
        if self.grid[row][column] == 0:
            return True  # 셀이 비어있으면 True 반환
        return False  # 셀이 비어있지 않으면 False 반환

    def is_row_full(self, row):
        # 주어진 행이 모두 채워져 있는지 확인
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False  # 빈 셀이 있으면 False 반환
        return True  # 모든 셀이 채워져 있으면 True 반환

    def clear_row(self, row):
        # 주어진 행의 모든 셀을 0으로 설정
        for column in range(self.num_cols):
            self.grid[row][column] = 0 # 셀을 0으로 설정

    def move_row_down(self, row, num_rows): # 주어진 행의 셀들을 아래로 이동
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]  # 셀을 아래로 이동
            self.grid[row][column] = 0  # 원래 위치를 비움

    def clear_full_rows(self):
        # 꽉 찬 행들을 삭제, 위의 행들을 아래로 이동
        completed = 0  # 지운 행의 수를 기록
        # 마지막 행부터 첫 번째 행까지 거꾸로 순회
        for row in range(self.num_rows - 1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)  # 행이 가득 찼으면 그 행을 비움
                completed += 1  # 지운 행의 수를 증가
            elif completed > 0:
                self.move_row_down(row, completed)  # 지운 행 수만큼 위의 행을 아래로 이동
        return completed  # 지운 행의 수를 반환

    def reset(self):
        # 게임판을 초기 상태로 리셋
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    def draw(self, screen): # 현재 게임판을 화면에 그리기
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]  # 현재 셀의 값을 가져옴
                # 셀의 위치와 크기를 기준으로 사각형(Rect)을 생성
                cell_rect = pygame.Rect(column * self.cell_size + 11,  # 셀의 위치와 크기를 기준으로 사각형을 생성
                                        row * self.cell_size + 11,
                                        self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect) # 셀의 값을 인덱스로 사용하여 해당 색상으로 사각형을 그리기
