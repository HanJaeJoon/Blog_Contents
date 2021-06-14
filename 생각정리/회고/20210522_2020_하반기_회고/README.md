## 2020 하반기 회고

### 6월 ~ 11월
스타트업으로 이직에 성공했다.  
경력이었기 때문에 바로 프로젝트에 투입됐다.
Websocket을 이용한 인터넷 전화 - CRM 연동 기능 개발  
.net Web API 프레임워크 개발, Swagger를 이용한 문서화

-> **.NET Web API 커스텀 개발로 회사 백엔드 프레임워크 구축**

### 8월 ~ 9월
on-premise 상태의 개발 환경을 모두 Azure Cloud로 옮겼다.  
Azure NAT gateway, Load balancer, DNS 설정 등  
(이땐 몰랐지 회사 네트워크 문제가 생기면 내가 불려가게 될 줄...)

-> **한 번도 해보지 못했던 네트워크를 공부하게 됨**

### 11월 ~ 12월
Layered Architecture 적용  
6월에 했던 Web API 프레임워크가 front에서 backend를 이어주는 가교 역할이라면  
Backend의 구조를 구축  
앞으로 회사에서 개발하는 모든 백엔드 구조의 표준 개발  
(Controller -> Service -> Business -> Repository -> DB)  
Async로 DB 작업을 할 수 있도록 개발했지만  
-> 다른 개발자 실수 발생 여지가 있어 추후 적용하기로 함😭

-> **회사 백엔드 프레임워크 프로토타입 완성**