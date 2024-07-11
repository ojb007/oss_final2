from getDev import main_getDev
from Top5data import find_worst_air_quality_regions
from air_korea_api import air_condition_realtime
from getAirData import filter_data_by_date_and_region, assess_air_quality

while True:
    print("1. 기간 중 PM10 변동성 순위")
    print("2. 기간 중 PM10 평균 농도 순위")
    print("3. 원하는 입력일 및 지역의 PM10  지수")
    print("4. 종료")
    num = input("번호를 입력하시오 : ")
    print('\n')
    if num == '4':
        print("종료합니다")
        break
    elif num == '1':
        main_getDev()
    elif num == '2':
        init_date = input("시작일을 입력하세요 (예: 20240701): ")
        end_date = input("종료일을 입력하세요 (예: 20240709): ")
        print('\n')
        worst_regions = find_worst_air_quality_regions(init_date, end_date)
        for region in worst_regions:
            print(f"지역: {region['district']}, 평균 PM10 농도: {region['average_pm10']:.2f}")
        print('\n')
    else:
        specific_date = input("시작일을 입력하세요 (예: 20240701): ")
        specific_date = specific_date[0:4] + '-' + specific_date[4:6] + '-' + specific_date[6:] 
        full_data = air_condition_realtime('PM10', 'DAILY')
        specific_region = input("원하는 지역을 입력하세요 (예: seoul, dague): ")
        filtered_data = filter_data_by_date_and_region(full_data, specific_date, specific_region)
        air_quality = assess_air_quality(filtered_data, specific_region)
        print("\n")
        print(f"{specific_date} {specific_region}의 공기질: {air_quality}")
        print("\n")