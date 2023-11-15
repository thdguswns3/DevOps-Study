### **주의사항** : 각 스택 배포 이후 반드시 해당 스택을 삭제 후 다음 실습을 진행해주세요.
## MSA
1. AWS Lambda 실행 과정을 Cold Start와 Warm Start로 구분지어 서술해주세요.
2. AWS Lambda의 Layer란 무엇인가요?
    - Python > requests 모듈을 Layer로 등록해주세요.
3. API Gateway를 구성하고 도메인을 등록해주세요.
4. ECS와 EKS의 차이점은 무엇인가요?
## System Architecture
1. Single Point of Failure란 무엇인가요?
    - 스택을 배포하고 서버에 Python locsut 모듈로 부하 테스트 코드를 작성 및 실행하고 부하에 따른 단일 장애점을 해결해보세요.
2. 스택을 배포하고 하기 내용을 참고하여 이중화로 동작하는 두 서버의 세션이 공유되도록 설정해주세요.
    - 스택 배포 후 Elasticache 클러스터 생성
        > 하기 옵션을 제외한 나머지는 기본 값 그대로 진행
    - 새 클러스터 구성 및 생성
    - 클러스터 모드 : 비활성화됨
    - 위치 : AWS 클라우드
        - 다중 AZ 및 자동 장애 조치 : 체크 해제
    - 클러스터 설정
        - 노드 유형 : cache.t2.micro
        - 복제본 개수 : 0
    - 보안
        - 암호화 : 체크 해제
        - 보안그룹 : Cache-SG
    - 서버 작업
        ```bash
        # 서버(2EA) SSM 접속 
        $sudo su -
        $cd /usr/share/tomcat

        $vi conf/redis-data-cache.properties
        ...
        redis.hosts=<Elasticache Endpoint>:6379
        ...

        $vi conf/context.xml
        <Context>  
            ...
            <Valve className="tomcat.request.session.redis.SessionHandlerValve" />
            <Manager className="tomcat.request.session.redis.SessionManager" />
            ...
        </Context>

        $vi conf/web.xml
        ...
        <session-config>
            <session-timeout>60</session-timeout>
        </session-config>
        ...

        $./bin/shutdown.sh
        $./bin/startup.sh
        ```
    - 서버 접속 : ALB-DNS/session_check.jsp
3. ECS를 구축하고 CodeSeries로 CI/CD 파이프라인을 구축해주세요.