# 경찰청 분실물 종합관리시스템을 위한 분류 모델(Capstone Design 2024-1)
* 소프트웨어융합학과 김유진
* 소프트웨어융합학과 이예찬

## Overview
* ### 과제의 배경과 필요성<br>
현재 분실물이 습득되면, 습득자는 근처 지역의 경찰서, 지구대, 파출소에 찾아가거나, 전국 유실물 처리 참여기관(지하철, 철도, 버스, 택시, 공항, 우체국, 대형마트, 쇼핑몰, 박물관, 병원)에 물건을 맡긴다. 습득된 분실물은 경찰관서나 해당 참여기관에서 관리되며, 이후 이 기관들이 경찰청 유실물 통합포털에 접수한다. 접수가 완료되면 경찰청 담당자가 이를 확인하고, 분실물의 세부 정보를 포함한 글을 작성하여 포털에 올린다. 이 글에는 분실물의 종류, 브랜드, 발견된 장소, 특징 등이 상세히 기술된다. 분실자는 경찰청 유실물 통합포털을 통해 해당 글을 검색하고, 본인의 물건임을 확인한 후 해당 기관에 연락하여 물건을 반환받는다. 이 과정에서 분실물의 소유 여부를 확인하기 위해 추가적인 정보나 증빙 서류를 제출해야 할 수도 있다. 이렇게 함으로써 분실물은 원래 주인에게 안전하게 반환되는 구조이다.<br>
  기존 경찰청 유실물 종합관리시스템은 습득한 분실물의 정보(종류, 브랜드, 텍스트 등)를 관리자가 매번 수기로 등록해야 하며, 이에 따라 글이 작성되기 전까지 분실자는 물건을 찾아 헤매야 하는 불편함이 있었다. 따라서 분실물 정보 등록에 걸리는 시간을 최소화하기 위해 분실물의 종류를 판별하는 object detection 모델 도입의 필요성이 제기된다. 후에, 해당 시스템에 물체인식 모델을 배포하여, 담당자가 분실물 글작성 기능을 사용할때 첫화면에 해당 분실물 이미지를 등록할 수 있는 페이지가 있다면 글이 자동작성 되도록 시스템을 만들 수 있을 것이다. 해당 모델은 도입된다면 기존 분실물 관리 시스템을 더 효율적으로 개선하는 것에 도움을 줄 수 있을 것이다.<Br>

* ### 과제의 목표<br>
3가지의 augmentation 기법(global color transfer, gaussian noise, cutout)과 2가지의 pseudo label들을 각각 조합하여 6가지의 student 모델을 만든다. Test data 400장에 대해, 기존 teacher 모델보다 성능이 향상된 조합의 student 모델이 있는지 찾아보고, 성능이 향상된 이유 혹은 성능이 하향된 이유 등을 깊이 분석하여 객체인식, 준지도 학습 분야에 대한 지식을 쌓는다. <br>
  


## Schedule
| Contents | March | April |  May  | June  |   Progress   |
|----------|-------|-------|-------|-------|--------------|
|  사전 조사 |    O   |    O   |   O    |    O   |     객체인식, 리눅스 환경, 준지도 학습 분야에 대한 리서치    |
|  데이터 크롤링 |   O    |       |       |       |     경찰청에서 자주 분실되는 분실물 카테고리 8개(card, card holder, earbuds, glasses, gloves, muffler, phone, umbrella)에 해당하는 분실물들의 사진들을 수집    |
|  Annotation |   O    |    O   |    O   |       |     11,400장에 대해 annotation 수행    |
|  지도학습 |       |    O   |    O   |       |     베이스 모델인 yolo v8m에 11,000장(train set 10,000장 & validation set 10,000장)의 labeled data를 epoch=100번 전이 학습    |
|  비지도 학습 |       |    O   |    O   |   O    |    3가지의 augmentation 기법(global color transfer, gaussian noise, cutout)과 2가지의 pseudo label(confidence threshold=0.8, 0.9)들을 각각 조합하여 6가지의 student 모델 학습   |
|  결과 분석 |       |       |       |   O    |    semi supervised learning을 진행한  student model들 사이의 성능을 평가 및 비교분석(F1-Confidence Curve, Precision-Recall Curve, Confusion Matrix를 중심으로)     |

## YOLO v8 Codes
config.yaml
``` YAML
path: C:/Programming/2024DSC/data # root dir. absolute path
train: images/train # train images (relative to 'path')
val: images/val # val images (relative to 'path') 

# Classes
names:
  0: card
  1: cardholder
  2: earbuds
  3: glasses
  4: gloves
  5: muffler
  6: phone
  7: umbrella
}
```
<br>

Transfer Learning YOLO Code

