# [2022 .NET Conf.] 나인크로니클의 .NET 6.0 전환기

2022 .NET Conf.에서 가장 기다렸던 세션이다.  
우리 팀에서도 열심히 진행을 하고 있는 중이기 때문에 더욱 기대했다.  
나인크로니클이라는 블록체인 기반 게임을 개발하는 회사에서 .NET 6.0 전환기를 발표했다.

### .NET 6.0 도입 목적  
- 성능을 위해 .NET 6.0으로 전환  
- C# 10, 신규 API 등  
- ARM64 지원

### 좋았던 신규 기능  
- Parallel.ForEachAsync()
- MaxBy(), MinBy() => 이건 왜 그동안 없었는지 의문일 정도. 많이 쓸 것 같다.
- Task.WaitAsync()
- record(C# 9)
- const interpolation(C# 10)

### .NET 6.0 도입 과정  
참고: https://github.com/planetarium/NineChronicles.Headless/pull/859/files
- dotnet 설치
- C# 버전 설정
- AddSingleton(): nullable 변수에 대한 에러 해결(null forgiving 등)
- WebClient의 obsolete => 우리는 RestSharp 사용 중이니 괜찮을듯

먼저 web app.인 우리 제품의 전환기와는 거리가 있는 것 같다.  
그리고 우리는 더욱 더 옛날 .NET 제품이기 때문에 저렇게 쉽게 도입이 힘들 것으로 보인다.  
하지만, 지금은 신입 개발자가 2명이 합류한 상황이라 든든하다.  
(귀찮은 작업들을 마음껏 시킬 수 있다.😈)  
이 속도라면 우리가 최초로 Web app.에서 .NET 6.0 전환기를 발표할 수 있는 날이 오지 않을까?  