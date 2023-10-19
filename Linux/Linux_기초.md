# Linux 기초
1. AWS Free-tier 계정으로 EC2 Amazon Linux2 인스턴스(t2a.micro)를 생성하고 ssh로 접속해보세요.
```
    $ ssh -i .\AWSJoon.pem ec2-user@3.35.229.32
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
- SSL handshake Protocol 사용
1. Client Hello


2. 

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
PS C:\Users\thdgu\OneDrive\Desktop> ssh -i .\AWSJoon.pem ec2-user@3.35.229.32 -p 2022
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
3. 최상위 루트 디렉토리('/')의 하위 디렉토리를 간략하게 설명해주세요.
    - /bin
    - /dev
    - /etc
    - /lib
    - /mnt
    - /proc
    - /usr
    - /var
4. 현재 사용 중인 쉘과 사용 가능한 쉘의 목록을 확인하는 명령어를 각각 입력해주세요.
    - 쉘이란 무엇일까요?
5. ls 명령어를 입력하면 현재 디렉토리 내 파일과 디렉토리의 목록을 반환합니다. 해당 명령어의 입력부터 출력까지의 과정을 설명해주세요.
    > 작성 키워드 : **fork & exec(system call)**
    - system call이란 무엇일까요?
6. ps -ef | grep "/bin/sh" 명령어를 입력해보시고, 파이프라인('**|**') 문자가 어떤 기능인지 설명해주세요.
    - 마찬가지로 ls | sort | cd /home/ec2-user 명령어를 입력하고, 어떤 내용이 출력되는지 작성해주세요.
        - 만약 출력되지 않는다면 그 이유를 설명해주세요.
7. pstree 명령어를 입력해주세요.
    - 최상단 프로세스(init 또는 systemd)의 역할은 무엇인지 설명해주세요.
    - init과 systemd의 차이점을 설명해주세요.
8. 네이버(www.naver.com)의 IP 주소를 확인하는 명령어는 무엇인가요?
    - 실행 결과(IP 주소)를 받는 과정을 설명해주세요(DNS 질의 과정)
    - /etc/hosts와 /etc/resolv.conf의 차이점을 설명해주세요.
9. curl, telnet, ping의 차이점을 설명해주세요.
10. yum 패키지를 통해 httpd를 설치하고, 80 포트를 개방하여 서비스를 실행해주세요.
    - yum과 apt의 차이점은 무엇인가요?
    - httpd 포트 상태(LISTEN…)를 확인하는 명령어를 입력하고 결과를 작성해주세요.
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
    - tasks
        - sleeping
        - zombie
    - Cpu(s)
        - hi
        - si
    - MiB
        - buff/cache
    - PR
    - VIRT
    - RES
    - SHR
    - MEM
12. 메모리 사용량을 확인하는 명령어를 입력하고 결과를 작성해주세요.
    - swap이란 항목은 무엇을 의미하는 걸까요?
        - 2GB 가량의 swap 메모리를 설정하고 메모리 사용량을 확인하는 명령어를 통해 결과를 작성해주세요.
