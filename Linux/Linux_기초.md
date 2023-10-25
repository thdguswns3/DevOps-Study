# Linux 기초
1. AWS Free-tier 계정으로 EC2 Amazon Linux2 인스턴스(t2a.micro)를 생성하고 ssh로 접속해보세요.
    ```
    > ssh -i .\AWSJoon.pem ec2-user@3.35.229.32
        ,     #_
        ~\_  ####_        Amazon Linux 2023
        ~~  \_#####\
        ~~     \###|
        ~~       \#/ ___   https://aws.amazon.com/linux/amazon-linux-2023
        ~~       V~' '->
            ~~~         /
            ~~._.   _/
                _/ _/
            _/m/'
        Last login: Thu Oct 19 12:03:03 2023 from 210.222.90.65
        [ec2-user@joontest ~]$
    ```
    - 위 sshd 접속 과정을 설명해주세요.
    ```
    - TLS handshake Protocol 사용
    1. Client가 SYN 패킷 송신 (Client -> Server)

    2. Server가 SYN 패킷을 수신하면 SYN + ACK를 보냄(Server -> Client)

    3. Client가 SYN + ACK 패킷을 수신하면 Server에게 ACK를 보냄 (Client -> Server)

    4. Client Hello (Client -> Server)
    - Client가 Server에 연결을 시도하며 전송하는 패킷
    - 사용 가능한 Cipher Suite 목록, Session ID, SSL Protocol Version, Random byte 등을 전달
    - Cipher Suite는 SSL Protocol version, 인증서 검정, 데이터 암호화 프로토콜, Hash 방식등의 정보를 가지고 있음 -> 데이터 암호화에 사용

    5. Server Hello (Server -> Client)
    - Cipher Suite 중 하나를 선택하여 Client에 알림, SSL Protocol Version 등도 같이 송신

    6. Certificate (Server -> Client)
    - Server가 자신의 SSL 인증서(공개키)를 전달 / 개인키는 Server가 소유
    - Client는 Server가 보낸 SSL 인증서(CA의 개인키로 암호화되어 있음)를 모두에게 공개된 CA의 공개키를 사용하여 복호화 -> 복호화에 성공할 경우 인증서가 진짜임이 증명됨(인증서 검증)
    - 인증서 검증 후 데이터 암호화에 사용할 대칭키(비밀키)를 생성한 후 SSL 인증서(Server가 발행) 내부에 들어있던 공개키를 이용해 암호화하여 Server에게 전송

    7. Server Key Exchange / ServerHello Done (Server -> Client)
    - Server Key Exchange는 Server의 공개키가 SSL 인증서 내부에 없는 경우에 Server가 직접 전달
    - 공개키가 SSL 인증서 내부에 있을 경우 Server Key Exchange는 생략
    - 인증서 내부에 공개키가 있는 경우 Client가 CA의 공개키를 통해 인증서를 복호화하여 Server의 공개키를 얻을 수 있음
    - Server가 행동을 마쳤음을 알림(ServerHello Done)

    8. Client Key Exchange(Client -> Server)
    - Client가 생성한 대칭키를 Server의 공개키를 사용해 암호화하여 Server에게 전달
    - 대칭키를 전달하는 것이 SSL Handshake의 목적
    - 대칭키를 통해 데이터를 암호화하게 된다.

    9. ChangeCipherSpec / Finished 
    - Client, Server 모두가 서로에게 보내는 패킷으로 교환할 정보를 모두 교환한 뒤 통신할 준비가 다 되었음을 알리기 위한 패킷
    - Finished 패킷을 보내어 SSL Handshake를 종료

    ```
    - 퍼블릭 키는 어디에 있나요?
    ```
    Public-Key 는 클라이언트에 존재
    ```
    - 리눅스 내부에서 접속 포트 번호를 22에서 2022로 변경하려면 어떻게 할까요?
    ```
    1. 포트 변경(/etc/sshd/sshd_config)
    [ec2-user@joontest ssh]$ sed -i 's/#Port 22/Port 2022/g' /etc/sshd/sshd_config

    2. 변경된 설정 적용 여부 확인
    [ec2-user@joontest ssh]$ sudo grep "Port" /etc/ssh/sshd_config
    Port 2022

    3. sshd 서비스 재시작
    [ec2-user@joontest ssh]$ sudo systemctl restart sshd.service && sudo systemctl status sshd.service
    ● sshd.service - OpenSSH server daemon
        Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; preset: enabled)
        Active: active (running) since Thu 2023-10-19 12:32:55 UTC; 37ms ago
        Docs: man:sshd(8)
                man:sshd_config(5)
    Main PID: 3451 (sshd)
        Tasks: 1 (limit: 2131)
        Memory: 1.2M
            CPU: 11ms
        CGroup: /system.slice/sshd.service
                └─3451 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups"

    Oct 19 12:32:55 joontest systemd[1]: Starting sshd.service - OpenSSH server daemon...
    Oct 19 12:32:55 joontest sshd[3451]: Server listening on 0.0.0.0 port 2022.
    Oct 19 12:32:55 joontest sshd[3451]: Server listening on :: port 2022.
    Oct 19 12:32:55 joontest systemd[1]: Started sshd.service - OpenSSH server daemon.

    4. 보안 그룹 설정 변경 후 2022포트로 재 접속
    > ssh -i .\AWSJoon.pem ec2-user@3.35.229.32 -p 2022
    ,     #_
    ~\_  ####_        Amazon Linux 2023
    ~~  \_#####\
    ~~     \###|
    ~~       \#/ ___   https://aws.amazon.com/linux/amazon-linux-2023
    ~~       V~' '->
        ~~~         /
        ~~._.   _/
            _/ _/
        _/m/'
    Last login: Thu Oct 19 12:05:47 2023 from 210.222.90.65
    [ec2-user@joontest ~]$

    ```
