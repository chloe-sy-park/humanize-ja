# humanize-ja v1.2 GitHub 공개 안내 (한국어)

현재 ZIP은 **공개 준비가 완료된 로컬 저장소 파일**입니다. `chloe-sy-park/humanize-ja` 원격 저장소가 생성되었거나 온라인 게시되었다는 뜻은 아닙니다.

## 1. GitHub에서 빈 저장소 생성

1. GitHub 계정 `chloe-sy-park`로 로그인합니다.
2. [새 저장소 만들기](https://github.com/new)에서 Repository name에 `humanize-ja`를 입력합니다.
3. Description: `Open-source Japanese writing humanizer skill for founders, marketers, advertising and business email — fact-preserving, voice-first.`
4. Public을 선택합니다. README, .gitignore, License 자동 추가는 **선택하지 않습니다**. (압축파일에 이미 포함돼 있습니다.)
5. Create repository를 클릭합니다.

## 2. 맥에서 ZIP 업로드

1. `humanize-ja-v1.2-public-github-repo.zip`을 다운로드하고 압축 해제합니다.
2. 터미널에서 압축 해제된 `humanize-ja` 폴더로 이동합니다. (`cd ` 입력 후 Finder에서 폴더를 터미널로 드래그해도 됩니다.)
3. 다음을 실행합니다.

```bash
git init -b main
git add .
git status
git commit -m "docs: prepare humanize-ja v1.2 for public release"
git remote add origin https://github.com/chloe-sy-park/humanize-ja.git
git push -u origin main
```

GitHub 인증과 Git 이름/이메일 설정은 본인 로컬 환경에 따라 별도로 요구될 수 있습니다. 이미 Git 저장소로 초기화되어 있다면 `git init`은 건너뛰고 `git remote -v`부터 확인하세요.

## 3. 첫 공개 후 점검

- README 상단의 일본어, 설치 안내, 예시 링크가 열리는지 확인
- Actions > Validation에서 두 Python 버전의 테스트가 통과하는지 확인
- `LICENSE`의 저작권자 표기를 최종 선택하고, `THIRD_PARTY_NOTICES.md`를 재확인
- `README.md`와 `docs/INSTALL_JA.md`의 `OWNER` 예시를 `chloe-sy-park`로 수정
- Releases에서 태그 `v1.2.0`과 `docs/RELEASE_NOTES_JA.md` 내용을 기반으로 첫 릴리스 생성

## 4. 추천 주제(Topics)

`agent-skills`, `japanese`, `writing`, `copywriting`, `marketing`, `claude-code`, `codex`, `editing`

검증된 원어민 편집 품질·광고 성과·법적 적합성을 보장하는 프로젝트로 소개하지 마세요. 현재 검증은 규칙 및 자동 테스트, 공개 원문을 활용한 제한적인 사례 비교에 해당합니다.
