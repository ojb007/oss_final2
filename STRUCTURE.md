# Program Structure

## 개요
이 문서는 프로그램의 구조를 개략적으로 설명하며, 주요 객체, 절차, 함수의 이름과 짧은 설명을 나열합니다.

## 객체 및 함수

# 데이터 처리
- **showRange(api) -> 
  - json 정해진 기간과 지역을 기준으로 데이터를 로드하고 DataFrame을 반환합니다.
- **showLive(api) ->
  - 정한 지역의 시간별 데이터
# 시각화
- **plot_emissions(df: pd.DataFrame) -> None**
  - 각 지역의 미세먼지 농도 보이기
# 스켈레톤 코드 개발을 위한 이슈
  
# 스켈레톤 코드 개발
- **작업**:
  - **작업 1**: `show_data` 함수 생성.
  - **작업 2**: `show_graph' 함수 생성
  - **작업 3**: `data_of_top5` 함수 생성.
  - **작업 4**: `data_of_top5_time` 함수 생성.