2. 현재 사용 중인 리눅스의 파일 시스템을 조회하는 명령어를 입력하고 결과를 작성해주세요.
    ```
    [ec2-user@joontest ~]$ df -Th
    Filesystem     Type      Size  Used Avail Use% Mounted on
    devtmpfs       devtmpfs  4.0M     0  4.0M   0% /dev
    tmpfs          tmpfs     475M     0  475M   0% /dev/shm
    tmpfs          tmpfs     190M  2.9M  188M   2% /run
    /dev/xvda1     xfs        30G  1.7G   29G   6% /
    tmpfs          tmpfs     475M     0  475M   0% /tmp
    /dev/xvda128   vfat       10M  1.3M  8.7M  13% /boot/efi
    tmpfs          tmpfs      95M     0   95M   0% /run/user/1000
    ```


3. 최상위 루트 디렉토리('/')의 하위 디렉토리를 간략하게 설명해주세요.
    - /bin : 실행(바이너리)파일 존재, 기본적인 명령어가 저장되어있음
    - /dev : 시스템 디바이스 파일 존재, 물리적 장치들이 파일화 되어 저장되어있음, 하드디스크(/dev/sda), CD-ROM(/dev/cdrom) 등
    - /etc : 사용자가 설치한 프로세스 등의 시스템의 거의 모든 설정 파일들이 존재
    - /lib : 커널이 필요로하는 각종 라이브러리 파일 및 커널의 모듈 파일등이 존재
    - /mnt : 외부 디스크등을 사용자가 직접 마운트하면 mnt 디렉토리에 위치
    - /proc : 현재 메모리에서 동작중인 프로세스 정보가 파일형태로 존재
    - /usr : 일반 사용자들이 사용하는 디렉토리, /usr/bin에는 일반사용자용 명령어가 위치함
    - /var : 주로 로그파일, 캐싱파일, 웹서버 이미지 파일등이 존재
