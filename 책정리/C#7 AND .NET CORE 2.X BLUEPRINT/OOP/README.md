## OOP

## 객체지향 프로그램 4대 원칙

### 추상화(Abstraction)
어떻게 하는지를 기술하지 않고 무엇을 해야 하는지를 기술하는 것.  
약속을 기술하지만 약속에 대한 완전한 구현을 제공하지 않는 형태  
abstract class, interface, Stream, IEnumerable<T>, Object 등

### 다형성(Polymorphism)
컴파일 다형성: 이름은 같지만 시그니처가 다른 메서드로 다양한 기능을 수행하는 것  (오버로딩, 초기 바인딩, 정적 바인딩)  
런타임 다형성: 이름과 서명이 동일한 메서드를 선언하는 것  
(오버라이딩, 후기 방인딩, 동적 바인딩)

### 상속(Inheritance)
기본 클래스에 정의한 동작을 재사용, 확장, 수정해 고유의 클래스를 만들 수 있는 기능

### 캡슐화(Encapsulation)
내부 동작을 외부 코드에 공개하는 것을 엄격하게 제한한다.  
private 키워드
