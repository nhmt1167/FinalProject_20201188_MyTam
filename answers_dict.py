import os

image_folder = "questions_folder"

answers_dict = {
    "celeb1.png": ["백종원", "baekjongwon", "baek jongwon", "baek jong won"],
    "celeb2.png": ["차은우", "chaeunwoo", "chaeunu", "cha eun woo"],
    "celeb3.png": ["도경수", "디오", "dokyungsoo", "do kyung soo", "do"],
    "celeb4.png": ["공유", "gongyoo", "gong yoo"],
    "celeb5.png": ["현빈", "hyunbin", "hyun bin"],
    "celeb6.png": ["아이유", "이지은", "iu"],
    "celeb7.png": ["jerry"],
    "celeb8.png": ["지민", "박지민", "parkjimin", "jimin", "park jimin", "park ji min", "ji min"],
    "celeb9.png": ["조인성", "jo in sung", "jo insung", "joinsung"],
    "celeb10.png": ["정국", "전정국", "jungkook", "kookie", "jung kook", "jk"],
    "celeb11.png": ["이준호", "준호", "leejunho", "lee junho", "lee jun ho"],
    "celeb12.png": ["이광수", "광수", "kwangsoo", "kwang soo", "lee kwang soo", "leekwangsoo", "lee kwangsoo"],
    "celeb13.png": ["이민호", "leeminho", "lee minho", "lee min ho"],
    "celeb14.png": ["loki"],
    "celeb15.png": ["loopy", "루피"],
    "celeb16.png": ["마동석", "madongseok", "ma dong seok", "ma dongseok"],
    "celeb17.png": ["남주혁", "namjoohyuk", "nam joo hyuk", "nam joohyuk"],
    "celeb18.png": ["나영석", "나피디", "nayeongseok", "na yeongseok", "na yeong-seok", "napd"],
    "celeb19.png": ["barackobama", "barack obama", "obama"],
    "celeb20.png": ["박보검", "parkbogum", "park bo gum", "park bogum"],
    "celeb21.png": ["박서준", "parkseojun", "park seo jun", "park seojun"],
    "celeb22.png": ["펭수", "pengsoo", "peng soo", "pengsu", "peng su"],
    "celeb23.png": ["rex"],
    "celeb24.png": ["알엠", "rm", "남준", "rapmonster"],
    "celeb25.png": ["rose", "로제"],
    "celeb26.png": ["서현진", "seohyunjin", "seo hyun jin", "seo hyunjin"],
    "celeb27.png": ["신세경", "shinsekyung", "shin sekyung", "shin se kyung"],
    "celeb28.png": ["최수영", "수영", "choisooyoung", "choi sooyoung", "sooyoung", "soo young"],
    "celeb29.png": ["stevejobs", "steve jobs"],
    "celeb30.png": ["stevenyeun", "steven yeun"],
    "celeb31.png": ["태양", "taeyang", "tae yang"],
    "celeb32.png": ["thor"],
    "celeb33.png": ["김태형", "뷔", "태태", "v", "taehyung", "kimtaehyung", "kim taehyung", "kim tae hyung"],
    "celeb34.png": ["woody", "우디"]
}


for key in answers_dict:
    answers_dict[key].append(os.path.join(image_folder, key))