4. 현재 사용 중인 쉘과 사용 가능한 쉘의 목록을 확인하는 명령어를 각각 입력해주세요.
    ```
    [ec2-user@joontest /]$ echo $SHELL
    /bin/bash
    [ec2-user@joontest /]$ cat /etc/shells
    /bin/sh
    /bin/bash
    /usr/bin/sh
    /usr/bin/bash
    /bin/csh
    /bin/tcsh
    /usr/bin/csh
    /usr/bin/tcsh
    ```
    - 쉘이란 무엇일까요?
    ```
    사용자가 운영체제, 커널을 사용하기 위한 유저 인터페이스 역할을 해주는 것, 사용자의 명령어를 입력받고 그것을 해석하여 실행하도록 하는 역할
    ```
5. ls 명령어를 입력하면 현재 디렉토리 내 파일과 디렉토리의 목록을 반환합니다. 해당 명령어의 입력부터 출력까지의 과정을 설명해주세요.
    > 작성 키워드 : **fork & exec(system call)**

    ```
    ls 명령어를 입력하면 shell process가 fork하여 자식 process를 만들고, 그 자식 process가 exec하여 ls 바이너리를 로드해서 실행하는 과정이 발생
    ```
    - system call이란 무엇일까요?
    ```
    - 유저 레벨의 프로그램(응용프로그램)은 유저레벨의 함수들 만으로 많은 기능을 구현하기 힘듦
    -> 유저모드에서는 실행 불가
    -> 반드시 커널의 개입이 필요
    -> 커널모드로 전환 필요(system call 필요)
    - user process executing -> calls "system call" -> execute system call -> return from system call
    - system call은 프로그램이 운영 체제의 서비스를 사용하도록 요청하는 인터페이스
    - system call을 통해 프로그램은 운영 체제의 보호된 리소스에 접근하고, 주변 장치를 제어하며, 네트워크 통신 등의 작업을 수행
    - 시스템 콜은 다음과 같은 작업들에 사용됩니다:
        -   파일 시스템 작업: 파일 생성, 삭제, 읽기, 쓰기 등
        -   장치 관리: 장치 사용 요청, 해제 등
        -   정보 유지: 시간 및 날짜 설정/조회 등
        -   통신: 프로세스 간 통신(IPC), 네트워크 연결 등
        -   프로세스 제어: fork(복제), exec(실행), exit(종료) 등
    ```
6. ps -ef | grep "/bin/sh" 명령어를 입력해보시고, 파이프라인('**|**') 문자가 어떤 기능인지 설명해주세요.
    ```
    - ps -ef 의 출력 결과값을 가져와 grep "/bin/sh" 명령어의 입력값으로 수행

    ```
    - 마찬가지로 ls | sort | cd /home/ec2-user 명령어를 입력하고, 어떤 내용이 출력되는지 작성해주세요.
        - 만약 출력되지 않는다면 그 이유를 설명해주세요.
    ```
    cd 명령어는 표준 입력을 받지 않기 때문에 위 명령어는 정상적으로 실행되지 않음
    ```
