# AWS EC2 Ubuntu Blazor Server 배포

먼저 아래 포스트를 참고하여 AWS EC2 Ubuntu 인스턴스를 만든다.  
https://jjester.tistory.com/139

## 필수 프로그램 설치

```
sudo apt update
```

### git

```
sudo apt install git
```

### nginx
```
sudo apt install nginx
```

### .NET 5.0 SDK & Runtime
```
wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb
```

```
sudo apt-get update; \
  sudo apt-get install -y apt-transport-https && \
  sudo apt-get update && \
  sudo apt-get install -y dotnet-sdk-5.0
```

```
sudo apt-get update; \
  sudo apt-get install -y apt-transport-https && \
  sudo apt-get update && \
  sudo apt-get install -y aspnetcore-runtime-5.0
```

```
sudo apt-get install -y dotnet-runtime-5.0
```

## Blazor Server 소스 수정  
Startup.cs
```
using Microsoft.AspNetCore.HttpOverrides;

...

app.UseForwardedHeaders(new ForwardedHeadersOptions
{
    ForwardedHeaders = ForwardedHeaders.XForwardedFor | ForwardedHeaders.XForwardedProto
});

app.UseAuthentication();

...

// http로 접근 시 https로 redirect되지 않도록 함
//app.UseHttpsRedirection();
```

`app.UseHttpsRedirection()`는 http로 접근 시 https로 redirect되도록 설정한다.  
아직 SSL 인증서가 없으므로 주석처리한다.  
(이 부분때문에 몇 시간을 헤맸던 것 같다😭)  

## Nginx config 설정
서버의 80포트로 접근하는 경우에 http://localhost:5000 연결되도록 설정한다.
```
server {
    listen        80;
    location / {
        proxy_pass         http://localhost:5000;
        proxy_http_version 1.1;
        proxy_set_header   Upgrade $http_upgrade;
        proxy_set_header   Connection keep-alive;
        proxy_set_header   Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto $scheme;
    }
}
```
MS documentation에서는 아래 부분이 있지만, 아직 도메인도 없기 때문에 제거한다.  
`server_name   example.com *.example.com;`  

## Publish  
소스 코드가 있는 위치로 이동해서 아래 명령어를 실행한다.  
```
dotnet publish --configuration Release
```
bin/Release/net5.0/publish 경로로 publish된다.  

해당 경로로 이동해서 아래 명령어를 실행하면 서버가 구동되는 것을 확인할 수 있다.  
```
dotnet <app_assembly>.dll
```

## Service 만들기  
서버가 계속 구동되어 있는 상태로 유지하기 위해 서비스가 필요하다.  
아래 경로에 `kestrel-helloapp.service` 생성한다.
```
sudo nano /etc/systemd/system/kestrel-helloapp.service
```
```
[Unit]
Description=Example .NET Web API App running on Ubuntu

[Service]
WorkingDirectory=/var/www/helloapp
ExecStart=/usr/bin/dotnet /var/www/helloapp/helloapp.dll
Restart=always
# Restart service after 10 seconds if the dotnet service crashes:
RestartSec=10
KillSignal=SIGINT
SyslogIdentifier=dotnet-example
User=www-data
Environment=ASPNETCORE_ENVIRONMENT=Production
Environment=DOTNET_PRINT_TELEMETRY_MESSAGE=false

[Install]
WantedBy=multi-user.target
```

나의 경우는 Blazor라는 이름의 프로젝트였고 아래와 같이 설정했다.  
```
WorkingDirectory=/home/ubuntu/source/Blazor/Blazor/bin/Release/net5.0/publish
ExecStart=/usr/bin/dotnet /home/ubuntu/source/Blazor/Blazor/bin/Release/net5.0/publish/Blazor.dll
```
**WorkingDirectory를 publish된 경로로 설정하지 않으면 css가 깨질 수 있기 때문에 주의해야 한다.**  
여기도 은근히 헤맸던 부분이다. 역시 경로는 간단히 하는 것이 정신 건강에 좋다.  

아래 명령어를 통해 만든 서비스를 실행하면 putty 세션을 종료해도 서버가 구동된다.
```
sudo systemctl enable kestrel-helloapp.service
sudo systemctl start kestrel-helloapp.service
sudo systemctl status kestrel-helloapp.service
```

아래 repository를 배포했다.  
이제 배포가 되는 것도 확인했으니 열심히 개발해야겠다.
- https://github.com/HanJaeJoon/Blazor  
- http://ec2-3-144-47-61.us-east-2.compute.amazonaws.com/