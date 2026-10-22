from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import unquote, urlsplit

from lxml import html


ROOT = Path(__file__).resolve().parent
PAGES = sorted(ROOT.glob("*.html")) + sorted((ROOT / "zh").glob("*.html"))
ERRORS: list[str] = []


def fail(page: Path, message: str) -> None:
    ERRORS.append(f"{page.relative_to(ROOT)}: {message}")


for page in PAGES:
    document = html.document_fromstring(page.read_text(encoding="utf-8"))
    expected_lang = "zh-CN" if page.parent.name == "zh" else "en"

    if document.get("lang") != expected_lang:
        fail(page, f"expected lang={expected_lang!r}, got {document.get('lang')!r}")
    if len(document.xpath("//h1")) != 1:
        fail(page, f"expected one h1, found {len(document.xpath('//h1'))}")
    if document.xpath('//*[contains(concat(" ", normalize-space(@class), " "), " en ") or contains(concat(" ", normalize-space(@class), " "), " zh ")]'):
        fail(page, "generated output still contains language-toggle content classes")

    checks = {
        "canonical": '//link[@rel="canonical"]',
        "description": '//meta[@name="description"]',
        "og:title": '//meta[@property="og:title"]',
        "og:description": '//meta[@property="og:description"]',
        "og:url": '//meta[@property="og:url"]',
        "JSON-LD": '//script[@type="application/ld+json"]',
        "hreflang=en": '//link[@rel="alternate" and @hreflang="en"]',
        "hreflang=zh-CN": '//link[@rel="alternate" and @hreflang="zh-CN"]',
        "hreflang=x-default": '//link[@rel="alternate" and @hreflang="x-default"]',
    }
    for label, xpath in checks.items():
        if len(document.xpath(xpath)) != 1:
            fail(page, f"expected exactly one {label}")

    for script in document.xpath('//script[@type="application/ld+json"]'):
        try:
            json.loads(script.text or "")
        except json.JSONDecodeError as error:
            fail(page, f"invalid JSON-LD: {error}")

    for element in document.xpath('//*[@href or @src]'):
        for attribute in ("href", "src"):
            value = element.get(attribute)
            if not value or value.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
                continue
            local_path = unquote(urlsplit(value).path)
            if not local_path:
                continue
            target = (page.parent / local_path).resolve()
            if not target.exists():
                fail(page, f"broken local {attribute}: {value}")


if not (ROOT / "sitemap.xml").exists():
    ERRORS.append("missing sitemap.xml")
if not (ROOT / "robots.txt").exists():
    ERRORS.append("missing robots.txt")
if not (ROOT / "assets/resume/Nana-Tan-SEO-Resume-EN.pdf").exists():
    ERRORS.append("missing English resume PDF")
if not (ROOT / "assets/resume/Tan-Danna-Overseas-SEO-Resume-ZH.pdf").exists():
    ERRORS.append("missing Chinese resume PDF")

if ERRORS:
    raise SystemExit("\n".join(ERRORS))

print(f"Validated {len(PAGES)} localized pages with no structural or local-link errors.")
