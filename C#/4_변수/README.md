## 변수

### 값 형식과 참조 형식

값 형식: 스택  
참조 형식: 스택(힙의 주소 저장) + 힙(실제 값 저장)

힙 영역은 가비지 콜렉터가 수거함.

### 2진수, 10진수, 16진수

2진수 리터럴 접두사 0b  
16진수 리터럴 접두사 0x  

### float vs double vs decimal

float(부동소수점)은 정밀도 면에서 한계가 있어서 수소 데이터를 다룰 떄 double을 사용해야 한다.  
double보다 데이터 손실이 적은 것은 decimal.  
(decimal은 정밀도가 중요한 필요한 남아공 billing 프로젝트에서 사용하기도 했음)  

float 리터럴 접미사 f  
double은 접미사 없음  
decimal 리터럴 접미사 m  

### object의 박싱, 언박싱

object는 모든 데이터 타입의 조상 클래스  
박싱: 값 형식 데이터를 힙에 할당하기 위한 기능  
언박싱: 힙에 할당된 데이터를 값 형식 변수에 저장하는 기능  

### nullable type

HasValue, Value 로 값이 있는지 확인, 값 확인 가능

### CTS(Common Type System)

다른 프로그래밍 언어와의 호환성을 갖도록 하는 Type을 지원함.  
제품 소스코드에 가끔 보이는 Int32, Int64 C++에서 사용되는 형식이다.  

### 문자열 보간

내가 그동안 리터럴 템플릿이라고 했던 것이 문자열 보간이었다. 😮  
https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated