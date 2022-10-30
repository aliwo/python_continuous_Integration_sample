# 개요

안녕하세요! 저는 3년차 Python 개발자고, 현재 유명 배달 3사 중 한 곳에서 파이썬 개발자로 일 하고 있습니다.

전에 부트 캠프 학생분들에게 Continuous Integration 을 가르치면서 CI 의 개념이 학생들에게 정말 어렵구나를 많이 느꼇습니다. 
"어떻게 하면 학생들이 CI 를 잘 이해하도록 만들까?" 를 많이 고민했었는데요, 
이 repository 에 동작하는 에제를 만들어 놓는 것으로 "CI 는 이렇게 하면 됩니다!" 를 예시를 들어드리고자 합니다.

편하게 보시고 자유롭게 issue & pull request 남겨주세요!

# Quick Start

CI 가 어떻게 동작하는지 바로 보실 수 있도록 친절한 설명과 함께 pull request 형태로 남겨두었습니다. 

* black: https://github.com/aliwo/python_continuous_Integration_sample/pulls/1
* isort:
* mypy:
* pytest


# Stack
가장 장래성있고 인기있는 스택 위주로 사용했습니다.
* fastapi
* tortoise orm
* pydantic
* httpx
* mysql

기본 프레임워크로 fastapi 를 사용합니다.
tortoise-orm 을 사용해서 mysql 에 접속하며, 모든 memo 레코드를 조회하는 api 에 대한 테스트가 `tests/test_db.py` 안에 있습니다. 


# Continuous Integration

이 프로젝트는 매 push 마다 다음과 같은 검증을 수행합니다.

* black: 코드 스타일 체크
* isort: 임포트 순서 체크
* mypy: 정적 타입 체크
* pytest & coverage: 모든 테스트가 통과하는지, coverage 가 너무 낮지는 않은지 체크



