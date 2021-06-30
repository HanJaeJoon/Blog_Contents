## [javascript] jquery ajax, Blob을 이용한 file download

전에 회사에서 csv, excel export 기능을 개발한 적이 있다.  
이번 회사에서도 새로 개발하려니 기록이 없어서 꽤 고생했다.  
이번에는 잘 기록해두어야지.😊

먼저, XmlHttpRequest의 response Type을 [Blob](https://developer.mozilla.org/en-US/docs/Web/API/Blob)(Binary type)으로 설정한다.  

```
$.ajax({
    url: url,
    data: parameters,
    type: 'POST',
    cache: false,
    xhrFields: {
        responseType: "blob",
    },
})
```

서버에서는 다음과 같이 response를 해준다.  
한글이 포함된 파일명도 잘 보이게 하도록 파일명을 URL encoding했다.  
```
Content-Disposition: attachment; filename=%ed%95%9c%ea%b8%80_file_download_20210630115035.xlsx  
Content-Length: 267848  
Content-Type: application/octect-stream  
```

아래 소스는 .NET Web API Controller의 response 예시
```
HttpResponseMessage response = new HttpResponseMessage(HttpStatusCode.OK)
{
    Content = new ByteArrayContent(stream.ToArray()),
};

response.Content.Headers.ContentDisposition = new ContentDispositionHeaderValue("attachment")
{
    FileName = HttpUtility.UrlEncode($"한글_file_download_{DateTime.Now:yyyyMMddHHmmss}"),
};

response.Content.Headers.ContentType = new MediaTypeHeaderValue("application/octect-stream");

return response;
```

정상적으로 response를 받았다면 done() callback에서 첫 번째 parameter로 BLOB 객체를 가져올 수 있다.  

```
.done(function (blob, status, xhr) {});
```

먼저 XmlHttpRequest 헤더에서 첨부된 파일명을 가져온다.  
아까 서버에서 한글도 가져오기 위해 URL encoding 했으니, decode해서 파일명을 가져온다.

```
 // check for a filename
var fileName = "";
var disposition = xhr.getResponseHeader("Content-Disposition");

if (disposition && disposition.indexOf("attachment") !== -1) {
    var filenameRegex = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
    var matches = filenameRegex.exec(disposition);

    if (matches != null && matches[1]) {
        fileName = decodeURI(matches[1].replace(/['"]/g, ""));
    }
}
```

IE, Chrome, Safari 등 모든 browser에서 지원하도록 file download를 구현한다.  
고마워요 stack overflow!👍  
```
// for IE
if (window.navigator && window.navigator.msSaveOrOpenBlob) {
    window.navigator.msSaveOrOpenBlob(blob, fileName);
} else {
    var URL = window.URL || window.webkitURL;
    var downloadUrl = URL.createObjectURL(blob);

    if (fileName) {
        var a = document.createElement("a");

        // for safari
        if (a.download === undefined) {
            window.location.href = downloadUrl;
        } else {
            a.href = downloadUrl;
            a.download = fileName;
            document.body.appendChild(a);
            a.click();
        }
    } else {
        window.location.href = downloadUrl;
    }
}
```


결과적으로 다음과 같이 ajax를 이용해서 file download를 할 수 있다.  

```
$.ajax({
    url: url,
    data: parameters,
    type: 'POST',
    cache: false,
    xhrFields: {
        responseType: "blob",
    },
})
    .done(function (blob, status, xhr) {
        // check for a filename
        var fileName = "";
        var disposition = xhr.getResponseHeader("Content-Disposition");

        if (disposition && disposition.indexOf("attachment") !== -1) {
            var filenameRegex = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
            var matches = filenameRegex.exec(disposition);

            if (matches != null && matches[1]) {
                fileName = decodeURI(matches[1].replace(/['"]/g, ""));
            }
        }

        // for IE
        if (window.navigator && window.navigator.msSaveOrOpenBlob) {
            window.navigator.msSaveOrOpenBlob(blob, fileName);
        } else {
            var URL = window.URL || window.webkitURL;
            var downloadUrl = URL.createObjectURL(blob);

            if (fileName) {
                var a = document.createElement("a");

                // for safari
                if (a.download === undefined) {
                    window.location.href = downloadUrl;
                } else {
                    a.href = downloadUrl;
                    a.download = fileName;
                    document.body.appendChild(a);
                    a.click();
                }
            } else {
                window.location.href = downloadUrl;
            }
        }
    });
```

물론 [file download javascript 라이브러리](https://github.com/rndme/download) 또는 MVC Controller의 FileContentResult를 활용하면 더 쉽게 구현할 수 있다.