# [.NET] FormData를 이용한 file upload

이번에 제품의 file upload 기능을 개선하게 되었다.  
분명 예전에 upload API prototype을 구현했던 것 같은데 기록을 안 해두니 까먹었다.  

요즘 내 블로그에서 가장 인기 글은 file download 관련된 글이다.  
(놀랍게도 의무교육 스킵하는 법이 아니다!)  
https://jjester.tistory.com/106

upload도 많이들 찾아오기를 바라며 잘 기록해야지.

---  

HTML Form Element을 이용해 서버로 request를 할 수 있다.  
[FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData)를 통해 쉽게 사용할 수 있기도 하다.  

jquery `ajax()`를 이용해서 formData를 서버에 전달할 수 있다.  
이때 formData에는 `<input type="file">`이 포함되어 file도 전달한다.

### Client
``` js
$.ajax({
    url: url
    type: "POST",
    data: formData, // FormData
    contentType: false,
    processData: false,
})
    .done(function (data) {
    });
```

.Net 5 이전 버전에는 MVC Controller와 Web API Controller가 존재한다.  
(.Net 5 에서 MVC Controller와 Web API Controller가 통합된다.)  
- MVC: System.Web.MVC, 주로 ActionResult(View)를 리턴한다.
- Web API: System.Web.Http, 주로 데이터를 리턴한다.

우리 제품은 **아직은** .Net 5 이전이니 각각의 구현 방식을 비교해보자.  

### Web API Controller 버전
``` C#
public async Task<HttpResponseMessage> UploadFile()
{
    // Check if the request contains multipart/form-data.
    if (!Request.Content.IsMimeMultipartContent())
    {
        throw new HttpResponseException(HttpStatusCode.UnsupportedMediaType);
    }

    try
    {
        // Read the form data.
        MultipartMemoryStreamProvider s = await Request.Content.ReadAsMultipartAsync();

        foreach (HttpContent httpContent in s.Contents)
        {
            // 왜인지 모르겠지만 쌍따옴표로 감싸져서 리턴된다.
            string name = httpContent.Headers.ContentDisposition.Name.Trim('\"');

            // formData에서 input[type="file"]의 name attribute
            // 업로드할 파일을 가져오기위해 별도로 처리한다.
            if (name == "file")
            {
                ContentDispositionHeaderValue cd = httpContent.Headers.ContentDisposition;
                
                // 업로드할 파일 Stream
                Stream stream = await httpContent.ReadAsStreamAsync();
            }

            // 업로드할 파일을 제외한 나머지 formData의 value. 모두 string으로 가져온다.
            string value = httpContent.ReadAsStringAsync().Result;
        }

        return Request.CreateResponse(HttpStatusCode.OK);
    }
    catch (System.Exception e)
    {
        return Request.CreateErrorResponse(HttpStatusCode.InternalServerError, e);
    }
}
```

### MVC Controller 버전
``` c#
public ActionResult UploadFile(FormCollection formCollection)
{
    // FormCollection으로 편리하게 이용가능하다.
    string value = formCollection[$"{name}"];

    // Request.Files로 첨부된 파일을 가져올 수 있다.
    HttpFileCollectionBase files = Request.Files;

    // HttpPostedFileBase.InputStream를 활용하면 너무나도 편하다.
    // Stream stream = files[i].InputStream;

    return Json(result);
}
```

FormData의 데이터를 가져오기 위해서  
Web API는 복잡한 반면에 MVC는 쉽게 사용할 수 있다.