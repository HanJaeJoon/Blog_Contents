## 개발자 온보딩

다음주부터 신입 개발자 온보딩이 있을 예정이다.  
(내가 채용에 관여한 첫 개발자!!!😎)  

나는 신입 개발자 때 어떻게 했는가 하는 회고를 가져봤다.    

지금 직장은 경력직이라 그런지 별도의 온보딩이 없었고,  

첫 직장에서 기억을 떠올렸다.  

한 달의 신입사원 연수(?)를 끝나고 팀에 갔을 떄 했던 팀 교육은 다음과 같았다.

1. 정규식(Regular Expression)

   정규식 실습 과제  
   그 당시에는 왜 해야 했는지 의문이 들었지만, 은근히 쓰게 되는 것 같았음  
   [정규식 테스터](http://regexstorm.net/tester)  
   [MS docs](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference)  

   -> 완전 필수는 아니지만 알고 있으면 좋은 정도

2. 토이 프로젝트

   팀에서 개발한 프레임워크를 이용한 게시판 개발  
   나의 사수: 주간보고를 위한 종합 용도의 게시판 개발, 팀내에서 이후로도 계속 사용함.  
   나: 토이 프로젝트 생략, 바로 업무투입(다국어 작업으로 거의 모든 제품의 프론트 소스를 보게 됨)  
   나의 후임: IE, PC 지원 제품 -> 태블릿, PC 동시 지원 가능하고 Multi browser 지원 가능한 제품 제작(나와 Pair Programming)  
   [Application Life Cycle](https://docs.microsoft.com/en-us/previous-versions/dotnet/netframework-3.0/ms178473(v=vs.85)?redirectedfrom=MSDN)  
   [.NET Page Life Cycle](https://docs.microsoft.com/en-us/previous-versions/aspnet/ms178472(v=vs.100))  
   [Web API Life Cycle1](https://www.dotnetcurry.com/aspnet/888/aspnet-webapi-message-lifecycle)  
   [Web API Life Cycle2](https://www.asp.net/media/4071077/aspnet-web-api-poster.pdf)  

   -> 처음 접하는 .NET 프레임워크에 대한 이해 증진 가능할듯. 필수  
   -> 멀티쓰레드로 게시판을 만드는  진행할 예정

3. 쿼리 튜닝

   쿼리 튜닝 과제(엑셀로 주어진 쿼리를 튜닝)  
   개인적으로 가장 어려웠던 과제, 학부 때 했던 SQL은 맛보기였음을 느낌.  
   실행 계획도 볼 수 없고 실제로 실행해볼 수 없는 상태에서 튜닝이라니...  
   (그로부터 3년이 지난 지금 MS-SQL 튜닝을 하고 있을지 몰랐음)  

   -> 우선순위 낮음.

4. 패키징

   전 회사는 제품 배포를 패키징으로 진행했었음.  
   각 고객 사이트에 Web.config를 설정 및 변경, DB 패치 등 제품 설치 교육  
   DB connect string 설정 방법, 제품, DB 패치 버전 관리가 어떻게 되는지 이해  

   -> 지금은 CI/CD 체험 정도로 대체할 수 있지 않을지.

5. Inspection
   신입 개발자가 개발한 페이지를 팀원들이 보고 피드백 후 전체 팀원 회의때 공유

   -> 피드백을 통해 코딩 컨벤션, .NET 프레임워크 이해 증진. 현재는 코드리뷰 문화가 정착되어 있음.