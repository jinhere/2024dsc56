# 경찰청 분실물 종합관리시스템을 위한 분류 모델(Capstone Design 2024-1)
* 소프트웨어융합학과 김유진
* 소프트웨어융합학과 이예찬

## Overview
* 과제의 배경과 필요성<br>
 현재 분실물이 습득되면, 습득자는 근처 지역의 경찰서, 지구대, 파출소에 찾아가거나, 전국 유실물 처리 참여기관(지하철, 철도, 버스, 택시, 공항, 우체국, 대형마트, 쇼핑몰, 박물관, 병원)에 물건을 맡긴다. 습득된 분실물은 경찰관서나 해당 참여기관에서 관리되며, 이후 이 기관들이 경찰청 유실물 통합포털에 접수한다. 접수가 완료되면 경찰청 담당자가 이를 확인하고, 분실물의 세부 정보를 포함한 글을 작성하여 포털에 올린다. 이 글에는 분실물의 종류, 브랜드, 발견된 장소, 특징 등이 상세히 기술된다. 분실자는 경찰청 유실물 통합포털을 통해 해당 글을 검색하고, 본인의 물건임을 확인한 후 해당 기관에 연락하여 물건을 반환받는다. 이 과정에서 분실물의 소유 여부를 확인하기 위해 추가적인 정보나 증빙 서류를 제출해야 할 수도 있다. 이렇게 함으로써 분실물은 원래 주인에게 안전하게 반환되는 구조이다.<br>
  기존 경찰청 유실물 종합관리시스템은 습득한 분실물의 정보(종류, 브랜드, 텍스트 등)를 관리자가 매번 수기로 등록해야 하며, 이에 따라 글이 작성되기 전까지 분실자는 물건을 찾아 헤매야 하는 불편함이 있었다. 따라서 분실물 정보 등록에 걸리는 시간을 최소화하기 위해 분실물의 종류를 판별하는 object detection 모델 도입의 필요성이 제기된다. 후에, 해당 시스템에 물체인식 모델을 배포하여, 담당자가 분실물 글작성 기능을 사용할때 첫화면에 해당 분실물 이미지를 등록할 수 있는 페이지가 있다면 글이 자동작성 되도록 시스템을 만들 수 있을 것이다. 해당 모델은 도입된다면 기존 분실물 관리 시스템을 더 효율적으로 개선하는 것에 도움을 줄 수 있을 것이다.<Br>

* 과제의 목표<br>
  3가지의 augmentation 기법(global color transfer, gaussian noise, cutout)과 2가지의 pseudo label들을 각각 조합하여 6가지의 student 모델을 만든다. Test data 400장에 대해, 기존 teacher 모델보다 성능이 향상된 조합의 student 모델이 있는지 찾아보고, 성능이 향상된 이유 혹은 성능이 하향된 이유 등을 깊이 분석하여 객체인식, 준지도 학습 분야에 대한 지식을 쌓는다. <br>
  


## Schedule
| Contents | March | April |  May  | June  |   Progress   |
|----------|-------|-------|-------|-------|--------------|
|  사전 조사 |       |       |       |       |     Link1    |
|  데이터 크롤링 |       |       |       |       |     Link1    |
|  Annotation |       |       |       |       |     Link2    |
|  지도학습 |       |       |       |       |     Link2    |
|  비지도 학습 |       |       |       |       |     Link2    |

## Results
* Main code, table, graph, comparison, ...
* Web link

``` C++
void Example(int x, int y) {
   ...  
   ... // comment
   ...
}
```

## Conclusion
* Summary, contribution, ...

## Reports
* Upload or link (e.g. Google Drive files with share setting)
* Midterm: [Report](Reports/Midterm.pdf)
* Final: [Report](Reports/Final.pdf), [Demo video](Reports/Demo.mp4)