7. pstree 명령어를 입력해주세요.
    ```
    [ec2-user@joontest /]$ pstree
    systemd─┬─2*[agetty]
            ├─amazon-ssm-agen───7*[{amazon-ssm-agen}]
            ├─atd
            ├─auditd───{auditd}
            ├─chronyd
            ├─dbus-broker-lau───dbus-broker
            ├─gssproxy───5*[{gssproxy}]
            ├─lsmd
            ├─rngd───{rngd}
            ├─sshd───sshd───sshd───bash───pstree
            ├─sssd─┬─sssd_be
            │      └─sssd_nss
            ├─systemd───(sd-pam)
            ├─systemd-homed
            ├─systemd-inhibit───acpid
            ├─systemd-journal
            ├─systemd-logind
            ├─systemd-network
            ├─systemd-resolve
            ├─systemd-udevd
            └─systemd-userdbd───3*[systemd-userwor]
    ```
    - 최상단 프로세스(init 또는 systemd)의 역할은 무엇인지 설명해주세요.

    ```
    - 모든 프로세스의 부모 프로세스
    - 시스템의 서비스를 시작하거나 중지하고, 사용자 세션을 관리하며, 시스템 종료나 재부팅 등의 작업을 수행
    ```
    - init과 systemd의 차이점을 설명해주세요.
    ```
    1. init
    - Unix, Linux 시스템에서 전통적으로 사용되는 최상단 프로세스
    - 시스템이 부팅될 때 커널에 의해 자동 실행되며, PID 1을 가짐
    - /etc/inittab 파일에 정의된 대로 다른 프로세스를 시작하고 관리

    2. systemd
    - 최근 대부분의 Linux 배포판에서 init의 대체제로 사용되는 최상단 프로세스
    - init과 같은 기본적인 기능을 수행함과 동시에 더 효율적인 병렬처리, 시스템 상태 로깅, 의존성 기반의 서비스 관리등과 같은 고급 기능 제공
    - 시스템의 부팅 시간을 줄이고, 시스템 작업을 더 쉽게 관리할 수 있게 해줌

    3. 주요 차이점
        3.1. 병렬처리
        - init은 순차적으로 서비스를 시작하고 각 서비스가 완전히 시작될 때까지 기다림
        - systemd는 가능한 한 많은 작업을 병렬로 실행하여 시스템 부팅 시간을 단축시킴

        3.2. 의존성 관리
        - systemd는 서비스 간의 의존성을 관리하여, 필요한 서비스만을 시작하고, 필요한 순서대로 서비스를 시작
        - init은 /etc/inittab에 명시된 순서대로 서비스를 시작하며, 의존성을 고려하지 않음

        3.3. 로깅
        - systemd는 journald 라는 로깅 시스템을 사용하여 시스템 메시지를 효율적으로 관리
        - init은 syslog를 사용하여 로그를 관리하며, 파일 기반의 로깅 방식을 사용

        3.4. cgroup 사용
        - systemd는 cgroups를 사용하여 프로세스들의 자원 사용을 제어하고, 서비스를 격리시킴
        - 서비스 안정성과 보안성을 향상
        - init은 기능 미 제공
    ```
8. 네이버(www.naver.com)의 IP 주소를 확인하는 명령어는 무엇인가요?
    ```
    [ec2-user@joontest /]$ nslookup
    > www.naver.com
    Server:         10.0.0.2
    Address:        10.0.0.2#53

    Non-authoritative answer:
    www.naver.com   canonical name = www.naver.com.nheos.com.
    Name:   www.naver.com.nheos.com
    Address: 223.130.195.200
    Name:   www.naver.com.nheos.com
    Address: 223.130.195.95
    ```
    - 실행 결과(IP 주소)를 받는 과정을 설명해주세요(DNS 질의 과정)
    ```
    1. 사용자가 nslookup www.naver.com 명령어를 입력하면, 로컬 DNS 서버(여기서는 10.0.0.2)에게 www.naver.com의 IP 주소를 요청
    2. 로컬 DNS 서버는 요청을 받아서 자신의 캐시를 확인합니다. 만약 캐시에 정보가 없다면 루트 DNS 서버에게 질의
    3. 루트 DNS 서버는 .com 도메인을 담당하는 TLD(Top-Level Domain) DNS 서버의 주소를 로컬 DNS 서버에게 전달
    4. 로컬 DNS 서버는 TLD DNS 서버에게 naver.com의 IP 주소를 요청
    5. TLD DNS 서버는 naver.com 도메인을 담당하는 Authoritative DNS 서버의 주소를 로컬 DNS 서버에게 전달
    6. 로컬 DNS 서버는 Authoritative DNS 서버에게 www.naver.com의 IP 주소를 요청
    7. Authoritative DNS 서버는 원하는 정보를 로컬 DNS 서버에게 전달
    8. 로컬 DNS 서버는 받은 정보를 사용자에게 전달하고, 동시에 자신의 캐시에 정보를 저장
    ```
    - /etc/hosts와 /etc/resolv.conf의 차이점을 설명해주세요.
    ```
    - /etc/hosts
        - 호스트 이름을 IP 주소에 매핑하는 역할을 하는 파일
        - 사용자가 특정 URL로 요청을 보낼 때 시스템은 가장 먼저 이 파일을 참조하여 도메인 이름을 IP 주소로 변환하려고 시도 
        - 주로 작은 네트워크 또는 테스트 환경에서 사용
    - /etc/resolv.conf
        - 시스템이 DNS 질의를 수행할 때 사용하는 DNS 서버의 IP 주소와 관련된 설정 파일
        - 네트워크 인터페이스를 통해 동적으로 업데이트될 수 있음
    ```
