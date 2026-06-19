from dataclasses import dataclass, field, asdict
from typing import List, Optional
from datetime import date

@dataclass
class KeywordNote:
    keyword: str
    note: str
    url: str
    created: date
    tags: List[str] = field(default_factory=list)
    priority: int = 0

    def formatted(self) -> str:
        tag_str = ", ".join(self.tags) if self.tags else "无标签"
        return (
            f"【关键词】{self.keyword}\n"
            f"  笔记：{self.note}\n"
            f"  来源：{self.url}\n"
            f"  日期：{self.created}\n"
            f"  标签：{tag_str}\n"
            f"  优先级：{self.priority}\n"
        )


def format_note_list(notes: List[KeywordNote], max_count: Optional[int] = None) -> str:
    if max_count is not None:
        notes = notes[:max_count]
    lines = []
    for i, note in enumerate(notes, 1):
        lines.append(f"--- 笔记 {i} ---")
        lines.append(note.formatted())
    return "\n".join(lines)


def sample_notes() -> List[KeywordNote]:
    return [
        KeywordNote(
            keyword="麻将胡了",
            note="经典役种，包含多种和牌型，是入门必学的基本规则。",
            url="https://main-portal-mahjong.com",
            created=date(2025, 2, 15),
            tags=["麻将", "规则", "入门"],
            priority=3,
        ),
        KeywordNote(
            keyword="立直",
            note="门清状态下宣言听牌，需要1000点棒作为供托。",
            url="https://main-portal-mahjong.com",
            created=date(2025, 3, 1),
            tags=["麻将", "役种", "立直"],
            priority=2,
        ),
        KeywordNote(
            keyword="断幺九",
            note="全部由中张牌组成，无幺九牌，容易达成。",
            url="https://main-portal-mahjong.com",
            created=date(2025, 1, 20),
            tags=["麻将", "役种", "简单"],
            priority=1,
        ),
        KeywordNote(
            keyword="一发",
            note="立直后第一巡内自摸和牌，与立直组合威力更强。",
            url="https://main-portal-mahjong.com",
            created=date(2025, 4, 5),
            tags=["麻将", "进阶", "立直"],
            priority=2,
        ),
    ]


def main():
    notes = sample_notes()
    print("所有关键词笔记：\n")
    print(format_note_list(notes))

    print("\n\n高优先级笔记（优先级 >= 2）：\n")
    high_priority = [n for n in notes if n.priority >= 2]
    print(format_note_list(high_priority))

    print("\n\n第一个笔记摘要（asdict）：\n")
    print(asdict(notes[0]))


if __name__ == "__main__":
    main()