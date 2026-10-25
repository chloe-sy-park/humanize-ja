# humanize-ja v1.2 — 한국어 안내

**일본어 원고의 AI 특유 문체를 검수하면서, 작성자 본래의 의미·수치·경험·브랜드 어조를 보존하는 Agent Skill**입니다.

일본 현지 브랜드 마케팅 카피, 상세페이지, 광고, B2B 이메일, 스타트업 창업자의 note/X/LinkedIn 글을 지원합니다. 원어민 검수나 광고 적법성 인증을 대신하지 않으며 AI 작성 여부도 판정하지 않습니다.

- [일본어 공식 README](README.md)
- [일본어 설치 설명서](docs/INSTALL_JA.md)
- [일본어 실전 예시와 프롬프트](docs/EXAMPLES_JA.md)
- [한국어 GitHub 공개 안내](docs/PUBLISH_KO.md)
- [공개 전 체크리스트](docs/PUBLISH_CHECKLIST_JA.md)

## 기본 사용법

스킬을 로드한 뒤 아래처럼 요청합니다.

> humanize-ja의 marketing-copy 모드로 다음 일본어 상품 상세페이지를 검수해줘. 사실·가격·효능 범위를 바꾸지 않고 일본 시장에서 읽기 자연스러운 표현으로 고쳐줘. 근거가 부족하면 HOLD로 표시하고 수정 이유를 한국어로 설명해줘.

## 설치 위치

- Codex: `~/.agents/skills/humanize-ja/` 또는 프로젝트 `.agents/skills/humanize-ja/`
- Claude Code: `~/.claude/skills/humanize-ja/` 또는 프로젝트 `.claude/skills/humanize-ja/`
- ChatGPT: 지원되는 맞춤 스킬 업로드 또는 프로젝트 내 파일·지침 제공

설치 시 `SKILL.md`만 옮기지 말고 `references/` 등 상대경로로 참조하는 자료를 함께 넣어야 합니다. Github 저장소 공개 전이라면 제공된 ZIP을 압축해제해 설치하세요. 외부 Python 라이브러리는 필요하지 않습니다.

이 저장소의 보조 검수 스크립트들은 단순 경고를 제공하며 실제 광고 규제 적합성을 보장하지 않습니다. 공식 근거 및 조사 한계는 [REFERENCES.md](REFERENCES.md)에 있습니다.
