#!/usr/bin/env python3
"""Generate localized HUMA site pages. Run from repo: python3 site/_build_i18n.py"""

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LANGS = ("ko", "en", "ja", "zh")
LANG_LABELS = {
    "ko": "한국어",
    "en": "English",
    "ja": "日本語",
    "zh": "中文",
}

# Shared asset paths from lang folders
CSS = "../styles.css"
JS = "../site.js"
PIC = "../pics"

CC = {
    "ko": "http://creativecommons.org/licenses/by-sa/3.0/deed.ko",
    "en": "http://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "ja": "http://creativecommons.org/licenses/by-sa/3.0/deed.ja",
    "zh": "http://creativecommons.org/licenses/by-sa/3.0/deed.zh",
}

UI = {
    "ko": {
        "nav_aria": "주요 메뉴",
        "nav_guide": "조립",
        "nav_bom": "부품 목록",
        "toc_aria": "목차",
        "toc": "목차",
        "lang_aria": "언어",
        "brand_guide": "조립 설명서",
        "brand_bom": "부품 목록",
        "footer_left": "HUMA · HUman Madeable Arduino · ",
    },
    "en": {
        "nav_aria": "Primary",
        "nav_guide": "Build",
        "nav_bom": "Parts",
        "toc_aria": "Contents",
        "toc": "Contents",
        "lang_aria": "Language",
        "brand_guide": "Assembly guide",
        "brand_bom": "Parts list",
        "footer_left": "HUMA · HUman Madeable Arduino · ",
    },
    "ja": {
        "nav_aria": "メインメニュー",
        "nav_guide": "組み立て",
        "nav_bom": "部品一覧",
        "toc_aria": "目次",
        "toc": "目次",
        "lang_aria": "言語",
        "brand_guide": "組み立てガイド",
        "brand_bom": "部品一覧",
        "footer_left": "HUMA · HUman Madeable Arduino · ",
    },
    "zh": {
        "nav_aria": "主导航",
        "nav_guide": "组装",
        "nav_bom": "零件清单",
        "toc_aria": "目录",
        "toc": "目录",
        "lang_aria": "语言",
        "brand_guide": "组装说明",
        "brand_bom": "零件清单",
        "footer_left": "HUMA · HUman Madeable Arduino · ",
    },
}


def lang_switch(current: str, page: str) -> str:
    opts = []
    for code in LANGS:
        sel = ' selected' if code == current else ""
        opts.append(f'<option value="{code}"{sel}>{LANG_LABELS[code]}</option>')
    return f"""<label class="lang-switch">
        <span class="visually-hidden">{UI[current]["lang_aria"]}</span>
        <select data-lang-switch data-page="{page}" aria-label="{UI[current]["lang_aria"]}">
          {"".join(opts)}
        </select>
      </label>"""


def header(lang: str, page: str) -> str:
    ui = UI[lang]
    brand = ui["brand_guide"] if page == "index" else ui["brand_bom"]
    brand_href = "index.html"
    guide_cur = ' aria-current="page"' if page == "index" else ""
    bom_cur = ' aria-current="page"' if page == "bom" else ""
    return f"""  <header class="site-header">
    <div class="site-header__inner">
      <a class="brand" href="{brand_href}">HUMA <span>{brand}</span></a>
      <nav class="nav" aria-label="{ui["nav_aria"]}">
        <a href="index.html"{guide_cur}>{ui["nav_guide"]}</a>
        <a href="bom.html"{bom_cur}>{ui["nav_bom"]}</a>
        <a class="nav-external" href="https://github.com/suapapa/HUMA" rel="noopener noreferrer">GitHub</a>
        {lang_switch(lang, page)}
      </nav>
    </div>
  </header>"""


def footer(lang: str) -> str:
    ui = UI[lang]
    return f"""  <footer class="site-footer">
    <div class="site-footer__inner">
      <p>{ui["footer_left"]}<a href="{CC[lang]}">CC BY-SA</a></p>
      <p>Homin Lee &lt;<a href="mailto:i@homin.dev">i@homin.dev</a>&gt;</p>
    </div>
  </footer>"""


GUIDE = {}