``` Python
from ultralytics import YOLO

model=YOLO('yolov8m.pt')
results=model.train(data='config.yaml',epochs=100)
```
<br>

## Semi Supervised Learning Flow
<img width="484" alt="image" src="https://github.com/jinhere/Lost-and-Found-with-YOLO/assets/74696590/ac7af0fb-36c7-4b59-baa4-1b9aedce40ea">
<br>

## Results

### 성능 평가 결과 <br>
<img width="495" alt="image" src="https://github.com/jinhere/Lost-and-Found-with-YOLO/assets/74696590/d93f21c7-e347-498a-ba0a-89b7b3aa65a0">

### 그래프분석<br>
- 첫째, teacher 모델의 성능이 모든 평가 지표에서 여전히 다른 모든 students보다 높았다. student model에서 왜 더 낮은 성능을 보였는지는 아래에서 자세하게 분석한다.
- 둘째, student 모델들의 성능이 학습데이터의 confidence threshold가 0.8일 때가 0.9일때보다 결과가 좋았다. 이유를 분석해봤을때, confidence가 0.9로 높았을 때는 해당 이미지에서 실제 물체가 존재함에도 존재하지 않는다는 잘못된 annotation을 했을 가능성이 높다. 비교적 threshold가 낮았던 0.8의 경우에는 인식한 물체들이 더 많았을 것이다. 즉, confidence가 0.8 이상인 bounding box들을 포함한 pseudo label들이 더 실제 label과 가까웠다는 걸로 해석할 수 있고, 더 정확한 pseudo label로 학습한 student model들이 더 성능이 좋게 나왔다.
- 셋째, augmentation method로써 global color transfer를 사용한 모델은 cutout을 사용한 모델과 성능이 비슷했으나, 그 둘과 비교하였을 때 gaussian noise를 사용한 모델의 성능은 비교적 낮았다. 그 이유를 두 가지로 추정한다. 첫 번째 이유로, gaussian noise augmentation의 강도를 너무 지나치게 설정했을 수 있다. 두 번째 이유로, 경찰청 유실물 종합관리센터에서 크롤링한 이미지 중, 해상도가 크지 않거나 초점이 흐릿한 이미지의 비중이 높은 편이었는데 이 경우 이미지로부터 object를 detect하기 어렵게 만들었을 수 있다.

### Student 모델이 teacher model보다 더 낮은 성능을 보인 이유<br>

   #### student 모델의 학습데이터 선별 과정에서의 문제  
- student model의 학습데이터에는 오직 teacher model이 pseudo labeling한 이미지들만 train data에 포함시켰다. pseudo labeling 외에도 기존 teacher model이 학습에 사용했던 labeled image를 포함시켰다면 더 실제에 가까운 성능을 보였을거라 기대한다.
- 실제 label과 유사한 pseudo labeling을 얻기 위해 teacher model이 예측할 당시 confidence threshold를 높게 설정하는 방법만 사용했었다. 하지만 이 외에 다른 방법들을 혼합해서 label의 신빙성을 더 높일 수 있을 것이라 기대한다. 추가적인 방법들은 크게 두가지이다. 
  - Model Ensemble: 여러 teacher 모델을 사용하여 예측 결과를 결합하는 방법이다. 서로 다른 아키텍처와 하이퍼파라미터 설정을 가진 모델들을 사용하면, 각 모델의 약점을 보완할 수 있다. 여러 모델의 예측 결과를 평균 내거나 투표 방식을 사용하여 최종 pseudo label을 생성하면 더 신뢰성 있는 레이블을 얻을 수 있다.
  - Self-Training with Augmentation: 데이터 증강을 사용하여 원본 이미지의 변형된 버전을 생성하고, 이 변형된 데이터에 대해 pseudo label을 생성한다. 동일한 이미지의 여러 버전에서 일관된 예측을 얻을 수 있는지 확인함으로써 pseudo label의 신뢰성을 높일 수 있다.
- confidence threshold를 설정할 때 좀 더 다양한 range의 confidence threshold 값으로 실험을 할 수 있었다면 최적의 threshold를 찾을 수 있을 것이다. 하지만 여러 threshold값들을 무작위로 선정하기보다는, 특정 기준을 가지고 threshold 후보를 선택한다면 더 효과적으로 최적값을 찾을 수 있을 것이다. 예를 들어, 가장 f1 score가 높은 confidence값 근방의 값을 선별한다던가, 프로젝트의 특성에 따라 지켜져야 하는 최소 precision과 recall값 기준이 있다면 대응하는 confidence 값의 근방값들로 범위를 좁힐 수 있다.
- teacher 학습시와 마찬가지로 student 모델의 학습데이터에도 해당 8개 클래스 외 물건들이 포함된 background 클래스의 사진들을 일정 비율 포함했다면 generalization performance를 더 높일 수 있었을 것이다. 

