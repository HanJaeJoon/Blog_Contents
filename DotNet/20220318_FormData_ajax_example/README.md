# [.NET] FormData로 ajax request

client
``` js
$.ajax({
    url: "/common/file/upload-file", // url
    type: "POST",
    data: formdata, // FormData로 전달
    contentType: false,
    processData: false,
})
    .done(function (data) {
    });
```

Web API Controller 버전
``` C#
public async Task<HttpResponseMessage> UploadFiles()
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
            string name = httpContent.Headers.ContentDisposition.Name.Trim('\"');

            // formData의 name
            if (name == "file")
            {
                ContentDispositionHeaderValue cd = httpContent.Headers.ContentDisposition;
                
                // 파일 Stream
                Stream stream = await httpContent.ReadAsStreamAsync();
            }

            // formData의 value
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

MVC Controller 버전
``` c#
public ActionResult UploadFile(FormCollection formCollection)
{
    // FormCollection으로 편리하게 이용가능하다.
    string value = formCollection[$"{name}"];

    // Request.Files로 첨부된 파일을 가져올 수 있다.
    HttpFileCollectionBase files = Request.Files;

    return Json(result);
}
```