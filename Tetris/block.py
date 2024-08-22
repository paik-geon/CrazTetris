from colors import Colors
import pygame
from position import Position

# 위의 코드는 게임 실행을 위한 라이브러리 호출

class Block: # 블록 기능을 위해 클래스 정의
    def __init__(self, id):
        self.id = id  # 블록의 고유 식별자를 설정
        self.cells = {}  # 블록의 회전 상태에 따른 셀의 위치를 저장할 딕셔너리
        self.cell_size = 30  # 블록의 각 셀의 크기를 30 픽셀로 설정
        self.row_offset = 0  # 블록의 행 오프셋을 0으로 초기화
        self.column_offset = 0  # 블록의 열 오프셋을 0으로 초기화
        self.rotation_state = 0  # 블록의 회전 상태를 0으로 초기화
        self.colors = Colors.get_cell_colors()  # Colors 클래스에서 블록의 색상 배열을 가져와 저장

    def move(self, rows, columns): # 블록의 위치를 지정된 행과 열만큼 이동
        self.row_offset += rows  # 현재 행 오프셋에 주어진 행 수를 더함
        self.column_offset += columns  # 현재 열 오프셋에 주어진 열 수를 더함

    def get_cell_positions(self): # 현재 회전 상태에서 블록의 셀 위치를 계산하여 반환
        tiles = self.cells[self.rotation_state]  # 현재 회전 상태에 해당하는 셀들의 원래 위치를 호출
        moved_tiles = []  # 이동된 셀들의 위치를 저장할 리스트
        for position in tiles:  # 각 셀의 위치를 순회
            position = Position(position.row + self.row_offset, position.column + self.column_offset)  # 오프셋을 적용하여 새로운 위치를 계산
            moved_tiles.append(position)  # 계산된 위치를 리스트에 추가
        return moved_tiles  # 이동된 셀들의 위치 리스트를 반환

    def rotate(self): # 블록을 시계 방향으로 90도 회전
        self.rotation_state += 1  # 회전 상태를 1 증가
        if self.rotation_state == len(self.cells):  # 회전 상태가 모든 회전 상태의 수를 초과시
            self.rotation_state = 0  # 회전 상태를 0으로 리셋

    def undo_rotation(self): # 마지막 회전을 취소하여 블록을 이전 상태로 복구
        self.rotation_state -= 1  # 회전 상태를 1 감소
        if self.rotation_state == -1:  # 회전 상태가 -1이 된다면
            self.rotation_state = len(self.cells) - 1  # 마지막 회전 상태로 복구

    def draw(self, screen, offset_x, offset_y): # 현재 블록을 화면에 그리기
        tiles = self.get_cell_positions()  # 현재 블록의 셀 위치를 가져옴
        for tile in tiles:  # 각 셀을 순회
            # 셀의 위치와 크기를 기준으로 사각형을 생성
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, # 사각형을 해당 블록의 색상으로 출력
                                    offset_y + tile.row * self.cell_size,
                                    self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect) # 지정된 위치에 특정 색상의 블록을 화면에 출력