GUIDE["ko"] = {
    "title": "HUMA 조립 설명서",
    "desc": "HUMA는 직접 납땜해 조립하는 아두이노 호환 보드입니다. 부품 점검부터 납땜, 부트로더까지 단계별로 안내합니다.",
    "toc": [
        ("#tools", "도구 및 준비물"),
        ("#solder", "납땜하기"),
        ("#bootloader", "부트로더 굽기"),
    ],
    "h1": "HUMA 조립 설명서",
    "hero": """HUMA는
            프리두이노(Freeduino)를 기반으로 한 아두이노 호환 보드입니다.
            예전 라디오 키트를 조립하듯 모든 부품을 손수 납땜하며 만들 수 있도록 설계되었습니다.
            기초적인 납땜 경험만 있다면 누구나 완성할 수 있습니다.""",
    "cta_start": "조립 시작",
    "cta_bom": "부품 목록",
    "pcb_alt": "HUMA PCB 보드",
    "pcb_cap": "HUMA PCB",
    "body": f"""
      <p>
        납땜이 오랜만이거나 익숙하지 않다면
        <a href="https://homin.dev/blog/p=460/">만화로 배우는 납땜</a>을 먼저 살펴보세요.
      </p>
      <p>
        HUMA는 오픈소스 하드웨어입니다. 조립 및 사용 과정에서 발생하는 보드 손상이나
        인적·물적 피해에 대해서는 어떠한 책임도 지지 않습니다.
      </p>
      <p>
        회로도, 아트워크 및 관련 문서는 모두
        <a href="{CC["ko"]}">CC BY-SA</a>
        라이선스를 따릅니다.
      </p>

      <aside class="callout callout-warn" role="note">
        <p>
          <strong>안전 주의사항</strong>
          작업자의 안전은 스스로 지켜야 합니다. 조립할 때는 보안경 등 보호장구를 착용하고,
          가열된 인두기에 화상을 입지 않도록 각별히 주의하세요. 환기가 잘되는 곳에서 작업하는 것을 권장합니다.
        </p>
      </aside>

      <h2 id="tools">도구 및 준비물</h2>
      <div class="figure-pair">
        <figure class="figure">
          <img src="{PIC}/00_tools.webp" alt="조립에 필요한 도구" width="640" height="480" loading="lazy" />
          <figcaption>조립 도구</figcaption>
        </figure>
        <figure class="figure">
          <img src="{PIC}/00_check_parts.webp" alt="부품 점검" width="640" height="480" loading="lazy" />
          <figcaption>부품 점검</figcaption>
        </figure>
      </div>
      <p>
        HUMA PCB와 <a href="bom.html">부품 목록</a>을 대조하며 필요한 부품이 빠짐없이 준비되었는지 확인합니다.
      </p>

      <h2 id="solder">납땜하기</h2>
      <p>
        부품은 높이가 낮은 것부터 높은 것 순으로, 기판의 안쪽에서 바깥쪽으로,
        열에 강한 부품부터 약한 부품 순으로 납땜하는 것이 기본 원칙입니다.
      </p>
      <p>
        먼저 높이가 가장 낮은 3.3V 전원용 SMD 커패시터부터 납땜해 보겠습니다.
        SMD 커패시터는 플러스(+) 극 쪽에 띠 모양 표시가 있습니다.
      </p>

      <figure class="figure">
        <img src="{PIC}/01_solder_smd_cap.webp" alt="SMD 커패시터 자리 잡기" width="800" height="600" loading="lazy" />
        <figcaption>SMD 커패시터 위치 잡기</figcaption>
      </figure>

      <p>보드의 2.2u 글자 방향으로 띠가 오도록 위치를 맞춘 뒤, 한쪽 접점을 먼저 납땜해 고정합니다.</p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>참고</strong>
          보드 실크에는 2.2u로 표기되어 있으나, 실제로는 10uF 커패시터를 사용했습니다.
        </p>
      </aside>

      <figure class="figure">
        <img src="{PIC}/02_solder_smd_cap.webp" alt="SMD 커패시터 반대편 접점 납땜" width="800" height="600" loading="lazy" />
        <figcaption>반대편 접점 납땜</figcaption>
      </figure>

      <p>
        자리가 잡히면 반대편 접점을 마저 납땜합니다. 이어서 커패시터 옆의 솔더 점퍼에 납을 올려
        USB와 3V3 패드를 연결해 줍니다. 이렇게 하면 USB 시리얼 칩(FT232BL)이 공급하는 3.3V를 보드 전원으로 사용하게 됩니다.
      </p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>참고</strong>
          3.3V 전원에서 더 큰 전류가 필요한 회로를 구성한다면, HUMA 보드 뒷면에 MIC5219 레귤레이터와 470pF 커패시터를 장착하고
          솔더 점퍼의 LDO와 3V3을 연결하세요. 5V 전원에서 변환된 넉넉한 3.3V 전원을 공급받을 수 있습니다.
        </p>
      </aside>

      <p>
        다음으로 USB-시리얼 변환 칩인 FT232BL(또는 FT232BM)을 납땜합니다. SMD IC 납땜 경험이 없다면
        <a href="https://homin.dev/blog/p=481/">SMD 납땜하기</a> 가이드를 먼저 참고하세요.
      </p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>참고</strong>
          확대경이나 루페를 사용해 SMD 핀들이 쇼트(합선) 없이 잘 연결되었는지 꼼꼼히 확인합니다.
          다른 부품들을 모두 장착하고 난 뒤에는 납땜 불량을 수정하기가 무척 까다롭습니다.
        </p>
      </aside>

      <p>
        보드에는 100nF 커패시터가 총 7개 들어갑니다. SMD(1608 규격)와 원형 디스크 모양의 세라믹 커패시터 중
        원하는 부품을 골라 장착할 수 있도록 패드가 겸용으로 마련되어 있습니다. SMD 커패시터를 준비했다면 지금 납땜해 줍니다.
        100nF 커패시터는 극성이 없으므로 방향을 구분하지 않아도 됩니다.
      </p>
      <p>여기까지 마쳤다면 보드 조립에서 가장 까다로운 SMD 부품 납땜이 끝났습니다.</p>

      <figure class="figure">
        <img src="{PIC}/03_solder_lead_parts.webp" alt="리드 부품 납땜 시작" width="800" height="600" loading="lazy" />
        <figcaption>리드 부품 납땜</figcaption>
      </figure>

      <p>
        보드에 표기된 저항값에 맞추어 저항들을 꽂고 납땜합니다. 1/4W 또는 1/8W 규격의 일반 저항(정밀도 5%)을 사용하면 됩니다.
        높은 정밀도(1%)의 저항은 가격이 더 비싸지만, 이런 디지털 회로에서는 뚜렷한 장점이 없습니다.
        1/2W 규격 저항은 가격은 같으나 크기가 커서 패드에 꽂기 번거롭습니다.
      </p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>참고</strong>
          <code>*470</code>으로 표시된 저항 3개는 LED 전류 제한용 저항입니다. 꼭 470Ω이 아니더라도
          330Ω~1kΩ 사이의 저항을 사용해도 무방합니다. (예시 제작에서는 부품 상자에 여유가 있던 680Ω을 사용했습니다.)
        </p>
      </aside>

      <figure class="figure">
        <img src="{PIC}/04_solder_lead_parts.webp" alt="저항과 다이오드, 비드 장착" width="800" height="600" loading="lazy" />
        <figcaption>다이오드와 비드 장착</figcaption>
      </figure>

      <p>
        전원 잭 옆의 다이오드와 USB 커넥터 아래의 비드(Ferrite Bead)를 납땜합니다. 비드 대신 정품 아두이노처럼
        PTC0805 자리에 복구형 퓨즈(Resettable Fuse)를 장착할 수도 있습니다. 비드와 퓨즈 중 편한 부품을 하나 골라 장착하세요.
      </p>

      <figure class="figure">
        <img src="{PIC}/05_solder_7805.webp" alt="7805 레귤레이터 자리 잡기" width="800" height="600" loading="lazy" />
        <figcaption>7805 레귤레이터 자리 잡기</figcaption>
      </figure>

      <p>보드를 뒤집어 5V 레귤레이터인 7805를 납땜합니다. 먼저 한쪽 다리 패드에 납을 살짝 올려 위치를 잡은 뒤,</p>

      <figure class="figure">
        <img src="{PIC}/06_solder_7805.webp" alt="7805 나머지 패드 납땜" width="800" height="600" loading="lazy" />
        <figcaption>7805 납땜 완료</figcaption>
      </figure>

      <p>자리가 반듯하게 잡히면 나머지 패드들을 마저 납땜합니다.</p>

      <figure class="figure">
        <img src="{PIC}/07_solder_crystal.webp" alt="레조네이터와 크리스탈 장착" width="800" height="600" loading="lazy" />
        <figcaption>레조네이터와 크리스털</figcaption>
      </figure>

      <p>레조네이터(파란 부품)와 크리스털(은색 부품)을 납땜합니다.</p>

      <figure class="figure">
        <img src="{PIC}/08_solder_led.webp" alt="LED 세 개 장착" width="800" height="600" loading="lazy" />
        <figcaption>LED 장착</figcaption>
      </figure>

      <p>
        3mm LED 3개를 연결합니다. LED는 극성이 있으므로 방향을 잘 맞추어 장착해야 합니다.
        보드 표기(R/T, L, PWR) 쪽으로 짧은 다리(또는 테두리가 깎인 면)가 오도록 꽂아 줍니다.
      </p>

      <figure class="figure">
        <img src="{PIC}/09_solder_ic_socket.webp" alt="IC 소켓 장착" width="800" height="600" loading="lazy" />
        <figcaption>IC 소켓 장착</figcaption>
      </figure>

      <p>
        ATmega용 IC 소켓을 장착합니다. 사진에서는 필요한 핀 수만큼 잘라 쓰는 소켓을 사용했습니다.
        소켓이 들뜨지 않고 반듯하게 붙도록 마스킹 테이프와 핀헤더 소켓으로 임시 고정한 뒤 납땜했습니다.
      </p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>참고</strong>
          종이 테이프(마스킹 테이프)는 작업 직후 떼어내면 끈적임이 남지 않습니다.
          3cm 정도로 몇 개 잘라 두면 조립하는 동안 부품을 임시 고정할 때 두고두고 요긴하게 쓸 수 있습니다.
        </p>
      </aside>

      <p>앞서 SMD 커패시터를 장착하지 않았다면, 100nF 세라믹 커패시터 7개를 지금 납땜합니다.</p>

      <figure class="figure">
        <img src="{PIC}/10_solder_capacitor.webp" alt="전해 커패시터 장착" width="800" height="600" loading="lazy" />
        <figcaption>전해 커패시터 장착</figcaption>
      </figure>

      <p>
        47uF~100uF 규격의 전해 커패시터(또는 솔리드 커패시터)를 장착합니다. SMD 타입도 쓸 수 있도록 패드가 겸용으로 마련되어 있습니다.
        사진처럼 커패시터 몸통의 하얀 띠(마이너스, -극)가 보드 실크의 평평한 면을 향하도록 방향을 맞춰 장착합니다.
      </p>
      <p>이어서 USB 커넥터, 전원 잭, 리셋 버튼 스위치, 6핀 ISP 핀헤더 등을 납땜합니다.</p>

      <figure class="figure">
        <img src="{PIC}/11_make_pinheader_socket.webp" alt="핀헤더 소켓 자르기 준비" width="800" height="600" loading="lazy" />
        <figcaption>핀헤더 소켓 가공 준비</figcaption>
      </figure>

      <p>
        아두이노 실드를 꽂을 6핀과 8핀 핀헤더 소켓이 각각 2개씩 필요합니다. 긴 규격의 소켓을 구입했다면 사진처럼 자를 위치의 핀을
        니퍼나 플라이어로 뽑아낸 뒤,
      </p>

      <figure class="figure">
        <img src="{PIC}/12_make_pinheader_socket.webp" alt="핀헤더 소켓 자르기" width="800" height="600" loading="lazy" />
        <figcaption>소켓 절단</figcaption>
      </figure>

      <p>핀이 빠져나간 자리를 잘라서 사용하면 됩니다.</p>

      <figure class="figure">
        <img src="{PIC}/13_solder_pinheader_socket.webp" alt="핀헤더 소켓 납땜" width="800" height="600" loading="lazy" />
        <figcaption>핀헤더 소켓 납땜</figcaption>
      </figure>

      <p>
        아두이노 실드가 있다면 소켓 위에 꽂아두고 작업할 때 훨씬 수월합니다. (실드가 없다면 테이프로 수직을 맞춰 임시 고정합니다.)
        핀헤더의 양 끝 핀을 먼저 납땜해 위치를 잡은 뒤, 실드를 분리하고 나머지 핀들도 마저 납땜합니다.
      </p>
      <p>납땜 작업이 모두 끝났습니다. IC 소켓의 홈 방향에 맞춰 ATmega 칩을 조심스럽게 끼웁니다.</p>

      <figure class="figure">
        <img src="{PIC}/14_done.webp" alt="조립이 끝난 HUMA 보드" width="800" height="600" loading="lazy" />
        <figcaption>조립 완료</figcaption>
      </figure>

      <p>전원 선택용 점퍼(USB / 외장 전원)를 꽂아 완성을 마칩니다.</p>

      <h2 id="bootloader">부트로더 굽기</h2>
      <p>
        부트로더가 미리 구워진 ATmega 칩을 구입한 것이 아니라면, 최초 1회는 AVR ISP 프로그래머를 사용해
        아두이노 부트로더를 직접 구워주어야 합니다.
      </p>
      <p>미리 빌드된 부트로더(hex 파일)는 아두이노 IDE 설치 경로의 다음 디렉터리에 있습니다.</p>
      <ul>
        <li>ATMEGA8: <code>hardware/arduino/bootloaders/atmega8</code></li>
        <li>ATMEGA168, ATMEGA328: <code>hardware/arduino/bootloaders/atmega</code></li>
      </ul>
      <p>부트로더를 굽는 구체적인 방법은 다음 링크들을 참고하세요.</p>
      <ul>
        <li><a href="https://homin.dev/blog/p=74/">Arduino S3V3 bootloader</a></li>
        <li><a href="http://tinysun.tistory.com/8">Arduino 시작하기</a> - 작은태양님</li>
      </ul>
""",
}

