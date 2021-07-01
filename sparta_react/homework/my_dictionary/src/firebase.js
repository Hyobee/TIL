import firebase from "firebase/app";
import "firebase/firestore";

const firebaseConfig = {
    // firebase 설정과 관련된 개인 정보
    apiKey: "AIzaSyCibu8UD3h-hmAac51-10sT7cV9BNrcFWE",
    authDomain: "sparta-react-7c473.firebaseapp.com",
    projectId: "sparta-react-7c473",
    storageBucket: "sparta-react-7c473.appspot.com",
    messagingSenderId: "91571784526",
    appId: "1:91571784526:web:7ba829255249be2557ec1f",
    measurementId: "G-3QYRH6P97R"
};

// firebaseConfig 정보로 firebase 시작
firebase.initializeApp(firebaseConfig);

// firebase의 firestore 인스턴스를 변수에 저장
const firestore = firebase.firestore();

// 필요한 곳에서 사용할 수 있도록 내보내기
export { firestore };