# 엑셀로 네이버 증권 크롤링하기

채권평가사인 친구가 엑셀로 네이버 증권 크롤링을 한다고 해서  
무두절인 오늘 나도 한 번 만들어봤다.  
만들고 보니 모멘텀 투자에 괜찮을 것 같다.   

[이 github 링크에서 다운 받을 수 있다.](https://github.com/HanJaeJoon/Blog_Contents/blob/main/%EC%83%9D%EA%B0%81%EC%A0%95%EB%A6%AC/%ED%88%AC%EC%9E%90/20210729_%EC%97%91%EC%85%80_%EB%84%A4%EC%9D%B4%EB%B2%84_%ED%8C%8C%EC%9D%B4%EB%82%B8%EC%85%9C_%ED%81%AC%EB%A1%A4%EB%A7%81/files/VBA.xlsm)

아래 게시판에서 page를 이동하며 당일 종가 정보를 가져온다.
![](images/0.png)

VBA 문법을 찾아서 개발했어야 해서 은근히 오래 걸렸다.  
API가 아닌 크롤링은 DOM element를 selector로 찾기 때문에 네이버에서 UI를 바꾸면 잘못된 데이터가 들어올 수 있다.  
그리고 원하는 데이터만 선별적으로 가져올 수 없기 때문에 너무 복잡하고 비효율적이다.  

개발을 할 줄 안다면 API를 이용하도록 하자!  
API로 개발한 VAA 계산기도 흥해라!  
https://quant-jj-vaa.herokuapp.com/

### 사용방법  
종목코드를 입력하고 버튼을 누르면  
![](images/1.png)

최근 4분기의 종가를 확인할 수 있다.
![](images/2.png)