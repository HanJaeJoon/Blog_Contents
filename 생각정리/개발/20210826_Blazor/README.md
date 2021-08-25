# Blazor 토이 프로젝트

.NET 6.0에서 완성이 될 것으로 보이는 Blazor를 배우기 위해 간단히 토이 프로젝트를 진행하고 있다.  

https://github.com/HanJaeJoon/Blazor  

먼저 기술 자체는 너무 신기하고 편리했지만, 개발 경험(?)은 좋지 않았다.  
Blazor WebAssembly는 중단점이 동작을 안 해서 디버깅이 불가능했다.  
Blazor Server는 front를 수정하고 새로고침을 해도 변동사항이 적용되지 않았다.  
새로운 Hot reload 기능도 Blazor WebAssembly, Server 모두 잘 동작허자 않았다.  

개발을 하다보니 배포가 되는지 실험하고 싶었다.  
Documentation을 보니 비교적 Azure Cloud에 배포하면 편해서 그렇게 하려고 했다.  
하지만, 왜 인지 나는 Azure 12개월 무료 서비를 받을 수 없었다.  

며칠동안의 삽질을 통해 결국 AWS Cloud 배포를 해낼 수 있었다.😂😂  
http://ec2-3-144-47-61.us-east-2.compute.amazonaws.com/

다음 포스트에서 하나씩 되짚어보면서 문서와 달랐던 설정들을 확인해봐야겠다.  

참고한 문서는 다음과 같다.
- https://docs.microsoft.com/en-us/aspnet/core/host-and-deploy/linux-nginx?view=aspnetcore-5.0
- https://docs.microsoft.com/en-us/aspnet/core/blazor/host-and-deploy/server?view=aspnetcore-5.0