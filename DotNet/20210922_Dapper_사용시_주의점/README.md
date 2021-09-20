# [.NET] Dapper 사용시 주의점

[Dapper](https://github.com/DapperLib/Dapper)를 사용중인데 Temp Table을 사용하는 경우에 두번째 `ExecuteAsync` 에서 접근하지 못하는 문제가 있었다.  
찾아보니 ***DB connection을 명시적으로 Open 해놓으면 Dapper 내부에서 DB Connection을 Open/Close를 하는 것을 방지할 수 있다.***
```
await conn.OpenAsync();
```

> The point about temporary tables is that they're limited to the scope of the connection. Dapper will automatically open and close a connection if it's not already opened. That means that any temp table will be lost directly after creating it, if the connection passed to Dapper has not been opened.

- https://riptutorial.com/dapper/example/23692/how-to-work-with-temp-tables