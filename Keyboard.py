import pygame, os

# 게임 스크린 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("Keyboard")

# 스크린 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# assets 경로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

# 키보드 이미지 초기 설정
keyboard_image = pygame.image.load(os.path.join(assets_path, 'keyboard.png'))
keyboard_x = int(SCREEN_WIDTH/2)
keyboard_y = int(SCREEN_HEIGHT/2)
keyboard_dx = 0
keyboard_dy = 0

# 게임 종료 전까지 반복
done = False    # 게임이 진행 중 인지 확인하는 변수
# done이 True라면 게임이 계속 진행 중 이라는 의미

# 게임 반복 구간
while not done: # 게임이 진행되는 동안 계속 반복 작업을 하는 while 루프
    # 이벤트 반복 구간
    for event in pygame.event.get():
        # 어떤 이벤트가 발생했는지 확인
        if event.type == pygame.QUIT:
            # QUIT는 윈도우 창을 닫을때 발생하는 이벤트
            # 창이 닫히는 이벤트가 발생했다면
            done = True # 반복을 중지시켜 게임 종료
        
        # 키가 눌릴 경우
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keyboard_dx = -3
            elif event.key == pygame.K_RIGHT:
                keyboard_dx = 3
            elif event.key == pygame.K_UP:
                keyboard_dy = -3
            elif event.key == pygame.K_DOWN:
                keyboard_dy = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                keyboard_dx = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                keyboard_dy = 0

    # 게임 로직 구간
    # 키보드 이미지의 위치 변경
    keyboard_x += keyboard_dx
    keyboard_y += keyboard_dy

    # 게임 삭제 구간

    # 스크린 채우기
    screen.fill(GRAY)

    # 화면 그리기 구간
    # 키보드 이미지 그리기
    screen.blit(keyboard_image, [keyboard_x, keyboard_y])

    # 화면 업데이트
    pygame.display.flip()

    # 초당 60프레임으로 업데이트
    clock.tick(60)
    
# 게임 종료
pygame.quit()
