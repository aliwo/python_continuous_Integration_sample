# CI 는 대체 어떻게 하는거에요?

안녕하세요! 저는 3년차 Python 개발자고, 현재 유명 배달 3사 중 한 곳에서 파이썬 개발자로 일 하고 있습니다.

전에 부트 캠프 학생분들에게 Continuous Integration 을 가르치면서 CI 의 개념이 학생들에게 정말 어렵구나를 많이 느꼈습니다. 
"어떻게 하면 학생들이 CI 를 잘 이해하도록 만들까?" 를 많이 고민했었는데요, 
이 repository 에 동작하는 에제를 만들어 놓는 것으로 " CI 는 대체 어떻게 하는거에요?" 에 대한 저의 대답입니다.

편하게 보시고 자유롭게 issue & pull request & 질문 남겨주세요!

# What is CI?
코드가 메인 브렌치로 합쳐질 떄 마다 일련의 검사를 실행하는 것을 CI 라고 합니다. (단위 테스트 필수)
다음과 같은 검사를 실행합니다.

정적분석:
* black: pep8 을 준수하였는지 검사합니다.
* isort: import 순서가 맞는지 검사합니다.
* mypy: 정적 타입을 체크 합니다.

단위테스트:
* pytest: 단위테스트를 실행합니다.
* coverage: 테스트 실행시 line coverage (실행된 라인 수 / 전체 라인 수) 를 검사합니다.

# Quick Start

CI 가 어떻게 동작하는지 바로 보실 수 있도록 친절한 설명과 함께 pull request 형태로 남겨두었습니다. 클릭해 보세요!

* [black](https://github.com/aliwo/python_continuous_Integration_sample/pull/1)
* [isort](https://github.com/aliwo/python_continuous_Integration_sample/pull/2)
* [mypy](https://github.com/aliwo/python_continuous_Integration_sample/pull/3)
* [pytest](https://github.com/aliwo/python_continuous_Integration_sample/pull/4)


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


# Tags
* 파이썬 깃헙액션 연동 
* CI
* continuous integration
