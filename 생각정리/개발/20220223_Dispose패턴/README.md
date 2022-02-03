# [C#] Dispose 패턴

요즘 메모리를 효율적으로 사용하는 작업을 진행하고 있다.  
Visual Studio의 diagnostic tools로 메모리 사용량을 확인할 수 있다.  

![](./images/1.png)

`IDisposable` 인터페이스를 통해 메모리를 낮추는 데 성공했다(ID: 2).  
(그런데 정작 개발 서버에서는 잘 동작하지 않아서 `GC.Collect()` 사용을 고민 중이다.)  

---  

Dispose 패턴에서는 반드시 finalizer를 구현해야 한다.  
=> 사용자가 Dispose() 메서드를 올바르게 호출할 것이라고 믿으면 안 됨.  

`IDisposable.Dispose()` 는 반드시 다음과 같은 작업을 수행해야 한다.
- 모든 비관리 리소스를 정리한다.
- 모든 관리 리소스를 정리한다.
- 객체가 이미 정리되었음을 나타내기 위한 플래그 설정.
- finalizer 호출 회피(`GC.SuppressFinalize(this)`)


`Dispose()` 내에서는 리소스 정리 작업만 수행해야 한다. 다른 작업은 절대 수행하면 안 된다.  

`IDisposable` 인터페이스만 필요하고 finalizer를 구현할 필요가 없는 경우라도 표준 Dispose 패턴의 구조는 온전히 유지하는 것이 좋다.

코드 예시  
``` C#
public class MyResourceHog : IDisposable
{
    // 이미 dispose 되었는지 확인하는 플래그
    private bool alreadyDisposed = false;

    // 비관리 리소스를 포함하는 경우에만 finalizer 구현
    ~MyResourceHog()
    {
        this.Dispose(false);
    }

    public void Dispose()
    {
        Dispose(true); // Dispose(bool) 호출
        GC.SuppressFinalize(this); // finalizer 호출 회피
    }

    protected virtual void Dispose(bool isDisposing)
    {
        if (alreadyDisposed) return;

        if (isDisposing)
        {
            // 관리 리소스 정리
        }
        
        // 비관리 리소스 정리

        alreadyDisposed = true; // flag 설정
    }

    public void ExampleMethod()
    {
        if (alreadyDisposed)
        {
            // ObjectDisposedException 발생(Dispose 패턴 규칙)
            throw new ObjectDisposedException("MyResourceHog", 
                "Called Example Method on Disposed object.");
        }
    }
}
```
