# 러닝뱅크 교육 스킵하기

이번엔 러닝뱅크 교육 스킵하기다.  
나름 중간에 눌러줘야 하는 것도 없고 순한맛 교육 러닝뱅크...  
킹치만 나는 그것조차 귀찮은걸?😋  

스크립트는 다음과 같다.  
```
function setCookie(name,value,expire,path){ 
    path = (!path)?"/":path; 
    var todaydate = new Date();
    unixtime = todaydate.getTime();
    if (value==null) {
        expire = 0;
    }
    if (expire != null) {
        extime = unixtime+(expire*1000);
        todaydate.setTime(extime);
        expiretime = " expires=" + todaydate.toUTCString() +";"; 
    }else{
        expiretime = ""; 
    }
    document.cookie = name + "=" + escape(value) + "; path="+path+";"+expiretime; 
}

function study(a) {
    setCookie("pPage",'1' + a); // class 1, page 1
    movepg(a); // move to page 2
}

var idx = 2;

function loop() {
  setTimeout(function() {
    study(idx);
    console.log(idx)
    idx++;
    if (idx < 25) {
      loop();
    }
  }, 3000);
}

loop();
```

조금 길지만 입력하고 가만히 기다리면 끝낼 수 있다.