# English, Japanese, Chinese translations follow - keep technical accuracy
GUIDE["en"] = {
    "title": "HUMA Assembly Guide",
    "desc": "HUMA is a solder-it-yourself Arduino-compatible board. Step-by-step from parts check through soldering and bootloader.",
    "toc": [
        ("#tools", "Tools and parts"),
        ("#solder", "Soldering"),
        ("#bootloader", "Burn the bootloader"),
    ],
    "h1": "HUMA Assembly Guide",
    "hero": """HUMA is an Arduino-compatible board based on Freeduino.
            It is designed so you can solder every part yourself, like a classic radio kit.
            Basic soldering experience is enough to finish the board.""",
    "cta_start": "Start building",
    "cta_bom": "Parts list",
    "pcb_alt": "HUMA PCB board",
    "pcb_cap": "HUMA PCB",
    "body": f"""
      <p>
        If soldering feels rusty, start with
        <a href="https://homin.dev/blog/p=460/">this Korean comic guide to soldering</a>.
      </p>
      <p>
        HUMA is open-source hardware. We take no responsibility for damage to the board
        or any personal or material harm that may occur while assembling or using it.
      </p>
      <p>
        Schematics, artwork, and related documents are licensed under
        <a href="{CC["en"]}">CC BY-SA</a>.
      </p>

      <aside class="callout callout-warn" role="note">
        <p>
          <strong>Safety</strong>
          Your safety is your responsibility. Wear eye protection and other gear while assembling,
          and watch the hot soldering iron. Work in a well-ventilated area.
        </p>
      </aside>

      <h2 id="tools">Tools and parts</h2>
      <div class="figure-pair">
        <figure class="figure">
          <img src="{PIC}/00_tools.webp" alt="Tools needed for assembly" width="640" height="480" loading="lazy" />
          <figcaption>Tools</figcaption>
        </figure>
        <figure class="figure">
          <img src="{PIC}/00_check_parts.webp" alt="Checking parts" width="640" height="480" loading="lazy" />
          <figcaption>Parts check</figcaption>
        </figure>
      </div>
      <p>
        Prepare the HUMA PCB and every item on the <a href="bom.html">parts list</a>.
      </p>

      <h2 id="solder">Soldering</h2>
      <p>
        Solder from lowest parts to tallest, from the center of the board outward,
        and from heat-tolerant parts to heat-sensitive ones.
      </p>
      <p>
        Start with the lowest 3.3V SMD capacitor. The plus (+) side is marked with a stripe.
      </p>

      <figure class="figure">
        <img src="{PIC}/01_solder_smd_cap.webp" alt="Placing the SMD capacitor" width="800" height="600" loading="lazy" />
        <figcaption>Place the SMD capacitor</figcaption>
      </figure>

      <p>Align the stripe toward the 2.2u marking, tack one pad first, then finish the other.</p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>Note</strong>
          The silk says 2.2u, but a 10uF capacitor was used in practice.
        </p>
      </aside>

      <figure class="figure">
        <img src="{PIC}/02_solder_smd_cap.webp" alt="Soldering the other SMD capacitor pad" width="800" height="600" loading="lazy" />
        <figcaption>Finish the other pad</figcaption>
      </figure>

      <p>
        Then bridge the solder jumper next to the capacitor to connect USB and 3V3.
        That routes the FT232BL USB-serial chip's 3.3V onto the board rail.
      </p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>Note</strong>
          If you need more 3.3V current, fit MIC5219 and a 470pF capacitor on the back of the board
          and bridge the LDO-to-3V3 solder jumper instead, so 3.3V is derived from the 5V rail.
        </p>
      </aside>

      <p>
        Next solder the USB-serial chip FT232BL (or FT232BM). If you are new to SMD ICs, see
        <a href="https://homin.dev/blog/p=481/">this SMD soldering guide</a> (Korean).
      </p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>Note</strong>
          Check every SMD pin under magnification for opens and shorts.
          Fixes get much harder after the rest of the board is populated.
        </p>
      </aside>

      <p>
        Seven 100nF capacitors are used. Pads accept either SMD 1608 or disc ceramic parts.
        If you chose SMD, solder them now. 100nF caps are non-polar.
      </p>
      <p>The hardest SMD work on this board is done.</p>

      <figure class="figure">
        <img src="{PIC}/03_solder_lead_parts.webp" alt="Starting through-hole soldering" width="800" height="600" loading="lazy" />
        <figcaption>Through-hole parts</figcaption>
      </figure>

      <p>
        Install resistors to the values marked on the board. Use ordinary 1/4W or 1/8W 5% resistors.
        1% parts cost more without benefit in this digital circuit. 1/2W parts are bulkier and harder to fit.
      </p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>Note</strong>
          The three resistors marked <code>*470</code> are LED current limiters. Any value from 330Ω to 1kΩ is fine
          (680Ω was used in the example build).
        </p>
      </aside>

      <figure class="figure">
        <img src="{PIC}/04_solder_lead_parts.webp" alt="Diode and bead installed" width="800" height="600" loading="lazy" />
        <figcaption>Diode and bead</figcaption>
      </figure>

      <p>
        Solder the diode by the power jack and the ferrite bead under the USB connector.
        Instead of the bead you may fit a resettable fuse in the PTC0805 footprint, as on official Arduino boards.
        Choose one of the two.
      </p>

      <figure class="figure">
        <img src="{PIC}/05_solder_7805.webp" alt="Placing the 7805 regulator" width="800" height="600" loading="lazy" />
        <figcaption>Place the 7805</figcaption>
      </figure>

      <p>Flip the board and solder the 7805. Tack one lead first to hold position,</p>

      <figure class="figure">
        <img src="{PIC}/06_solder_7805.webp" alt="Finishing 7805 pads" width="800" height="600" loading="lazy" />
        <figcaption>7805 done</figcaption>
      </figure>

      <p>then solder the remaining pads once it sits flat.</p>

      <figure class="figure">
        <img src="{PIC}/07_solder_crystal.webp" alt="Resonator and crystal" width="800" height="600" loading="lazy" />
        <figcaption>Resonator and crystal</figcaption>
      </figure>

      <p>Solder the resonator (blue) and the crystal (silver).</p>

      <figure class="figure">
        <img src="{PIC}/08_solder_led.webp" alt="Three LEDs installed" width="800" height="600" loading="lazy" />
        <figcaption>LEDs</figcaption>
      </figure>

      <p>
        Fit three 3mm LEDs. Observe polarity: the short lead (or flat edge) faces the silk labels (R/T, L, PWR).
      </p>

      <figure class="figure">
        <img src="{PIC}/09_solder_ic_socket.webp" alt="IC socket installed" width="800" height="600" loading="lazy" />
        <figcaption>IC socket</figcaption>
      </figure>

      <p>
        Install the ATmega IC socket. The photos use a cut-to-length socket, taped and braced with pin-header sockets before soldering.
      </p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>Note</strong>
          Masking tape leaves little residue if removed soon. Keep a few 3cm strips handy to hold parts while soldering.
        </p>
      </aside>

      <p>If you skipped the SMD 100nF caps earlier, solder seven ceramic 100nF caps now.</p>

      <figure class="figure">
        <img src="{PIC}/10_solder_capacitor.webp" alt="Electrolytic capacitors" width="800" height="600" loading="lazy" />
        <figcaption>Electrolytic capacitors</figcaption>
      </figure>

      <p>
        Fit 47uF-100uF electrolytics (or solid caps). SMD footprints are also provided.
        Orient the white stripe (-) toward the flat side of the silk outline.
      </p>
      <p>Then solder the USB connector, power jack, reset switch, and ISP pin header.</p>

      <figure class="figure">
        <img src="{PIC}/11_make_pinheader_socket.webp" alt="Preparing pin-header sockets" width="800" height="600" loading="lazy" />
        <figcaption>Prepare pin-header sockets</figcaption>
      </figure>

      <p>
        You need two 6-pin and two 8-pin female headers for shields. If you bought long strips, pull the pin at the cut point with pliers,
      </p>

      <figure class="figure">
        <img src="{PIC}/12_make_pinheader_socket.webp" alt="Cutting pin-header sockets" width="800" height="600" loading="lazy" />
        <figcaption>Cut the sockets</figcaption>
      </figure>

      <p>then cut the plastic at that gap.</p>

      <figure class="figure">
        <img src="{PIC}/13_solder_pinheader_socket.webp" alt="Soldering pin-header sockets" width="800" height="600" loading="lazy" />
        <figcaption>Solder the sockets</figcaption>
      </figure>

      <p>
        An Arduino shield plugged into the sockets keeps them square while soldering. Without one, tape them vertical.
        Tack the end pins first, remove the shield, then finish the rest.
      </p>
      <p>Soldering is done. Insert the ATmega into the socket, matching the notch.</p>

      <figure class="figure">
        <img src="{PIC}/14_done.webp" alt="Finished HUMA board" width="800" height="600" loading="lazy" />
        <figcaption>Complete</figcaption>
      </figure>

      <p>Fit the power-select jumper (USB / external) to finish.</p>

      <h2 id="bootloader">Burn the bootloader</h2>
      <p>
        If your ATmega did not come with an Arduino bootloader, burn one once with an AVR ISP programmer.
      </p>
      <p>Prebuilt bootloader hex files ship with the Arduino IDE here:</p>
      <ul>
        <li>ATMEGA8: <code>hardware/arduino/bootloaders/atmega8</code></li>
        <li>ATMEGA168, ATMEGA328: <code>hardware/arduino/bootloaders/atmega</code></li>
      </ul>
      <p>See also:</p>
      <ul>
        <li><a href="https://homin.dev/blog/p=74/">Arduino S3V3 bootloader</a></li>
        <li><a href="http://tinysun.tistory.com/8">Getting started with Arduino</a> (Korean)</li>
      </ul>
""",
}

