1. VPC란 무엇인가요?
2. 다음과 같은 예시 문제에 대한 솔루션을 제공해주세요.
    - Private Subnet 내 EC2 인스턴스의 어플리케이션이 S3 버킷의 특정 객체에 접근하고자 할 때 어떤 구성이 필요할까요?
3. VPC Endpoint 종류와 특징을 설명해주세요.
4. Private/Public Subnet 차이를 각각 설명해주세요.
5. 다음과 같이 생성한 Subnet의 IP 대역마다 예약된 IP 주소를 각각 서술해주세요.
    - 10.0.0.0/24
        1. 10.0.0.0
        2. 10.0.0.1
        3. 10.0.0.2
        4. 10.0.0.255
6. Public IP와 Elastic IP의 차이는 무엇인가요?
7. NACL과 Security Group의 차이는 무엇인가요?
8. Single Point of Failure란 무엇인가요?
9. 다음 로드밸런서의 특징을 설명해주세요.
    - Application Loadbalancer
    - Network Loadbalancer
    - Gateway Loadbalancer
10. Application Loadbalancer의 리스너 규칙엔 어떤 종류가 있을까요?
    - [스택](https://github.com/eljoelee/DevOps-Study/blob/main/AWS/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC_%EB%AC%B8%ED%95%AD_10%EB%B2%88.yaml)을 배포하고 다음 조건을 충족하는 리스너 규칙 생성 및 로드밸런싱 결과를 작성해주세요.
        1. 경로 '/one' 입력 시 Server-One으로 라우팅
        2. 경로 '/two' 입력 시 Server-Two으로 라우팅
        3. 기본 경로는 '404 Not Found' 에러 코드 반환
11. VPC와 온프레미스간 통신을 수행하려면 어떤 리소스를 사용해야 할까요?
12. 서로 다른 VPC간 통신을 수행하려면 어떤 리소스를 사용해야 할까요?
13. S3, Cloudfront를 활용하여 간단한 웹 페이지(index.html)를 호스팅해주세요.
    - S3와 Cloudfront에 CORS 설정을 적용해주세요.
    - 무료 도메인 제공 사이트([Link](https://iter.kr/%EB%AC%B4%EB%A3%8C-%EB%8F%84%EB%A9%94%EC%9D%B8-%ED%94%84%EB%A6%AC%EB%86%88/))를 통해 도메인을 제공받고 Route53으로 해당 도메인과 호스팅 중인 사이트를 연결해주세요.
    - 브라우저의 개발자 도구(F12)를 통해 Cache Hit와 Access Control Allow Origin 헤더를 찾고 결과를 작성해주세요.
    - 웹 페이지 내용을 수정하고 Cloudfront가 바로 반영하도록 조치하는 방법을 설명해주세요.
14. [스택](https://github.com/eljoelee/DevOps-Study/blob/main/AWS/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC_%EB%AC%B8%ED%95%AD_14%EB%B2%88.yaml)을 배포하고 하기 DVWA 실습으로 인한 모의 해킹 상황을 WAF 적용하여 방어 결과를 작성해주세요.
    1. SQL Injection 메뉴에서 User ID란에 **' OR 1=1 #**(특수문자 '`' 주의)를 입력하고 계정 정보 유출을 확인한다.
        - SQL Injection 공격을 방지하는 ManagedRule을 적용해주세요.
    2. XSS(Reflected) 메뉴에서 What's your name란에 아래와 같은 자바스크립트 코드를 입력하고 쿠키 탈취(Hello 출력 확인)를 확인한다.
        ```javascript
        <script>alert(document.cookie)</script>
        ```
        - XSS Exploit 공격을 방지하는 ManagedRule을 적용해주세요.
    3. Chrome 확장 앱에서 Browsec VPN 설치하고 Singapore로 우회하여 DVWA에 접속한다.
        - 해외 국가 접속을 차단하는 Custom Rule을 적용해주세요.