9. curl, telnet, ping의 차이점을 설명해주세요.
    ```
    1. curl
    - curl은 다양한 프로토콜을 사용하여 데이터를 전송하는 데 사용되는 툴
    - curl 명령어는 HTTP, HTTPS, FTP 등과 같은 프로토콜을 지원
    - URL을 통해 데이터를 전송하거나 받아올 수 있음
    - 웹 개발에서는 주로 REST API를 테스트하거나 웹 페이지의 내용을 가져오는 데 사용

    2. telnet
    - 원격 컴퓨터와 TCP/IP 연결을 통해 통신하는 데 사용되는 프로토콜 및 명령줄 도구
    - 원격 호스트에 로그인하거나 원격 호스트의 서비스가 정상적으로 작동하는지 테스트 가능
    - 특정 포트가 열려 있는지 확인하는 데 주로 사용

    3. ping
    - 네트워크 연결의 상태를 확인하는 데 사용되는 명령줄 도구
    - ping 명령어는 ICMP(Internet Control Message Protocol)를 사용하여 목적지 호스트에 에코 요청 패킷을 보내고 에코 응답 패킷을 수신
    - 응답 시간과 패킷 손실률을 통해 네트워크의 성능을 측정하거나 문제를 진단하는 데 사용
    ```
10. yum 패키지를 통해 httpd를 설치하고, 80 포트를 개방하여 서비스를 실행해주세요.
    ```
    [ec2-user@joontest /]$ sudo yum -y install httpd

    ''' 중략 '''

    Installed:
    apr-1.7.2-2.amzn2023.0.2.x86_64
    apr-util-1.6.3-1.amzn2023.0.1.x86_64
    apr-util-openssl-1.6.3-1.amzn2023.0.1.x86_64
    generic-logos-httpd-18.0.0-12.amzn2023.0.3.noarch
    httpd-2.4.56-1.amzn2023.x86_64
    httpd-core-2.4.56-1.amzn2023.x86_64
    httpd-filesystem-2.4.56-1.amzn2023.noarch
    httpd-tools-2.4.56-1.amzn2023.x86_64
    libbrotli-1.0.9-4.amzn2023.0.2.x86_64
    mailcap-2.1.49-3.amzn2023.0.3.noarch
    mod_http2-2.0.11-2.amzn2023.x86_64
    mod_lua-2.4.56-1.amzn2023.x86_64

    Complete!
    [ec2-user@joontest /]$ sudo systemctl start httpd

    ''' 보안 그룹 설정 진행 후 '''

    [ec2-user@joontest /]$ curl localhost:80
    <html><body><h1>It works!</h1></body></html>
    ```
    - yum과 apt의 차이점은 무엇인가요?
    ```
    - yum과 apt는 둘 다 리눅스 배포판에서 소프트웨어 패키지를 설치하고 관리하는 데 사용되는 패키지 관리 도구
    1. yum
        - Red Hat 계열의 리눅스 배포판(CentOS, Fedora 등)에서 사용되는 패키지 관리 도구
        - RPM(Red Hat Package Manager) 패키지를 관리하며, 패키지의 의존성을 자동으로 해결
        - /etc/yum.repos.d/ 디렉토리에 저장된 저장소(repository) 설정을 사용하여 패키지를 관리

    2. apt
        - apt는 Debian 계열의 리눅스 배포판(Debian, Ubuntu 등)에서 사용되는 패키지 관리 도구
        - DEB 패키지를 관리하며, 패키지의 의존성을 자동으로 해결
        - /etc/apt/sources.list 파일이나 /etc/apt/sources.list.d/ 디렉토리에 저장된 저장소 설정을 사용하여 패키지를 관리
    ```
    - httpd 포트 상태(LISTEN…)를 확인하는 명령어를 입력하고 결과를 작성해주세요.
    ```
    [ec2-user@joontest /]$ netstat -antp
    (Not all processes could be identified, non-owned process info
    will not be shown, you would have to be root to see it all.)
    Active Internet connections (servers and established)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name

    tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -

    tcp        0    448 10.0.1.148:22           210.222.90.65:52506     ESTABLISHED -

    tcp        0      0 10.0.1.148:46008        169.254.169.254:80      TIME_WAIT   -

    tcp6       0      0 :::22                   :::*                    LISTEN      -

    tcp6       0      0 :::80                   :::*                    LISTEN      -

    tcp6       0      0 ::1:34410               ::1:80                  TIME_WAIT   -

    ```