GUIDE["ja"] = {
    "title": "HUMA 組み立てガイド",
    "desc": "HUMAは自分ではんだ付けして組み立てるArduino互換ボードです。部品確認からはんだ付け、ブートローダ書き込みまで手順で案内します。",
    "toc": [
        ("#tools", "工具と部品"),
        ("#solder", "はんだ付け"),
        ("#bootloader", "ブートローダ書き込み"),
    ],
    "h1": "HUMA 組み立てガイド",
    "hero": """HUMAは
            FreeduinoベースのArduino互換ボードです。
            昔のラジオキットのように、部品を自分ではんだ付けして組み立てられるよう設計されています。
            基本的なはんだ付け経験があれば完成できます。""",
    "cta_start": "組み立て開始",
    "cta_bom": "部品一覧",
    "pcb_alt": "HUMA PCBボード",
    "pcb_cap": "HUMA PCB",
    "body": f"""
      <p>
        はんだ付けに久しぶりなら、まず
        <a href="https://homin.dev/blog/p=460/">マンガではんだ付けを学ぶ</a>（韓国語）を参照してください。
      </p>
      <p>
        HUMAはオープンソースハードウェアです。組み立てや使用中のボード損傷、人身・物的損害について
        一切の責任を負いません。
      </p>
      <p>
        回路図・アートワーク・関連文書は
        <a href="{CC["ja"]}">CC BY-SA</a>
        ライセンスです。
      </p>

      <aside class="callout callout-warn" role="note">
        <p>
          <strong>安全上の注意</strong>
          作業者自身の安全は自分で守ってください。保護メガネなどを着用し、熱いこてによるやけどに注意し、
          換気の良い場所で作業してください。
        </p>
      </aside>

      <h2 id="tools">工具と部品</h2>
      <div class="figure-pair">
        <figure class="figure">
          <img src="{PIC}/00_tools.webp" alt="組み立てに必要な工具" width="640" height="480" loading="lazy" />
          <figcaption>工具</figcaption>
        </figure>
        <figure class="figure">
          <img src="{PIC}/00_check_parts.webp" alt="部品の確認" width="640" height="480" loading="lazy" />
          <figcaption>部品確認</figcaption>
        </figure>
      </div>
      <p>
        HUMA PCBと<a href="bom.html">部品一覧</a>を照合し、必要な部品が揃っているか確認します。
      </p>

      <h2 id="solder">はんだ付け</h2>
      <p>
        背の低い部品から高い部品へ、基板の内側から外側へ、熱に強い部品から弱い部品の順ではんだ付けします。
      </p>
      <p>
        まず最も低い3.3V電源用SMDコンデンサから。プラス(+)側に帯表示があります。
      </p>

      <figure class="figure">
        <img src="{PIC}/01_solder_smd_cap.webp" alt="SMDコンデンサの位置合わせ" width="800" height="600" loading="lazy" />
        <figcaption>SMDコンデンサの配置</figcaption>
      </figure>

      <p>2.2u表記の向きに帯を合わせ、片側を仮付けしてから反対側を仕上げます。</p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>参考</strong>
          シルクは2.2uですが、実機では10uFコンデンサを使用しました。
        </p>
      </aside>

      <figure class="figure">
        <img src="{PIC}/02_solder_smd_cap.webp" alt="SMDコンデンサの反対側" width="800" height="600" loading="lazy" />
        <figcaption>反対側のパッド</figcaption>
      </figure>

      <p>
        続けて隣のソルダージャンパでUSBと3V3を接続します。これでFT232BLが供給する3.3Vをボード電源に使います。
      </p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>参考</strong>
          3.3Vでより大きな電流が必要なら、裏面にMIC5219と470pFを実装し、LDOと3V3のジャンパを接続して
          5Vから変換した3.3Vを使ってください。
        </p>
      </aside>

      <p>
        次にUSB-シリアル変換チップFT232BL（またはFT232BM）をはんだ付けします。SMD ICが初めてなら
        <a href="https://homin.dev/blog/p=481/">SMDはんだ付けガイド</a>（韓国語）を参照してください。
      </p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>参考</strong>
          拡大鏡でショートや浮きがないか確認します。他部品を実装したあとの修正は非常に困難です。
        </p>
      </aside>

      <p>
        100nFは7個です。SMD 1608またはディスクセラミック両対応パッドがあります。SMDを選んだら今はんだ付けします。極性はありません。
      </p>
      <p>このボードで最も難しいSMD作業はここまでです。</p>

      <figure class="figure">
        <img src="{PIC}/03_solder_lead_parts.webp" alt="リード部品のはんだ付け" width="800" height="600" loading="lazy" />
        <figcaption>リード部品</figcaption>
      </figure>

      <p>
        基板表記どおりに抵抗を実装します。1/4Wまたは1/8Wの5%抵抗で十分です。1%は高価でも利点は少なく、1/2Wは大きくて取り付けにくいです。
      </p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>参考</strong>
          <code>*470</code>の抵抗3本はLED用です。330Ω〜1kΩなら470Ωでなくても構いません（作例では680Ω）。
        </p>
      </aside>

      <figure class="figure">
        <img src="{PIC}/04_solder_lead_parts.webp" alt="ダイオードとビーズ" width="800" height="600" loading="lazy" />
        <figcaption>ダイオードとビーズ</figcaption>
      </figure>

      <p>
        電源ジャック横のダイオードとUSB下のフェライトビーズを実装します。ビーズの代わりにPTC0805位置へリセッタブルヒューズでも可。どちらか一方を選んでください。
      </p>

      <figure class="figure">
        <img src="{PIC}/05_solder_7805.webp" alt="7805の配置" width="800" height="600" loading="lazy" />
        <figcaption>7805の仮付け</figcaption>
      </figure>

      <p>裏返して7805を実装します。まず片脚を仮付けし、</p>

      <figure class="figure">
        <img src="{PIC}/06_solder_7805.webp" alt="7805の仕上げ" width="800" height="600" loading="lazy" />
        <figcaption>7805完了</figcaption>
      </figure>

      <p>位置が決まってから残りをはんだ付けします。</p>

      <figure class="figure">
        <img src="{PIC}/07_solder_crystal.webp" alt="レゾネータとクリスタル" width="800" height="600" loading="lazy" />
        <figcaption>レゾネータとクリスタル</figcaption>
      </figure>

      <p>レゾネータ（青）とクリスタル（銀）を実装します。</p>

      <figure class="figure">
        <img src="{PIC}/08_solder_led.webp" alt="LED 3個" width="800" height="600" loading="lazy" />
        <figcaption>LED</figcaption>
      </figure>

      <p>
        3mm LEDを3個。極性に注意し、短い脚（または平坦面）をシルク表記（R/T, L, PWR）側へ向けます。
      </p>

      <figure class="figure">
        <img src="{PIC}/09_solder_ic_socket.webp" alt="ICソケット" width="800" height="600" loading="lazy" />
        <figcaption>ICソケット</figcaption>
      </figure>

      <p>
        ATmega用ICソケットを実装します。写真では必要な長さに切ったソケットをテープとピンヘッダで仮固定してはんだ付けしています。
      </p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>参考</strong>
          マスキングテープは早めに剥がせば糊が残りにくいです。3cm程度切っておくと部品の仮固定に便利です。
        </p>
      </aside>

      <p>SMDの100nFをまだ付けていなければ、セラミック100nFを7個今実装します。</p>

      <figure class="figure">
        <img src="{PIC}/10_solder_capacitor.webp" alt="電解コンデンサ" width="800" height="600" loading="lazy" />
        <figcaption>電解コンデンサ</figcaption>
      </figure>

      <p>
        47uF〜100uFの電解（または固体）コンデンサを実装します。SMD用パッドもあります。
        白い帯（−）をシルクの平らな側へ向けます。
      </p>
      <p>続いてUSBコネクタ、電源ジャック、リセットスイッチ、ISPピンヘッダなどを実装します。</p>

      <figure class="figure">
        <img src="{PIC}/11_make_pinheader_socket.webp" alt="ピンヘッダソケットの加工" width="800" height="600" loading="lazy" />
        <figcaption>ソケット加工の準備</figcaption>
      </figure>

      <p>
        6ピンと8ピンのメスヘッダが各2本必要です。長いソケットなら切る位置のピンを引き抜いてから、
      </p>

      <figure class="figure">
        <img src="{PIC}/12_make_pinheader_socket.webp" alt="ソケット切断" width="800" height="600" loading="lazy" />
        <figcaption>ソケット切断</figcaption>
      </figure>

      <p>その隙間で切断して使います。</p>

      <figure class="figure">
        <img src="{PIC}/13_solder_pinheader_socket.webp" alt="ピンヘッダソケットのはんだ付け" width="800" height="600" loading="lazy" />
        <figcaption>ソケットのはんだ付け</figcaption>
      </figure>

      <p>
        シールドがあれば上に挿して垂直を保ちやすいです（なければテープで仮固定）。両端を仮付けし、シールドを外して残りを仕上げます。
      </p>
      <p>はんだ付け完了です。ノッチ向きに合わせてATmegaをソケットへ挿入します。</p>

      <figure class="figure">
        <img src="{PIC}/14_done.webp" alt="完成したHUMAボード" width="800" height="600" loading="lazy" />
        <figcaption>完成</figcaption>
      </figure>

      <p>電源選択ジャンパ（USB / 外部電源）を挿して完成です。</p>

      <h2 id="bootloader">ブートローダ書き込み</h2>
      <p>
        ブートローダ入りATmegaを買っていない場合、最初の1回はAVR ISPでArduinoブートローダを書き込みます。
      </p>
      <p>ビルド済みhexはArduino IDEの次の場所にあります。</p>
      <ul>
        <li>ATMEGA8: <code>hardware/arduino/bootloaders/atmega8</code></li>
        <li>ATMEGA168, ATMEGA328: <code>hardware/arduino/bootloaders/atmega</code></li>
      </ul>
      <p>手順の参考:</p>
      <ul>
        <li><a href="https://homin.dev/blog/p=74/">Arduino S3V3 bootloader</a></li>
        <li><a href="http://tinysun.tistory.com/8">Arduinoをはじめよう</a>（韓国語）</li>
      </ul>
""",
}

