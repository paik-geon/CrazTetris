from grid import Grid
from blocks import *
import random
import pygame

# 위의 코드는 게임 실행을 위한 라이브러리 호출


class Game: # 게임동작을 위해 동적인 부분을 담당할 Game으로 불리는 class를 선언
	def __init__(self): # 주요 변수와 기능들을 Game 클래스 전체가 사용할 수 있도록 만들기 위해 정의
		self.grid = Grid() #  게임판 생성
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()] # 블록 종류의 리스트 생성
		self.current_block = self.get_random_block() # 현재 블록을 랜덤으로 선택
		print(self.current_block)
		self.next_block = self.get_random_block() #다음 블록을 랜덤으로 선택
		print(self.next_block)
		self.game_over = False # 게임오버 상태를 초기화
		self.score = 0 # 점수를 0으로 설정

	def move_down(self): # 블록을 아래로 내리기 위해 정의
		self.current_block.move(1, 0) # 블록을 한칸 아래로 이동
		if self.block_inside() == False or self.block_fits() == False: # 만약 블록이 게임판 안에 없거나 다른 블록들과 겹치는 경우
			self.current_block.move(-1, 0) # 블록을 원래 위치로 되돌림
			self.lock_block() # 블록을 고정

	def move_left(self): # 블록을 왼쪽으로 보내기 위해 정의
		self.current_block.move(0, -1) # 블록을 왼쪽으로 한 칸 이동
		if self.block_inside() == False or self.block_fits() == False: # 만약 블록이 게임판 안에 없거나 다른 블록들과 겹치는 경우
			self.current_block.move(0, 1) # 블록을 윈래 위치로 되돌림

	def move_right(self): # 블록을 오른쪽으로 보내기 위해 정의
		self.current_block.move(0, 1) # 블록을 오른쪽으로 한 칸 이동
		if self.block_inside() == False or self.block_fits() == False: # 만약 블록이 게임판 안에 없거나 다른 블록들과 겹치는 경우
			self.current_block.move(0, -1) # 블록을 원래 위치로 이동

	def update_score(self, lines_cleared, move_down_points): # 점수를 업데이트 하기 위해 정의
		if lines_cleared == 1: # 만약 한 줄을 지운 경우
			self.score += 100 # 100점 추가
		elif lines_cleared == 2: # 혹은 두 줄을 지운 경우
			self.score += 300 # 300점 추가
		elif lines_cleared == 3: # 혹은 세 줄을 지운 경우
			self.score += 500 # 500점 추가
		self.score += move_down_points # 추가적인 이동 점수를 더함

	def get_random_block(self): # 랜덤 블록을 가져오기 위해 정의
		if len(self.blocks) == 0: # 만약 블록 리스트가 비어있다면
			self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()] # 모든 블록리스트를 다시 생성
		block = random.choice(self.blocks) # 랜덤으로 블록을 선택
		self.blocks.remove(block) # 리스트에서 블록을 삭제
		print(block)
		return block # 선택한 블록 반환

	def lock_block(self): # 현재 블록을 게임판에 고정하기 위해 정의
		tiles = self.current_block.get_cell_positions() # 현재 블록의 위치를 확인
		for position in tiles: # 각 타일의 위치에 대해서
			self.grid.grid[position.row][position.column] = self.current_block.id # 게임판에 블록을 고정
		self.current_block = self.next_block # 다음 블록을 현재 블록으로 설정
		self.next_block = self.get_random_block() # 새로운 다음 블록을 랜덤으로 설정
		rows_cleared = self.grid.clear_full_rows() # 가득 찬 줄을 삭제
		if rows_cleared > 0: # 만약 제거된 줄이 있는 경우
			self.update_score(rows_cleared, 0) # 점수를 업데이트
		if self.block_fits() == False: # 만약 새로운 블록이 게임판을 벗어난 경우
			self.game_over = True # 게임 오버로 상태변환

	def reset(self): # 게임을 초기로 리셋하기 위해 정의
		self.grid.reset() # 게임판 리셋
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()] # 블록 리스트 초기화
		self.current_block = self.get_random_block() # 현재 블록을 랜덤으로 선택
		self.next_block = self.get_random_block() # 다음 블록을 랜덤으로 선택
		self.score = 0 # 점수를 0으로 설정

	def block_fits(self): # 블록이 게임판에 맞는지 확인하기 위해 정의
		tiles = self.current_block.get_cell_positions() # 현재 블록의 타일 위치 확인
		for tile in tiles: # 각 타일의 위치에 대해
			if self.grid.is_empty(tile.row, tile.column) == False: # 타일이 비어있지 않은 경우
				return False # False 반환
		return True # 블록이 맞을 경우 True 반환

	def rotate(self): # 블록을 회전시키기 위해 정의
		self.current_block.rotate() # 블록을 회전
		if self.block_inside() == False or self.block_fits() == False: # 만약 블록이 게임판을 벗어나거나 다른 블록과 겹치는 경우
			self.current_block.undo_rotation() # 회전을 취소

	def block_inside(self): # 블록이 게임판에 맞는지 확인하기 위해 정의
		tiles = self.current_block.get_cell_positions() # 현재 블록의 타일 위치를 확인
		for tile in tiles: # 각 타일의 위치에 대해
			if self.grid.is_inside(tile.row, tile.column) == False: # 타일이 게임판 안에 없는 경우
				return False # False 반환
		return True # 블록이 타일 안에 있으면 True 반환

	def draw(self, screen): # 그리드를 화면에 그리기 위해 정의
		self.grid.draw(screen) # 그리드를 화면에 출력
		self.current_block.draw(screen, 11, 11) # 현재 블록을 화면에 11, 11 위치에 	출력

		if self.next_block.id == 3: # 만약 다음 블록의 ID가 3일 경우
			self.next_block.draw(screen, 255, 290) # 다음 블록을 255, 290 위치에 출력
		elif self.next_block.id == 4: # 만약 다음 블록의 ID가 4일 경우
			self.next_block.draw(screen, 255, 280) # 다음 블록을 255, 280 위치에 출력
		else: # 둘 다 아닐 경우
			self.next_block.draw(screen, 270, 270) # 270, 270 위치에 다음 블록을 출력