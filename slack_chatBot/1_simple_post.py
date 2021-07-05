# 1_simple_post.py
# 생성한 슬랙 봇을 통해 메시지를 보내는 예제

# 생성한 슬랙 handler 불러오기
from handler import slack_handler

# 메인 함수
if __name__ == "__main__":
	slack_handler.post_slack_message(message="Hello, World!", channel="#일반")