GUIDE["zh"] = {
    "title": "HUMA 组装说明",
    "desc": "HUMA 是可自行焊接组装的 Arduino 兼容板。从零件核对、焊接到烧录引导程序逐步说明。",
    "toc": [
        ("#tools", "工具与零件"),
        ("#solder", "焊接"),
        ("#bootloader", "烧录引导程序"),
    ],
    "h1": "HUMA 组装说明",
    "hero": """HUMA 是基于
            Freeduino 的 Arduino 兼容开发板。
            设计上可像早期收音机套件一样，亲手焊接全部零件完成组装。
            具备基础焊接经验即可完成。""",
    "cta_start": "开始组装",
    "cta_bom": "零件清单",
    "pcb_alt": "HUMA PCB 电路板",
    "pcb_cap": "HUMA PCB",
    "body": f"""
      <p>
        若久未焊接，可先阅读
        <a href="https://homin.dev/blog/p=460/">漫画学焊接</a>（韩文）。
      </p>
      <p>
        HUMA 为开源硬件。对组装或使用过程中造成的板卡损坏以及人身、财产损失不承担任何责任。
      </p>
      <p>
        原理图、工艺图及相关文档采用
        <a href="{CC["zh"]}">CC BY-SA</a>
        许可。
      </p>

      <aside class="callout callout-warn" role="note">
        <p>
          <strong>安全提示</strong>
          请自行注意安全。组装时佩戴护目镜等防护用具，谨防烙铁烫伤，并在通风良好处操作。
        </p>
      </aside>

      <h2 id="tools">工具与零件</h2>
      <div class="figure-pair">
        <figure class="figure">
          <img src="{PIC}/00_tools.webp" alt="组装所需工具" width="640" height="480" loading="lazy" />
          <figcaption>工具</figcaption>
        </figure>
        <figure class="figure">
          <img src="{PIC}/00_check_parts.webp" alt="核对零件" width="640" height="480" loading="lazy" />
          <figcaption>零件核对</figcaption>
        </figure>
      </div>
      <p>
        对照 HUMA PCB 与<a href="bom.html">零件清单</a>，确认零件齐全。
      </p>

      <h2 id="solder">焊接</h2>
      <p>
        原则：由矮到高、由板内到板外、由耐热到不耐热依次焊接。
      </p>
      <p>
        先焊最矮的 3.3V SMD 电容。正极(+)一侧有色带标记。
      </p>

      <figure class="figure">
        <img src="{PIC}/01_solder_smd_cap.webp" alt="放置 SMD 电容" width="800" height="600" loading="lazy" />
        <figcaption>放置 SMD 电容</figcaption>
      </figure>

      <p>使色带朝向 2.2u 丝印方向，先焊一侧定位，再完成另一侧。</p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>说明</strong>
          丝印为 2.2u，实际使用了 10uF 电容。
        </p>
      </aside>

      <figure class="figure">
        <img src="{PIC}/02_solder_smd_cap.webp" alt="焊接另一侧焊盘" width="800" height="600" loading="lazy" />
        <figcaption>完成另一侧</figcaption>
      </figure>

      <p>
        再在电容旁的焊桥上上锡，连接 USB 与 3V3，即可使用 FT232BL 提供的 3.3V。
      </p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>说明</strong>
          若 3.3V 需要更大电流，可在板背面安装 MIC5219 与 470pF，并将 LDO 与 3V3 焊桥连通，由 5V 转换供电。
        </p>
      </aside>

      <p>
        接着焊接 USB 转串口芯片 FT232BL（或 FT232BM）。若不熟悉 SMD IC，请先参考
        <a href="https://homin.dev/blog/p=481/">SMD 焊接指南</a>（韩文）。
      </p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>说明</strong>
          用放大镜仔细检查引脚是否虚焊或短路。其余零件装完后再返修会非常困难。
        </p>
      </aside>

      <p>
        板上共需 7 只 100nF。焊盘兼容 SMD 1608 与圆片陶瓷电容。若选用 SMD，现在焊接。100nF 无极性。
      </p>
      <p>至此，本板上最难的 SMD 工序已完成。</p>

      <figure class="figure">
        <img src="{PIC}/03_solder_lead_parts.webp" alt="开始焊接插件" width="800" height="600" loading="lazy" />
        <figcaption>插件焊接</figcaption>
      </figure>

      <p>
        按板上阻值安装电阻。使用 1/4W 或 1/8W、5% 普通电阻即可。1% 更贵但对数字电路帮助不大；1/2W 体积大更难装。
      </p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>说明</strong>
          标有 <code>*470</code> 的三只电阻为 LED 限流电阻，330Ω~1kΩ 均可（示例使用 680Ω）。
        </p>
      </aside>

      <figure class="figure">
        <img src="{PIC}/04_solder_lead_parts.webp" alt="二极管与磁珠" width="800" height="600" loading="lazy" />
        <figcaption>二极管与磁珠</figcaption>
      </figure>

      <p>
        焊接电源座旁的二极管与 USB 下方的磁珠。也可像原版 Arduino 一样在 PTC0805 位置装自恢复保险丝。二者择一。
      </p>

      <figure class="figure">
        <img src="{PIC}/05_solder_7805.webp" alt="放置 7805" width="800" height="600" loading="lazy" />
        <figcaption>放置 7805</figcaption>
      </figure>

      <p>翻面焊接 7805。先点焊一只脚定位，</p>

      <figure class="figure">
        <img src="{PIC}/06_solder_7805.webp" alt="完成 7805" width="800" height="600" loading="lazy" />
        <figcaption>7805 完成</figcaption>
      </figure>

      <p>摆正后再焊其余焊盘。</p>

      <figure class="figure">
        <img src="{PIC}/07_solder_crystal.webp" alt="谐振器与晶振" width="800" height="600" loading="lazy" />
        <figcaption>谐振器与晶振</figcaption>
      </figure>

      <p>焊接谐振器（蓝色）与晶振（银色）。</p>

      <figure class="figure">
        <img src="{PIC}/08_solder_led.webp" alt="三只 LED" width="800" height="600" loading="lazy" />
        <figcaption>LED</figcaption>
      </figure>

      <p>
        安装三只 3mm LED。注意极性：短脚（或削平面）朝向丝印文字（R/T、L、PWR）一侧。
      </p>

      <figure class="figure">
        <img src="{PIC}/09_solder_ic_socket.webp" alt="IC 座" width="800" height="600" loading="lazy" />
        <figcaption>IC 座</figcaption>
      </figure>

      <p>
        安装 ATmega IC 座。图中使用可裁切插座，并用胶带与排母临时固定后再焊接。
      </p>

      <aside class="callout callout-note" role="note">
        <p>
          <strong>说明</strong>
          美纹纸胶带若尽快撕下通常不留残胶。剪几段约 3cm 的胶带，组装时临时固定零件很方便。
        </p>
      </aside>

      <p>若尚未安装 SMD 100nF，现在焊接 7 只陶瓷 100nF。</p>

      <figure class="figure">
        <img src="{PIC}/10_solder_capacitor.webp" alt="电解电容" width="800" height="600" loading="lazy" />
        <figcaption>电解电容</figcaption>
      </figure>

      <p>
        安装 47uF~100uF 电解（或固态）电容。亦提供 SMD 焊盘。白色色带（负极）朝向丝印平坦一侧。
      </p>
      <p>接着焊接 USB 座、电源座、复位键、ISP 排针等。</p>

      <figure class="figure">
        <img src="{PIC}/11_make_pinheader_socket.webp" alt="准备排母" width="800" height="600" loading="lazy" />
        <figcaption>加工排母</figcaption>
      </figure>

      <p>
        需要 6 针与 8 针排母各两根。若买的是长条，先拔出裁切处的针脚，
      </p>

      <figure class="figure">
        <img src="{PIC}/12_make_pinheader_socket.webp" alt="切断排母" width="800" height="600" loading="lazy" />
        <figcaption>切断排母</figcaption>
      </figure>

      <p>再在缺口处切断使用。</p>

      <figure class="figure">
        <img src="{PIC}/13_solder_pinheader_socket.webp" alt="焊接排母" width="800" height="600" loading="lazy" />
        <figcaption>焊接排母</figcaption>
      </figure>

      <p>
        有扩展板时可先插上以保持垂直（否则用胶带固定）。先焊两端定位，取下扩展板后再焊其余针脚。
      </p>
      <p>焊接全部完成。按缺口方向将 ATmega 插入 IC 座。</p>

      <figure class="figure">
        <img src="{PIC}/14_done.webp" alt="组装完成的 HUMA" width="800" height="600" loading="lazy" />
        <figcaption>完成</figcaption>
      </figure>

      <p>插上电源选择跳线（USB / 外部电源）即告完成。</p>

      <h2 id="bootloader">烧录引导程序</h2>
      <p>
        若芯片未预烧 Arduino 引导程序，需用 AVR ISP 首次烧录一次。
      </p>
      <p>预编译 hex 位于 Arduino IDE 安装目录：</p>
      <ul>
        <li>ATMEGA8: <code>hardware/arduino/bootloaders/atmega8</code></li>
        <li>ATMEGA168, ATMEGA328: <code>hardware/arduino/bootloaders/atmega</code></li>
      </ul>
      <p>参考：</p>
      <ul>
        <li><a href="https://homin.dev/blog/p=74/">Arduino S3V3 bootloader</a></li>
        <li><a href="http://tinysun.tistory.com/8">Arduino 入门</a>（韩文）</li>
      </ul>
""",
}

