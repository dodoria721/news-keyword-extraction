<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/Neo4j-4581C3?style=for-the-badge&logo=Neo4j&logoColor=white"> <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white">

# news-keyword-extraction

네이버 뉴스 랭킹 페이지에서 지정한 기간의 뉴스 정보를 스크래핑합니다.

스크래핑한 데이터에서 각 뉴스의 제목을 정제하여 필요 없는 문자를 제거합니다.

정제된 제목에서 키워드를 추출하기 위해 한국어 형태소 분석기(Kkma, Komoran)를 사용합니다.

추출한 키워드를 데이터프레임에 저장하여 뉴스와 해당 키워드 간의 연결을 유지합니다.

데이터프레임에서 결측값을 제거하고, 특정 미디어와 중복된 뉴스를 제외하여 분석에 사용할 데이터를 정제합니다.

분석에 필요한 그래프, 통계 또는 시각화 작업을 수행하여 뉴스 랭킹의 트렌드나 키워드의 동향을 파악합니다
