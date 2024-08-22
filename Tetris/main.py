import pygame, sys
from game import Game
from colors import Colors

# 위의 코드는 게임 실행을 위한 라이브러리 호출

pygame.init()  # Pygame 라이브러리를 초기화

# 게임 내에서 사용할 폰트와 텍스트 렌더링
title_font = pygame.font.Font(None, 40)  # 기본 폰트로 크기 40의 폰트 객체 생성
score_surface = title_font.render("Score", True, Colors.white)  # Score 텍스트를 하얀색으로 렌더링
next_surface = title_font.render("Next", True, Colors.white)  # Next 텍스트를 하얀색으로 렌더링
game_over_surface = title_font.render("GAME OVER", True, Colors.white)  # GAME OVER 텍스트를 하얀색으로 렌더링

# 점수와 다음 블록 표시를 위한 사각형 생성
score_rect = pygame.Rect(320, 55, 170, 60)  # 점수 표시용 사각형 영역 설정
next_rect = pygame.Rect(320, 215, 170, 180)  # 다음 블록 표시용 사각형 영역 설정

# 게임 창 설정
screen = pygame.display.set_mode((500, 620))  # 크기 500x620의 게임 화면 생성
pygame.display.set_caption("Python Tetris")  # 창의 제목을 Python Tetris로 설정

clock = pygame.time.Clock()  # 게임 루프 속도를 제어할 시계 객체 생성

game = Game()  # Game 클래스의 인스턴스 생성

# 게임 업데이트 이벤트를 생성하여 200밀리초마다 발생하도록 설정
GAME_UPDATE = pygame.USEREVENT  # 사용자 정의 이벤트 생성
pygame.time.set_timer(GAME_UPDATE, 200)  # 200ms마다 게임 업데이트 발생

# 메인 게임 루프 시작
while True:
    for event in pygame.event.get():  # 모든 이벤트를 가져와 처리
        if event.type == pygame.QUIT:  # 창 닫기 버튼을 클릭했을 때
            pygame.quit()  # Pygame 종료
            sys.exit()  # 프로그램 종료
        if event.type == pygame.KEYDOWN:  # 키를 눌렀을 때 발생하는 이벤트
            if game.game_over == True:  # 게임이 끝났을 경우
                game.game_over = False  # 게임 오버 상태를 해제
                game.reset()  # 게임을 초기화
            if event.key == pygame.K_LEFT and game.game_over == False:  # 왼쪽 방향키를 눌렀을 때
                game.move_left()  # 블록을 왼쪽으로 이동
            if event.key == pygame.K_RIGHT and game.game_over == False:  # 오른쪽 방향키를 눌렀을 때
                game.move_right()  # 블록을 오른쪽으로 이동
            if event.key == pygame.K_DOWN and game.game_over == False:  # 아래쪽 방향키를 눌렀을 때
                game.move_down()  # 블록을 아래로 이동
                game.update_score(0, 1)  # 점수를 1점 추가
            if event.key == pygame.K_UP and game.game_over == False:  # 위쪽 방향키를 눌렀을 때
                game.rotate()  # 블록을 회전
        if event.type == GAME_UPDATE and game.game_over == False:  # 200ms마다 발생하는 이벤트
            game.move_down()  # 블록을 아래로 이동

    # 화면 그리기
    score_value_surface = title_font.render(str(game.score), True, Colors.white)  # 현재 점수를 렌더링

    screen.fill(Colors.dark_blue)  # 화면을 어두운 파란색으로 채움
    screen.blit(score_surface, (365, 20, 50, 50))  # Score 텍스트를 화면에 표시
    screen.blit(next_surface, (375, 180, 50, 50))  # Next 텍스트를 화면에 표시

    if game.game_over == True:  # 게임 오버 상태일 경우
        screen.blit(game_over_surface, (320, 450, 50, 50))  # GAME OVER 텍스트를 화면에 표시

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)  # 점수 표시 영역에 밝은 파란색 사각형 그리기
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))  # 현재 점수를 화면에 표시
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)  # 다음 블록 표시 영역에 밝은 파란색 사각형 그리기
    game.draw(screen)  # 게임 화면을 그리기

    pygame.display.update()  # 화면 업데이트
    clock.tick(60)  # 초당 60프레임으로 게임 루프를 실행
