# airtableData 크롤링

블록체인 투자 현황을 크롤링하여 스마트팔로우 전략으로 투자할 수 있는 서비스를 만드는 것이 목표이다.
test.py는 그 정보가 담긴 airtable의 테이블 데이터 API를 불러와 크롤링한다.
헤더를 꼭 다 첨부해주어야 한다.

- [x] 크롤링하기
- [x] csv 파일 쓰는 코드 만들기
- [x] 크롤링 파일 csv로 옮기기

## 사용방법

1. git clone 으로 레포지토리 복제, 혹은 dataToCSV.py 다운로드 하기.
2. 터미널키기
3. 레포지토리가 있는 경로에서 source .venv/bin/activate 입력해서 가상환경 실행하기. (입력하고 나서 터미널 맨 앞에 (.venv)가 생겼다면 성공입니다.)
4. python dataToCSV.py 입력
5. 행 하나를 쓰기 할때마다 숫자를 늘려가며 출력합니다.
6. 마지막 요소가 1963이 나왔다면 정상적으로 실행된 것입니다. (혹시 어딘가에서 끊기거나 에러가 생겼다면 알려주세요.)
7. 같은 경로에 airTableData.csv란 이름으로 csv파일이 생성됩니다.
8. 엑셀에 생성된 csv파일을 열면 된다.

로직에 대해 궁금한 것이 있다면 dataToCSV.py 의 맨 밑부분으로 내려서 보시면 됩니다.
나머지 위에 긴 부분은 전부 처리할때 id값을 가져오기 위해 붙여놓은거기 때문에 신경안쓰셔도 됩니다.

---

Description, Fundrasing Round의 column ID :
fldJHMHegLEl2A56n, fld7v0ugjCe9N07W1
( tableSchemas -> columns - 테이블의 column들)

=> 각각의 column ID 를 기억해둔다.

tableDatas는 요소 하나가 있는데 그게 지금 보고있는 페이지의 table임
tableDatas -> rows 내부의 각각의 요소는 웹페이지상의 회사 한개를 의미한다.

rows -> cellValuesByColumnId
원하는 필드값을 확인하려면 위에서 저장해놓은 column ID 값들을 key로 가지고 있는 요소를 찾으면 된다.

위에서 예시로 Description의 ID를 적어놨는데 row[0]에서 각각 id를 찾아보면
Dora Factory - Seed , Open DAO-as-a-Service… 인 것을 찾을 수 있다.
