Freeduino - HUMA 부품 목록

## 부품 목록 ##

NAME               VALUE        EA  DESC
----------------   ---------  ----  ------------------------------------------------------
LDO                7805DT        1
USB2SERIAL IC      FT232BM       1  FT232BL로 대치 가능
DIODE              1N4004        1
PWR-JACK                         1
USB CONNECT                      1
PINHEADER          1X3           1  전원선택
PINHEADER          2x3           1  AVR ISP 6pin
PUSHBUTTON                       1
RESISTOR           10k           1
RESISTOR           470           4  `*`표시된 저항 3개는 330~1k 사이의 값으로 대치 가능
RESISTOR           27            2
RESISTOR           1k5           1
RESISTOR           1k            2
FUSE               PTC1812       1
LED                3mm           3  글자 방향으로 짧은 다리가 오도록 장착
RESOATOR           6MHz          1  **PCB상에 12MHz로 오기 되어 있음**
CRYSTAL            16MHz         1
CAPACITOR          22pF          2
CAPACITOR          100nF         7
CAPACITOR          47uF          2
CAPACITOR          10uF          1  **PCB상에 2.2uF으로 표시 되어 있음**
MCU                ATMEGA8       1  ATMEGA168/328로 대치 가능 
IC SOCKET

## 부품 가격 표 ##

다음 표는 부품 별 단가(PRICE), 최소구매수량(MOQ), 판매사이트링크(SITE) 입니다.

- [엘레파츠](http://www.eleparts.co.kr) 구입가로 조사하였습니다.
- 단가는 최소구매수량을 구입할 때의 *개당* 가격 입니다.
- 부가가치세 별도의 금액 입니다.
- 가격은 조사시점의 가격으로 현재와 다를 수 있습니다.
- 소켓 류는 긴 소켓으로 조사하였으며, 조립자가 잘라서 조립해야 합니다

NAME              REQ     PRICE  MOQ   ELEPARTS PN
---------------- ---- --------- ----  --------------------------------------------
7805                1       500    1    [EPX3333G](http://eleparts.co.kr/EPX3333G)
FT232BM             1      5300    1    [EPX3333H](http://eleparts.co.kr/EPX3333H)
1N4004              1        20   10    [EPX3333J](http://eleparts.co.kr/EPX3333J)
PWR-JACK            1        90    1    [EPX3333K](http://eleparts.co.kr/EPX3333K)
USB CONNECT         1       215    1    [EPX3333L](http://eleparts.co.kr/EPX3333L)
PINHEADER-1X3       1       145    1    [EPX3333M](http://eleparts.co.kr/EPX3333M)
PINHEADER-2x3       1         -    -    -
PUSHBUTTON          1        30    1    [EPX3333N](http://eleparts.co.kr/EPX3333N)
R-27                2        10   10    [EPX3333T](http://eleparts.co.kr/EPX3333T)
R-470               4        10   10    [EPX3333R](http://eleparts.co.kr/EPX3333R)
R-1k                2        10   10    [EPX34LRU](http://eleparts.co.kr/EPX34LRU)
R-1k5               1        10   10    [EPX3333B](http://eleparts.co.kr/EPX3333B)
R-10k               1        10   10    [EPX3333P](http://eleparts.co.kr/EPX3333P)
FUSE-PTC0805L       1              1    [EPX3FGFF](http://eleparts.co.kr/EPX3FGFF)
LED-R               1        40    1    [EPX3333U](http://eleparts.co.kr/EPX3333U)
LEG-G               1        40    1    [EPX3333V](http://eleparts.co.kr/EPX3333V)
LEG-Y               1        40    1    [EPX3333W](http://eleparts.co.kr/EPX3333W)
RESOATOR-6MHz       1       390    5    [EPX3333X](http://eleparts.co.kr/EPX3333X)
CRYSTAL-12MHz       1       220    2    [EPX3333Y](http://eleparts.co.kr/EPX3333Y)
C-22pF              2        12   10    [EPX33343](http://eleparts.co.kr/EPX33343)
C-100nF             7        25   10    [EPX33344](http://eleparts.co.kr/EPX33344)
C-47uF              2        35   10    [EPX33346](http://eleparts.co.kr/EPX33346)
C-10uF              1       160   10    [EPX33347](http://eleparts.co.kr/EPX33347)
ATMEGA8             1      4500    1    [EPX33348](http://eleparts.co.kr/EPX33348)
PINSOCKET-6         2       480    1    [EPX3333F](http://eleparts.co.kr/EPX3333F)
PINSOCKET-8         2         -    -    -
IC-SOCKET-28pin     1        60    5    [EPX3333D](http://eleparts.co.kr/EPX3333D)

ELEPARTS PN 으로 엘레파츠에서 검색하시면 해당 부품을 찾을 수 있습니다.
또는, 위 목록의 링크를 클릭하거나 다음과 같이 주소창에 입력해서 검색 결과를 바로 확인해 보세요.

    http://www.eleparts.co.kr/EPXNNNNN

위 주소에서, EPXNNNNN 대신 위 목록의 번호로 바꿔서 입력하면 됩니다.

> NOTE: HUMA 보드 1개를 만들 때의 수량(REQ)만큼 단가를 계산하면,
부가가치세 포함하여 15000원 가량의 금액이 나옵니다.