# BOM rows: NAME, VALUE, EA are shared; DESC per language
BOM_ROWS = [
    ("LDO", "7805DT", "1", {
        "ko": "5V 레귤레이터",
        "en": "5V regulator",
        "ja": "5Vレギュレータ",
        "zh": "5V 稳压器",
    }),
    ("USB2SERIAL IC", "FT232BM", "1", {
        "ko": "FT232BL로 대체 가능",
        "en": "FT232BL also OK",
        "ja": "FT232BLでも可",
        "zh": "可用 FT232BL 替代",
    }),
    ("DIODE", "1N4004", "1", {"ko": "", "en": "", "ja": "", "zh": ""}),
    ("PWR-JACK", "", "1", {
        "ko": "DC 전원 잭",
        "en": "DC power jack",
        "ja": "DC電源ジャック",
        "zh": "DC 电源座",
    }),
    ("USB CONNECT", "", "1", {
        "ko": "USB Type-B 커넥터",
        "en": "USB Type-B connector",
        "ja": "USB Type-Bコネクタ",
        "zh": "USB Type-B 接口",
    }),
    ("PINHEADER", "1X3", "1", {
        "ko": "전원 선택 점퍼",
        "en": "Power select jumper",
        "ja": "電源選択ジャンパ",
        "zh": "电源选择跳线",
    }),
    ("PINHEADER", "2x3", "1", {
        "ko": "AVR ISP 6핀",
        "en": "AVR ISP 6-pin",
        "ja": "AVR ISP 6ピン",
        "zh": "AVR ISP 6 针",
    }),
    ("PUSHBUTTON", "", "1", {
        "ko": "리셋 버튼 스위치",
        "en": "Reset switch",
        "ja": "リセットスイッチ",
        "zh": "复位按键",
    }),
    ("RESISTOR", "10k", "1", {
        "ko": "리셋 풀업 저항",
        "en": "Reset pull-up",
        "ja": "リセットプルアップ",
        "zh": "复位上拉电阻",
    }),
    ("RESISTOR", "470", "4", {
        "ko": "<code>*</code> 표시 저항 3개는 330Ω~1kΩ 사이 값으로 대체 가능",
        "en": "Three marked <code>*</code> may be 330Ω-1kΩ",
        "ja": "<code>*</code>の3本は330Ω〜1kΩで代替可",
        "zh": "标 <code>*</code> 的三只可用 330Ω~1kΩ 替代",
    }),
    ("RESISTOR", "27", "2", {
        "ko": "USB 신호선 저항",
        "en": "USB signal series",
        "ja": "USB信号線抵抗",
        "zh": "USB 信号电阻",
    }),
    ("RESISTOR", "1k5", "1", {
        "ko": "USB 풀업 저항",
        "en": "USB pull-up",
        "ja": "USBプルアップ",
        "zh": "USB 上拉电阻",
    }),
    ("RESISTOR", "1k", "2", {"ko": "", "en": "", "ja": "", "zh": ""}),
    ("FUSE", "PTC1812", "1", {
        "ko": "복구형 퓨즈 (또는 비드 대체)",
        "en": "Resettable fuse (or use bead)",
        "ja": "リセッタブルヒューズ（またはビーズ）",
        "zh": "自恢复保险丝（或用磁珠）",
    }),
    ("LED", "3mm", "3", {
        "ko": "보드 표기 방향으로 짧은 다리(-)가 오도록 장착",
        "en": "Short lead (-) toward silk labels",
        "ja": "短い脚(-)をシルク表記側へ",
        "zh": "短脚(-)朝向丝印文字一侧",
    }),
    ("RESONATOR", "6MHz", "1", {"ko": "", "en": "", "ja": "", "zh": ""}),
    ("CRYSTAL", "16MHz", "1", {"ko": "", "en": "", "ja": "", "zh": ""}),
    ("CAPACITOR", "22pF", "2", {"ko": "", "en": "", "ja": "", "zh": ""}),
    ("CAPACITOR", "100nF", "7", {
        "ko": "SMD 1608 또는 디스크 세라믹 겸용",
        "en": "SMD 1608 or disc ceramic",
        "ja": "SMD 1608またはディスクセラミック",
        "zh": "SMD 1608 或圆片陶瓷",
    }),
    ("CAPACITOR", "47uF", "2", {
        "ko": "전해 커패시터",
        "en": "Electrolytic",
        "ja": "電解コンデンサ",
        "zh": "电解电容",
    }),
    ("CAPACITOR", "10uF", "1", {
        "ko": "<strong>PCB 실크에는 2.2uF으로 표기 (10uF 사용)</strong>",
        "en": "<strong>Silk says 2.2uF; use 10uF</strong>",
        "ja": "<strong>シルクは2.2uF表記（10uF使用）</strong>",
        "zh": "<strong>丝印为 2.2uF，实际用 10uF</strong>",
    }),
    ("MCU", "ATMEGA8", "1", {
        "ko": "ATmega168 / ATmega328 호환 가능",
        "en": "ATmega168 / ATmega328 also OK",
        "ja": "ATmega168 / ATmega328も可",
        "zh": "亦可用 ATmega168 / ATmega328",
    }),
    ("IC SOCKET", "28pin", "1", {
        "ko": "ATmega용 DIP 소켓",
        "en": "DIP socket for ATmega",
        "ja": "ATmega用DIPソケット",
        "zh": "ATmega DIP 座",
    }),
]

