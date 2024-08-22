class Position: # Position이라는 블록모양 제작을 위해 필요한 기본 조건을 가지는 class 생성
	def __init__(self, row, column): # 주요 변수와 기능들을 Game 클래스 전체가 사용할 수 있도록 만들기 위해 정의
		self.row = row # 가로행을 생성
		self.column = column # 세로행을 생성