11. 다음은 리소스 모니터링을 수행하는 명령어 중 top 명령어를 수행한 결과입니다. 각각의 값이 무엇을 의미하는지 설명해주세요.
    ```bash
    $top
    top - 22:39:40 up 0 min,  0 users,  load average: 0.00, 0.00, 0.00
    Tasks:   5 total,   1 running,   4 sleeping,   0 stopped,   0 zombie
    %Cpu(s):  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
    MiB Mem :   6948.5 total,   6844.0 free,     75.0 used,     29.5 buff/cache
    MiB Swap:      0.0 total,      0.0 free,      0.0 used.   6733.4 avail Mem

    PID USER     PR  NI    VIRT    RES    SHR  S  %CPU  %MEM     TIME+  COMMAND
    1   root     20   0    1276    788    472  S   0.0   0.0   0:00.03  init
    14  root     20   0    1284    388     20  S   0.0   0.0   0:00.00  init
    15  root     20   0    1284    396     20  S   0.0   0.0   0:00.00  init
    16  eljoelee 20   0    6200   5028   3316  S   0.0   0.1   0:00.02  bash
    27  eljoelee 20   0    7788   3268   2904  R   0.0   0.0   0:00.00  top
    ```
    - load average
        - 시스템 부하 평균을 나타냄
        - 숫자 세 개는 각각 지난 1분, 5분, 15분 동안의 평균 부하를 의미
        - 부하란 시스템에서 실행 대기 중인 프로세스의 평균 개수를 의미
    - tasks : 현재 시스템에서 실행 중인 프로세스의 개수를 나타냄
        - sleeping : CPU 시간을 기다리고 있는 프로세스의 개수를 의미
        - zombie : 부모 프로세스에 의해 아직 회수되지 않은 종료된 프로세스를 의미
    - Cpu(s) : CPU 사용률을 나타내며, 다음의 하위 항목들을 포함
        - hi : 하드웨어 인터럽트로 인한 CPU 사용량을 의미
        - si : 소프트웨어 인터럽트로 인한 CPU 사용량을 의미
        
        (hi와 si 값이 높다는 것은 해당 시스템에서 인터럽트 처리에 많은 CPU 자원이 소비되고 있음을 의미)
    - MiB : Mem : 시스템 메모리 사용량
        - buff/cache : buff/cache: 버퍼와 캐시로 사용되고 있는 메모리 양을 의미
    - PR : 프로세스의 우선 순위
    - VIRT : 프로세스가 사용하는 가상 메모리의 총량
    - RES : 프로세스가 사용하는 실제 RAM 크기
    - SHR : 공유 메모리 크기
    - MEM : 프로세스가 사용하는 전체 물리 메모리의 비율

