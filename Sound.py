import pygame, os

# 게임 스크린 크기
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 400

# 색 정의
BLACK = (0, 0, 0)

# pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("Sound")

# 스크린 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# assets 경로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

# 배경 이미지 로드
background_image = pygame.image.load(os.path.join(assets_path, 'equalizer.png'))

# 배경 음악 로드    
pygame.mixer.music.load(os.path.join(assets_path, 'bgm.wav'))
pygame.mixer.music.play(-1)

# 효과음 로드
sound = pygame.mixer.Sound(os.path.join(assets_path, 'sound.wav'))

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            sound.play()

    # 게임 로직 구간

    # 게임 삭제 구간

    # 스크린 채우기
    screen.fill(BLACK)

    # 화면 그리기 구간
    screen.blit(background_image, background_image.get_rect())

    # 화면 업데이트
    pygame.display.flip()

    # 초당 60프레임으로 업데이트
    clock.tick(60)
    
# 게임 종료
pygame.quit()