#### Hyperparamter Tuning의 한계
- 트레이닝 configuration시 epoch 외 하이퍼파라미터들은 설정값을 사용했었다. 하지만 학습률, 배치 크기, 앵커 박스 개수와 크기, 네트워크 깊이, 네트워크 폭, 셀 그리드 크기, 객체성 손실 가중치, 클래스 손실 가중치, 좌표 손실 가중치, 비객체성 손실 가중치, 드롭아웃 비율, 데이터 증강 기법, 초기 가중치, 그리고 최적화 알고리즘 등의 하이퍼파라미터들을 조정하여 성능을 향상시킬 수 있다.

#### Augmentation 방법에서의 잠재적인 문제
아래와 같은 사항들을 고려했다면 student model의 성능을 높이는 데에 도움을 주었을 것으로 추측한다.

- 본 연구에서는 augmentation의 강도를 설정할 때, 객관적인 기준 없이 강도를 설정하였다. Augmented 이미지에서 사람이 물체의 위치와 종류를 판별할 수 있을 정도로 augmentation을 진행했으나, 그 기준이 모호하고 주관적이었기 때문에 성능 향상을 저해했을 수 있다.
- Student model의 training dataset을 global color transfer, cutout, gaussian noise 세 가지 방법으로 augmentation을 진행했다. 더 많은 방법들을 실험해보는 것이 바람직했겠으나, 시간 관계상 많은 종류의 augmentation 방식에 대해 실험을 진행해보지 못했다. 실험하였던 세 가지 augmentation 방법들은 일반적인 augmentation에 속하지만, 이와 다른 augmentation 방법을 사용했다면 더 좋은 성능을 낼 수 있었을 것으로 추측한다.
   다른 augmentation 방식을 사용하면 더 좋은 성능을 냈을 가능성이 있다.
  - 한 가지가 아닌, 여러 가지 augmentation 방식을 섞어서 사용하면 더 좋은 성능을 냈을 가능성이 있다.
  - 연구 진행 중, YOLO 내부에서 이미 기본값으로 augmentation을 한다는 사실을 뒤늦게 알게 되었다. Student model의 training set에 strong augmentation을 적용했는데, 거기에 추가로 augmentation을 했던 것이다. 이 때문에 student model이  object를 잘 detect하기 어렵게 만들었을 수 있다.

#### Semi-supervised model architecture의 잠재적인 문제
연구 중, 비록 제한된 조건 하에서였지만, 전이학습을 진행하지 않은 student model이 전이학습을 진행한 student model보다 성능이 더 뛰어난 결과를 보인 사례가 있었다. 이는 전이학습을 통해 student model의 학습 시간을 줄이면서 성능을 높일 것이라는 일반적인 기대를 벗어난 결과였다. Student model의 성능 향상을 위해, 전이학습이 아닌 다른 방법을 시도하는 것을 고려해볼 수 있다.

## 기대효과 및 활용방안
기존 시스템에서는 관리자가 매번 수기로 분실물 정보를 등록해야 하므로 시간이 많이 소요된다. Object detection 모델을 도입하면 자동으로 분실물의 종류를 판별하고 필요한 정보를 신속하게 등록할 수 있다. 이를 통해 분실물 정보 등록에 걸리는 시간을 크게 단축할 수 있다. 
분실물 정보가 신속하게 등록되면 분실자들은 더 빠르게 자신의 물건을 찾을 수 있다. 이는 분실자들이 경찰청을 방문하거나 온라인 시스템을 통해 분실물 정보를 검색할 때 효율성을 높인다. 결과적으로 분실물 찾기에 소요되는 시간을 줄이고, 분실자의 스트레스를 줄이는 데 기여한다.
또한, 수작업으로 분실물 정보를 등록하는 과정에서 발생할 수 있는 오류를 줄일 수 있다. Object detection 모델은 일관된 기준으로 분실물을 판별하고 정보를 등록하므로 데이터의 정확성을 높일 수 있다. 이는 분실물 관리의 효율성을 높이고, 분실물 검색 과정에서 잘못된 정보를 제공할 가능성을 줄인다.
마지막으로, 경찰청의 인력 자원을 더 효율적으로 사용할 수 있다. 분실물 정보를 자동으로 등록함으로써 관리자의 업무 부담을 줄이고, 이를 통해 보다 중요한 업무에 인력을 집중할 수 있다. 이는 경찰청의 운영 효율성을 높이고, 전체적인 업무 처리 속도를 개선할 수 있다.

## Reports
* Midterm: [Report](Reports/Mid.pdf)
* Final: [Report](Reports/Final.pdf), [Demo video](Reports/Demo.mp4)
