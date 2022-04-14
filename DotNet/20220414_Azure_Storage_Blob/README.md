## Azure Storage - Blob Storage

우리 제품은 Saas이고 당연히 멀티 테넌시 아키텍쳐가 적용되어 있다.  
고객 테넌트마다 많은 파일이 생성되고 저장되고 있다.  
네트워크 드라이브에 수십만 개의 파일이 쌓였고 File Explorer에서나 프로그램에서 개별 파일에 접근하기 힘들어지기 시작했다.  
그렇게 대안을 찾았고 그것이 바로 Azure Storage의 [Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/#overview)다.  

지난 달 프로토타입을 개발해서 시범 적용을 끝냈고,  
드디어 오늘 대부분의 기능에 적용해서 배포를 완료했다.  

---

### 사용법

아래 방법으로 Azure Portal - Azure Storage 에서 Container를 추가한다.  
https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-portal

Blob Storage는 Azure SDK를 이용해서 간단히 이용이 가능하다.  
[BlobClient documentation](https://docs.microsoft.com/en-us/dotnet/api/azure.storage.blobs.blobclient?view=azure-dotnet)

``` C#
BlobContainerClient containerClient = new(connectionString, containerName);
BlobClient blobClient = containerClient.GetBlobClient(blobPath);

// blob 업로드
await containerClient.UploadBlobAsync(fileName, fileStream));

// Stream으로 blob 다운로드
Stream stream = await blobClient.DownloadStreamingAsync();

// 파일로 blob 다운로드
await blobClient.DownloadToAsync(downloadPath);

// blob이 존재하면 제거
// File.Exists()로 늘 존재하는지 확인하고 제거했는데 이젠 그럴 필요가 없다.
containerClient.DeleteBlobIfExistsAsync(blobName, snapshotsOption: DeleteSnapshotsOption.IncludeSnapshots);
```

친절하게도 샘플 코드를 제공해준다.  
https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/storage/Azure.Storage.Blobs/samples  


### CDN

위에서 만든 Container를 Azure CDN과 쉽게 통합할 수 있다.  
https://docs.microsoft.com/en-us/azure/cdn/cdn-create-a-storage-account-with-cdn

### Access Control

Blob Container 별로 access level을 설정해서 익명 사용자의 접근을 제한할 수 있다.  
게다가 shared access signature(SAS)를 이용하면 원하는 정책에 따라 blob 리소스로의 접근을 컨트롤할 수 있다.  
아래는 Service SAS를 활용한 예제다.

``` C#
BlobContainerClient containerClient = new(connectionString, containerName);
BlobClient blobClient = containerClient.GetBlobClient(blobPath);

Uri uri = GetServiceSasUriForBlob(blobClient);

// SAS URI로 접근
BlobClient sasBlobClient = new(uri, null);
```

``` C#
private Uri GetServiceSasUriForBlob(BlobClient blobClient, string storedPolicyName = null)
{
    if (blobClient.CanGenerateSasUri)
    {
        // Create a SAS token that's valid for one hour.
        BlobSasBuilder sasBuilder = new BlobSasBuilder()
        {
            BlobContainerName = blobClient.GetParentBlobContainerClient().Name,
            BlobName = blobClient.Name,
            Resource = "b",
        };

        if (storedPolicyName == null)
        {
            sasBuilder.ExpiresOn = DateTimeOffset.UtcNow.AddHours(1);
            sasBuilder.SetPermissions(BlobSasPermissions.Read | BlobSasPermissions.Write);
        }
        else
        {
            sasBuilder.Identifier = storedPolicyName;
        }

        Uri sasUri = blobClient.GenerateSasUri(sasBuilder);
        
        Console.WriteLine("SAS URI for blob is: {0}", sasUri);

        return sasUri;
    }
    else
    {
        Console.WriteLine(@"BlobClient must be authorized with Shared Key credentials to create a service SAS.");
        return null;
    }
}
```

이렇게 강력하고 편리한 Cloud Service를 제공해주는 MS, 감사하다.  
이런데도 아직 MS 주주가 아닌 사람이 있다고?