BOM_META = {
    "ko": {
        "title": "HUMA 부품 목록",
        "desc": "Freeduino HUMA 보드 조립에 필요한 부품 목록입니다.",
        "h1": "부품 목록",
        "intro": "Freeduino 기반 HUMA 보드를 조립할 때 필요한 부품 목록입니다.",
        "cta": "조립 설명서",
        "th": ("NAME", "VALUE", "EA", "DESC"),
    },
    "en": {
        "title": "HUMA Parts List",
        "desc": "Parts required to assemble the Freeduino-based HUMA board.",
        "h1": "Parts list",
        "intro": "Parts required to assemble the Freeduino-based HUMA board.",
        "cta": "Assembly guide",
        "th": ("NAME", "VALUE", "EA", "DESC"),
    },
    "ja": {
        "title": "HUMA 部品一覧",
        "desc": "FreeduinoベースのHUMAボード組み立てに必要な部品一覧です。",
        "h1": "部品一覧",
        "intro": "FreeduinoベースのHUMAボード組み立てに必要な部品一覧です。",
        "cta": "組み立てガイド",
        "th": ("NAME", "VALUE", "EA", "DESC"),
    },
    "zh": {
        "title": "HUMA 零件清单",
        "desc": "组装基于 Freeduino 的 HUMA 板所需零件清单。",
        "h1": "零件清单",
        "intro": "组装基于 Freeduino 的 HUMA 板所需零件清单。",
        "cta": "组装说明",
        "th": ("NAME", "VALUE", "EA", "DESC"),
    },
}