12. 메모리 사용량을 확인하는 명령어를 입력하고 결과를 작성해주세요.
    ```
    [ec2-user@joontest /]$ free -h
                total        used        free      shared  buff/cache   available
    Mem:           949Mi       141Mi       549Mi       2.0Mi       258Mi       661Mi
    Swap:             0B          0B          0B
    ```
    - swap이란 항목은 무엇을 의미하는 걸까요?
    ```
    - Swap은 시스템이 물리 메모리(RAM)가 부족할 때 사용하는 디스크 공간을 의미
    - 일종의 '가상 메모리'로 사용되며, 메모리가 부족할 때 운영체제가 자동으로 사용
    - 운영 체제는 RAM에서 사용하지 않는 페이지(메모리의 일부분)를 디스크의 Swap 영역으로 이동시켜 메모리를 확보
    - RAM은 더 많은 공간을 확보하게 되지만, Swap 영역은 RAM보다 훨씬 느리기 때문에 성능에 영향을 줄 수 있음
    ```
      - 2GB 가량의 swap 메모리를 설정하고 메모리 사용량을 확인하는 명령어를 통해 결과를 작성해주세요.
    ```
    1. Swap 파일 메모리 할당
    [ec2-user@joontest /]$ sudo dd if=/dev/zero of=/swapfile bs=128M count=16
    16+0 records in
    16+0 records out
    2147483648 bytes (2.1 GB, 2.0 GiB) copied, 31.2296 s, 68.8 MB/s
    - dd: 'data duplicator'의 약자로, 낮은 수준에서 데이터를 복사하거나 변환하는 데 주로 사용
    - if=/dev/zero: 입력 파일(input file)을 지정, /dev/zero는 Linux 시스템에서 제공하는 특수 파일로, 읽을 때마다 null 바이트(0x00)가 계속 생성
    - of=/swapfile: 출력 파일(output file)을 지정합니다. 여기서는 '/swapfile'이라는 이름의 파일에 데이터를 쓰게 됩니다.
    - bs=128M: 'block size'의 약자로, 한 번에 읽고 쓸 데이터 블록의 크기를 지정 / 128MB 크기의 블록으로 설정됨
    - count=16: 'count' 옵션은 'bs' 옵션으로 지정된 블록 크기 단위로 얼마나 많은 데이터를 복사할 것인지 결정 / count 값은 16으로 설정되어 있으므로 총 2GB (128MB * 16 = 2048MB) 크기의 swap file이 생성됨


    2. swapfile에 접근 권한 설정
    [ec2-user@joontest /]$ sudo chmod 600 /swapfile

    3. swapfile을 추가할 swap 공간을 생성
    [ec2-user@joontest /]$ sudo mkswap /swapfile
    Setting up swapspace version 1, size = 2 GiB (2147479552 bytes)
    no label, UUID=c3c7f352-dc45-4545-9149-c4a918ea5ed

    4. swapfile을 swap memory에 추가
    [ec2-user@joontest /]$ sudo swapon /swapfile

    5. /etc/fstab 설정에 추가
    [ec2-user@joontest /]$ sudo vi /etc/fstab
    하단에 추가
    /swapfile swap swap defaults 0 0

    - /swapfile: 마운트할 디바이스 또는 파티션의 경로
    - swap: 마운트 포인트, 여기서 'swap'은 스왑 공간임을 의미
    - swap: 파일 시스템 타입, 여기서도 'swap'은 스왑 공간임을 의미
    - defaults: 마운트 옵션, 'defaults'는 기본 옵션을 사용하겠다는 의미
    - 0: dump 유틸리티가 해당 파티션의 백업을 수행해야 하는지 여부 (0: 백업하지 않음)
    - 0: fsck 명령어가 부팅시에 해당 파티션의 체크를 수행해야 하는 순서 (0: 체크하지 않음)

    6. 확인
    [ec2-user@joontest /]$ free -h
                total        used        free      shared  buff/cache   available
    Mem:           949Mi       160Mi       169Mi       3.0Mi       620Mi       637Mi
    Swap:          2.0Gi          0B       2.0Gi

    ```