def build_assets() -> None:
    src_path = ROOT / "pics" / "14_done.webp"
    if not src_path.exists():
        return
    try:
        from PIL import Image, ImageDraw, ImageFilter, ImageFont
    except ImportError:
        print("PIL not installed, skipping asset generation")
        return

    src = Image.open(src_path).convert("RGBA")

    def get_font(font_type, size, bold=False):
        candidates = []
        if font_type == "korean":
            candidates = [
                ("/System/Library/Fonts/AppleSDGothicNeo.ttc", 4 if bold else 2),
                ("/Library/Fonts/Arial Unicode.ttf", 0),
                ("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 0),
                ("/usr/share/fonts/truetype/nanum/NanumGothic.ttf", 0),
            ]
        elif font_type == "latin":
            candidates = [
                ("/System/Library/Fonts/Helvetica.ttc", 1 if bold else 0),
                ("/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf", 0),
                ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 0),
            ]
        for path, idx in candidates:
            if os.path.exists(path):
                try:
                    return ImageFont.truetype(path, size, index=idx)
                except Exception:
                    pass
        return ImageFont.load_default()

    # 1. OG Image (1200x630)
    W, H = 1200, 630
    font_huge = get_font("latin", 84, bold=True)
    font_sub = get_font("korean", 32, bold=True)
    font_desc = get_font("latin", 24, bold=False)
    font_badge = get_font("korean", 18, bold=True)
    font_tag = get_font("korean", 17, bold=True)

    im = Image.new("RGBA", (W, H), (244, 246, 248, 255))
    draw = ImageDraw.Draw(im)
    for y in range(H):
        ratio = y / H
        r = int(248 - ratio * 8)
        g = int(250 - ratio * 8)
        b = int(252 - ratio * 8)
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

    # Top accent bar
    draw.rectangle([0, 0, W, 8], fill=(196, 92, 38, 255))

    # Pill badge
    bx, by = 80, 75
    draw.rounded_rectangle([bx, by, bx + 270, by + 36], radius=18, fill=(255, 243, 234, 255), outline=(196, 92, 38, 160), width=1)
    draw.text((bx + 16, by + 8), "HUman MAdeable Arduino", font=font_badge, fill=(154, 63, 18, 255))

    # Title & descriptions
    draw.text((80, 135), "HUMA", font=font_huge, fill=(26, 35, 50, 255))
    draw.text((80, 250), "라디오 키트처럼 직접 납땜하여 완성하는\n오픈소스 아두이노 호환 보드", font=font_sub, fill=(30, 41, 59, 255), spacing=10)
    draw.text((80, 360), "Hand-solderable Arduino-compatible\nFreeduino-based DIY maker kit", font=font_desc, fill=(100, 116, 139, 255), spacing=6)

    # Tags
    tags = ["Through-Hole DIY", "ATmega8 / 328P", "Freeduino"]
    tx = 80
    for t in tags:
        tb = font_tag.getbbox(t)
        tw = tb[2] - tb[0] + 24
        draw.rounded_rectangle([tx, 475, tx + tw, 475 + 36], radius=8, fill=(255, 255, 255, 255), outline=(203, 213, 225, 255), width=1)
        draw.text((tx + 12, 475 + 8), t, font=font_tag, fill=(71, 85, 105, 255))
        tx += tw + 12

    # Card on right
    card_w = 540
    card_h = int(card_w * src.height / src.width)
    board = src.resize((card_w, card_h), Image.Resampling.LANCZOS)
    card_x = 590
    card_y = (H - card_h) // 2 + 10

    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.rounded_rectangle([card_x - 6, card_y + 12, card_x + card_w + 6, card_y + card_h + 26], radius=24, fill=(15, 23, 42, 60))
    shadow = shadow.filter(ImageFilter.GaussianBlur(28))
    im = Image.alpha_composite(im, shadow)

    mask = Image.new("L", (card_w, card_h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, card_w, card_h], radius=16, fill=255)
    im.paste(board, (card_x, card_y), mask)

    final_draw = ImageDraw.Draw(im)
    final_draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=16, outline=(255, 255, 255, 255), width=2)

    im.convert("RGB").save(ROOT / "og-image.png", format="PNG", optimize=True)
    print("wrote", ROOT / "og-image.png")

    # 2. Favicons
    crop = src.crop((140, 20, 500, 380))
    ati = crop.resize((180, 180), Image.Resampling.LANCZOS).convert("RGB")
    ati.save(ROOT / "apple-touch-icon.png", format="PNG", optimize=True)
    print("wrote", ROOT / "apple-touch-icon.png")

    def make_rounded(size, radius):
        im_r = crop.resize((size, size), Image.Resampling.LANCZOS).convert("RGBA")
        scale = 4
        m = Image.new("L", (size * scale, size * scale), 0)
        md = ImageDraw.Draw(m)
        md.rounded_rectangle([0, 0, size * scale - 1, size * scale - 1], radius=radius * scale, fill=255)
        m = m.resize((size, size), Image.Resampling.LANCZOS)
        im_r.putalpha(m)
        return im_r

    fav_48 = make_rounded(48, 8)
    fav_32 = make_rounded(32, 6)
    fav_16 = make_rounded(16, 3)

    fav_32.save(ROOT / "favicon-32x32.png", format="PNG", optimize=True)
    fav_32.save(ROOT / "favicon.png", format="PNG", optimize=True)
    fav_16.save(ROOT / "favicon-16x16.png", format="PNG", optimize=True)
    fav_48.save(ROOT / "favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    print("wrote favicons (ico, png)")


def write_guide(lang: str) -> None:
    g = GUIDE[lang]
    ui = UI[lang]
    toc_items = "\n".join(f'        <li><a href="{h}">{t}</a></li>' for h, t in g["toc"])
    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{g["title"]}</title>
  <meta name="description" content="{g["desc"]}" />
  <link rel="icon" href="../favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" sizes="32x32" href="../favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="../favicon-16x16.png" />
  <link rel="apple-touch-icon" href="../apple-touch-icon.png" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="HUMA" />
  <meta property="og:title" content="{g["title"]}" />
  <meta property="og:description" content="{g["desc"]}" />
  <meta property="og:url" content="https://suapapa.github.io/HUMA/{lang}/" />
  <meta property="og:image" content="https://suapapa.github.io/HUMA/og-image.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{g["title"]}" />
  <meta name="twitter:description" content="{g["desc"]}" />
  <meta name="twitter:image" content="https://suapapa.github.io/HUMA/og-image.png" />
  <link rel="stylesheet" href="{CSS}" />
</head>
<body>
{header(lang, "index")}

  <div class="layout">
    <aside class="toc" aria-label="{ui["toc_aria"]}">
      <h2>{ui["toc"]}</h2>
      <ol>
{toc_items}
      </ol>
    </aside>

    <main class="content">
      <header class="hero">
        <div class="hero__copy">
          <h1>{g["h1"]}</h1>
          <p>
            {g["hero"]}
          </p>
          <div class="hero__actions">
            <a class="btn btn-primary" href="#tools">{g["cta_start"]}</a>
            <a class="btn btn-secondary" href="bom.html">{g["cta_bom"]}</a>
          </div>
        </div>
        <figure class="hero__media">
          <img src="{PIC}/HUMA_pcb.webp" alt="{g["pcb_alt"]}" width="800" height="600" />
          <figcaption>{g["pcb_cap"]}</figcaption>
        </figure>
      </header>
{g["body"]}
    </main>
  </div>

{footer(lang)}

  <script src="{JS}" defer></script>
</body>
</html>
"""
    out = ROOT / lang / "index.html"
    out.write_text(html, encoding="utf-8")
    print("wrote", out)


def write_bom(lang: str) -> None:
    m = BOM_META[lang]
    th = m["th"]
    rows = []
    for name, value, ea, descs in BOM_ROWS:
        rows.append(
            f"            <tr><td>{name}</td><td>{value}</td><td>{ea}</td><td>{descs[lang]}</td></tr>"
        )
    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{m["title"]}</title>
  <meta name="description" content="{m["desc"]}" />
  <link rel="icon" href="../favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" sizes="32x32" href="../favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="../favicon-16x16.png" />
  <link rel="apple-touch-icon" href="../apple-touch-icon.png" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="HUMA" />
  <meta property="og:title" content="{m["title"]}" />
  <meta property="og:description" content="{m["desc"]}" />
  <meta property="og:url" content="https://suapapa.github.io/HUMA/{lang}/bom.html" />
  <meta property="og:image" content="https://suapapa.github.io/HUMA/og-image.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{m["title"]}" />
  <meta name="twitter:description" content="{m["desc"]}" />
  <meta name="twitter:image" content="https://suapapa.github.io/HUMA/og-image.png" />
  <link rel="stylesheet" href="{CSS}" />
</head>
<body>
{header(lang, "bom")}

  <div class="layout layout--solo">
    <main class="content">
      <header class="hero hero--solo">
        <div class="hero__copy">
          <h1>{m["h1"]}</h1>
          <p class="page-intro">
            {m["intro"]}
          </p>
          <div class="hero__actions">
            <a class="btn btn-secondary" href="index.html">{m["cta"]}</a>
          </div>
        </div>
      </header>

      <div class="table-wrap">
        <table class="table-parts">
          <thead>
            <tr>
              <th scope="col">{th[0]}</th>
              <th scope="col">{th[1]}</th>
              <th scope="col">{th[2]}</th>
              <th scope="col">{th[3]}</th>
            </tr>
          </thead>
          <tbody>
{chr(10).join(rows)}
          </tbody>
        </table>
      </div>
    </main>
  </div>

{footer(lang)}

  <script src="{JS}" defer></script>
</body>
</html>
"""
    out = ROOT / lang / "bom.html"
    out.write_text(html, encoding="utf-8")
    print("wrote", out)


def write_root_redirect() -> None:
    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>HUMA</title>
  <meta name="description" content="HUMA - HUman MAdeable Arduino assembly guide" />
  <link rel="icon" href="favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png" />
  <link rel="apple-touch-icon" href="apple-touch-icon.png" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="HUMA" />
  <meta property="og:title" content="HUMA - HUman MAdeable Arduino" />
  <meta property="og:description" content="HUMA - 직접 손으로 조립하는 오픈소스 아두이노 호환 보드" />
  <meta property="og:url" content="https://suapapa.github.io/HUMA/" />
  <meta property="og:image" content="https://suapapa.github.io/HUMA/og-image.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="HUMA - HUman MAdeable Arduino" />
  <meta name="twitter:description" content="HUMA - 직접 손으로 조립하는 오픈소스 아두이노 호환 보드" />
  <meta name="twitter:image" content="https://suapapa.github.io/HUMA/og-image.png" />
  <script>
    (function () {
      var langs = ["ko", "en", "ja", "zh"];
      var saved = null;
      try { saved = localStorage.getItem("huma-lang"); } catch (e) {}
      var lang = saved && langs.indexOf(saved) >= 0 ? saved : null;
      if (!lang) {
        var nav = (navigator.language || navigator.userLanguage || "en").toLowerCase();
        if (nav.indexOf("ko") === 0) lang = "ko";
        else if (nav.indexOf("ja") === 0) lang = "ja";
        else if (nav.indexOf("zh") === 0) lang = "zh";
        else lang = "en";
      }
      location.replace("./" + lang + "/");
    })();
  </script>
  <noscript>
    <meta http-equiv="refresh" content="0; url=./en/" />
  </noscript>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 40rem; margin: 3rem auto; padding: 0 1rem; line-height: 1.6; }
    a { margin-right: 1rem; }
  </style>
</head>
<body>
  <p>HUMA documentation</p>
  <p>
    <a href="./ko/">한국어</a>
    <a href="./en/">English</a>
    <a href="./ja/">日本語</a>
    <a href="./zh/">中文</a>
  </p>
</body>
</html>
"""
    out = ROOT / "index.html"
    out.write_text(html, encoding="utf-8")
    print("wrote", out)


def main() -> None:
    build_assets()
    for lang in LANGS:
        (ROOT / lang).mkdir(parents=True, exist_ok=True)
        write_guide(lang)
        write_bom(lang)
    write_root_redirect()
    # legacy redirects
    (ROOT / "huma_bom.html").write_text(
        """<!DOCTYPE html><html><head><meta charset="utf-8"/>
<title>HUMA - BOM</title>
<link rel="icon" href="favicon.ico" sizes="any" />
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png" />
<link rel="apple-touch-icon" href="apple-touch-icon.png" />
<meta property="og:title" content="HUMA - Parts List" />
<meta property="og:image" content="https://suapapa.github.io/HUMA/og-image.png" />
<script>
(function(){var s=null;try{s=localStorage.getItem("huma-lang")}catch(e){}
var l=s||"en";if(["ko","en","ja","zh"].indexOf(l)<0)l="en";
location.replace("./"+l+"/bom.html")})()</script>
<meta http-equiv="refresh" content="0;url=./en/bom.html"/></head>
<body><a href="./en/bom.html">Parts list</a></body></html>
""",
        encoding="utf-8",
    )
    print("wrote", ROOT / "huma_bom.html")


if __name__ == "__main__":
    main()
