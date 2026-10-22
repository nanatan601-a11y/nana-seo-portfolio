from __future__ import annotations

import copy
import json
from pathlib import Path

from lxml import etree, html


ROOT = Path(__file__).resolve().parent
SOURCE_DIR = ROOT / "source" / "pages"
ZH_DIR = ROOT / "zh"
BASE_URL = "https://nanatan601-a11y.github.io/nana-seo-portfolio/"

PAGE_META = {
    "index.html": {
        "en": (
            "Nana Tan | Overseas SEO Specialist & Organic Growth Strategist",
            "Bilingual SEO specialist with hands-on experience in B2B, e-commerce, local SEO, technical SEO, SEM, and AI search visibility.",
        ),
        "zh": (
            "谈丹娜｜海外 SEO 专员与独立站增长",
            "双语海外 SEO 专员，拥有 B2B、电商、本地 SEO、技术 SEO、SEM 与 AI 搜索可见度优化经验。",
        ),
        "type": "ProfilePage",
    },
    "cases.html": {
        "en": (
            "SEO Case Studies | Nana Tan",
            "Explore proof-backed SEO projects across B2B lead generation, e-commerce revenue, local search, technical SEO, and SEM.",
        ),
        "zh": (
            "SEO 案例作品集｜谈丹娜",
            "查看覆盖 B2B 询盘增长、电商收入、本地搜索、技术 SEO 与 SEM 的数据化案例。",
        ),
        "type": "CollectionPage",
    },
    "skills.html": {
        "en": (
            "SEO Capabilities | Nana Tan",
            "SEO capabilities across strategy, technical execution, content systems, e-commerce, B2B lead generation, SEM, analytics, and bilingual collaboration.",
        ),
        "zh": (
            "海外 SEO 核心能力｜谈丹娜",
            "覆盖 SEO 策略、技术执行、内容体系、电商增长、B2B 询盘、SEM、数据分析与双语协作。",
        ),
        "type": "ProfilePage",
    },
    "case-maggie.html": {
        "en": (
            "Maggie Sun Real Estate SEO Case Study | Nana Tan",
            "Remote, project-based local SEO and SEM case study covering bilingual content, technical SEO, Google Ads, lead tracking, and 41 qualified leads.",
        ),
        "zh": (
            "Maggie Sun 房地产 SEO 案例｜谈丹娜",
            "海外远程项目制案例，覆盖本地 SEO、双语内容、技术 SEO、Google Ads、线索追踪及 41 个有效线索。",
        ),
        "type": "CreativeWork",
        "image": "assets/img/maggie-geo.png",
    },
    "case-wjs.html": {
        "en": (
            "WJS Home E-commerce SEO Case Study | Nana Tan",
            "E-commerce SEO case study covering $265K+ USD in GA4 Organic Search revenue, Shopify technical SEO, content growth, and traffic recovery.",
        ),
        "zh": (
            "WJS Home 电商 SEO 案例｜谈丹娜",
            "覆盖超过 26.5 万美元 GA4 自然搜索收入、Shopify 技术 SEO、内容增长和流量恢复的电商 SEO 案例。",
        ),
        "type": "CreativeWork",
        "image": "assets/img/wjs-ga4.png",
    },
    "case-mokafx.html": {
        "en": (
            "Moka SFX B2B SEO & SEM Case Study | Nana Tan",
            "B2B SEO and SEM case study covering organic traffic growth, inquiry-quality analysis, technical SEO, and reduced wasted advertising spend.",
        ),
        "zh": (
            "Moka SFX B2B SEO 与 SEM 案例｜谈丹娜",
            "覆盖自然流量增长、询盘质量分析、技术 SEO 和广告降本增效的 B2B SEO 与 SEM 案例。",
        ),
        "type": "CreativeWork",
    },
    "case-sunsara.html": {
        "en": (
            "Sunsara Beauty B2B SEO Case Study | Nana Tan",
            "Early-stage B2B SEO case study covering keyword research, English content, product-page optimization, publishing workflows, and organic inquiry growth.",
        ),
        "zh": (
            "Sunsara Beauty B2B SEO 案例｜谈丹娜",
            "覆盖关键词研究、英文内容、产品页优化、发布流程和自然询盘增长的早期 B2B SEO 案例。",
        ),
        "type": "CreativeWork",
        "image": "assets/img/sunsara-comments.jpg",
    },
    "case-maggie-local-growth.html": {
        "en": (
            "Maggie Sun Local Search Growth Deep Dive | Nana Tan",
            "A detailed look at the local SEO, bilingual content, Google Ads, technical SEO, and lead-tracking system built for Maggie Sun Real Estate.",
        ),
        "zh": (
            "Maggie Sun 本地搜索增长深度案例｜谈丹娜",
            "深入拆解 Maggie Sun Real Estate 的本地 SEO、双语内容、Google Ads、技术 SEO 和线索追踪体系。",
        ),
        "type": "Article",
        "image": "assets/img/maggie-reddit-discussion.png",
    },
    "case-wjs-recovery.html": {
        "en": (
            "WJS Home Organic Traffic Recovery | Nana Tan",
            "A detailed look at how affected page patterns, content consolidation, and page-role planning supported WJS Home's organic traffic recovery.",
        ),
        "zh": (
            "WJS Home 自然搜索流量恢复案例｜谈丹娜",
            "深入拆解如何通过受影响页面分析、内容整合和页面角色规划推动 WJS Home 自然搜索流量恢复。",
        ),
        "type": "Article",
        "image": "assets/img/wjs-gsc.png",
    },
    "case-moka-sfx-ads.html": {
        "en": (
            "Moka SFX Ads Optimization Deep Dive | Nana Tan",
            "A detailed look at how inquiry-quality analysis, search-term reviews, negative keywords, and exclusion rules reduced wasted ad spend.",
        ),
        "zh": (
            "Moka SFX 广告优化深度案例｜谈丹娜",
            "深入拆解如何通过询盘质量分析、搜索词复盘、否定关键词和排除规则减少无效广告支出。",
        ),
        "type": "Article",
    },
}

ZH_TEXT = {
    "Home": "首页",
    "Cases": "案例",
    "Capabilities": "能力",
    "Contact": "联系",
    "View case": "查看案例",
    "Website": "官网",
    "Visit website": "访问网站",
    "View Semrush": "查看 Semrush",
    "Previous": "上一张",
    "Next": "下一张",
    "All cases": "所有案例",
    "Previous: Maggie": "上一个案例：Maggie",
    "Next: WJS Home": "下一个案例：WJS Home",
    "Previous: WJS Home": "上一个案例：WJS Home",
    "Next: Moka SFX": "下一个案例：Moka SFX",
    "Previous: Moka SFX": "上一个案例：Moka SFX",
    "Next: Sunsara": "下一个案例：Sunsara",
    "← Cases": "← 返回案例",
    "CRM evidence: 41 qualified leads. Personal information has been anonymized.": "CRM 数据：共 41 个有效线索，客户个人信息已做匿名处理。",
    "Google Ads: keyword campaigns, CTR, cost, and lead forms.": "Google Ads：关键词广告、CTR、费用及线索表单。",
    "GSC: clicks and impressions after tracking setup.": "GSC：追踪搭建后的点击与展示数据。",
    "GSC Generative AI: 44.4K impressions.": "GSC Generative AI：44.4K 次展示。",
    "GA4: $265,788.78 in Organic Search revenue, Nov 1, 2025-Jul 31, 2026.": "GA4：2025 年 11 月 1 日至 2026 年 7 月 31 日期间，Organic Search 收入为 265,788.78 美元。",
    "GA4 pre-engagement baseline: Jul 1-Oct 31, 2025.": "GA4 项目开始前基线：2025 年 7 月 1 日至 10 月 31 日。",
    "GSC: 16.7K clicks and 1.16M impressions.": "GSC：16.7K 次点击和 1.16M 次展示。",
    "GSC Generative AI: 50.7K impressions.": "GSC Generative AI：50.7K 次展示。",
    "GSC indexing: 4.14K indexed pages.": "GSC 收录：4.14K 个已收录页面。",
    "Core Web Vitals: Passed, with LCP 1.7s, INP 121ms, CLS 0.": "Core Web Vitals：通过评估，LCP 1.7 秒、INP 121 毫秒、CLS 0。",
    "Blog proof: “Curly Hair Struggles” received 433 comments.": "博客证明：《Curly Hair Struggles》获得 433 条评论。",
}

ARIA_ZH = {
    "Main navigation": "主要导航",
    "Language switcher": "语言切换",
    "Case navigation": "案例导航",
}


def page_url(filename: str, language: str) -> str:
    if filename == "index.html":
        return BASE_URL if language == "en" else f"{BASE_URL}zh/"
    return f"{BASE_URL}{filename}" if language == "en" else f"{BASE_URL}zh/{filename}"


def set_element_text(element: etree._Element, value: str) -> None:
    leading = " " if element.text and element.text.startswith(" ") else ""
    trailing = " " if element.text and element.text.endswith(" ") else ""
    element.text = f"{leading}{value}{trailing}"


def remove_language_nodes(document: etree._Element, language: str) -> None:
    opposite = "zh" if language == "en" else "en"
    opposite_xpath = f'//*[contains(concat(" ", normalize-space(@class), " "), " {opposite} ")]'
    selected_xpath = f'//*[contains(concat(" ", normalize-space(@class), " "), " {language} ")]'
    for element in list(document.xpath(opposite_xpath)):
        parent = element.getparent()
        if parent is not None:
            parent.remove(element)

    for element in document.xpath(selected_xpath):
        classes = [name for name in (element.get("class") or "").split() if name != language]
        if classes:
            element.set("class", " ".join(classes))
        else:
            element.attrib.pop("class", None)


def replace_language_switcher(document: etree._Element, filename: str, language: str) -> None:
    switcher_xpath = '//*[contains(concat(" ", normalize-space(@class), " "), " lang-toggle ")]'
    for switcher in document.xpath(switcher_xpath):
        for child in list(switcher):
            switcher.remove(child)

        en_link = etree.Element("a", href=filename if language == "en" else f"../{filename}")
        en_link.set("hreflang", "en")
        en_link.set("lang", "en")
        en_link.text = "EN"

        zh_link = etree.Element("a", href=f"zh/{filename}" if language == "en" else filename)
        zh_link.set("hreflang", "zh-CN")
        zh_link.set("lang", "zh-CN")
        zh_link.text = "中文"

        (en_link if language == "en" else zh_link).set("class", "active")
        switcher.extend([en_link, zh_link])


def localize_shared_ui(document: etree._Element) -> None:
    for element in document.iter():
        if element.text and element.text.strip() in ZH_TEXT:
            set_element_text(element, ZH_TEXT[element.text.strip()])
        if element.tail and element.tail.strip() in ZH_TEXT:
            element.tail = element.tail.replace(element.tail.strip(), ZH_TEXT[element.tail.strip()])

        aria_label = element.get("aria-label")
        if aria_label in ARIA_ZH:
            element.set("aria-label", ARIA_ZH[aria_label])


def adjust_asset_paths(document: etree._Element, language: str) -> None:
    if language != "zh":
        return
    for element in document.xpath("//*[@href or @src]"):
        for attr in ("href", "src"):
            value = element.get(attr)
            if value and value.startswith("assets/"):
                element.set(attr, f"../{value}")


def add_head_metadata(document: etree._Element, filename: str, language: str) -> None:
    meta = PAGE_META[filename]
    title, description = meta[language]
    canonical = page_url(filename, language)
    alternate_language = "zh" if language == "en" else "en"

    head = document.find("head")
    title_node = head.find("title")
    if title_node is None:
        title_node = etree.SubElement(head, "title")
    title_node.text = title

    for node in list(head.xpath(
        './meta[@name="description" or starts-with(@property, "og:") or starts-with(@name, "twitter:")]'
        '|./link[@rel="canonical" or @rel="alternate"]'
        '|./script[@type="application/ld+json"]'
    )):
        head.remove(node)

    etree.SubElement(head, "meta", name="description", content=description)
    etree.SubElement(
        head,
        "link",
        rel="icon",
        type="image/svg+xml",
        href="assets/img/favicon.svg" if language == "en" else "../assets/img/favicon.svg",
    )
    etree.SubElement(head, "link", rel="canonical", href=canonical)
    etree.SubElement(head, "link", rel="alternate", hreflang="en", href=page_url(filename, "en"))
    etree.SubElement(head, "link", rel="alternate", hreflang="zh-CN", href=page_url(filename, "zh"))
    etree.SubElement(head, "link", rel="alternate", hreflang="x-default", href=page_url(filename, "en"))

    og_type = "article" if meta["type"] in {"Article", "CreativeWork"} else "website"
    og_values = {
        "og:title": title,
        "og:description": description,
        "og:type": og_type,
        "og:url": canonical,
        "og:site_name": "Nana Tan SEO Portfolio",
        "og:locale": "en_US" if language == "en" else "zh_CN",
        "og:locale:alternate": "zh_CN" if language == "en" else "en_US",
    }
    if meta.get("image"):
        og_values["og:image"] = f"{BASE_URL}{meta['image']}"
        og_values["og:image:alt"] = title

    for prop, content in og_values.items():
        etree.SubElement(head, "meta", property=prop, content=content)

    etree.SubElement(head, "meta", name="twitter:card", content="summary_large_image" if meta.get("image") else "summary")
    etree.SubElement(head, "meta", name="twitter:title", content=title)
    etree.SubElement(head, "meta", name="twitter:description", content=description)
    if meta.get("image"):
        etree.SubElement(head, "meta", name="twitter:image", content=f"{BASE_URL}{meta['image']}")

    person_name = "Nana Tan" if language == "en" else "谈丹娜"
    person_description = (
        "Bilingual overseas SEO specialist focused on measurable organic growth across B2B, e-commerce, and local markets."
        if language == "en"
        else "专注 B2B、电商与本地市场可衡量自然增长的双语海外 SEO 专员。"
    )
    language_code = "en" if language == "en" else "zh-CN"
    graph = [
        {
            "@type": "Person",
            "@id": f"{BASE_URL}#nana-tan",
            "name": person_name,
            "alternateName": "谈丹娜" if language == "en" else "Nana Tan",
            "jobTitle": "Overseas SEO Specialist" if language == "en" else "海外 SEO 专员",
            "description": person_description,
            "url": BASE_URL,
            "email": "mailto:nanatan601@gmail.com",
            "telephone": "+86 188 2414 8436",
            "knowsAbout": [
                "Search engine optimization",
                "Technical SEO",
                "E-commerce SEO",
                "B2B lead generation",
                "Local SEO",
                "Google Ads",
                "Generative AI search visibility",
            ],
        },
        {
            "@type": meta["type"],
            "@id": f"{canonical}#webpage",
            "url": canonical,
            "name": title,
            "headline": title,
            "description": description,
            "inLanguage": language_code,
            "author": {"@id": f"{BASE_URL}#nana-tan"},
        },
    ]
    if filename == "index.html":
        graph.append(
            {
                "@type": "WebSite",
                "@id": f"{BASE_URL}#website",
                "url": BASE_URL,
                "name": "Nana Tan SEO Portfolio",
                "inLanguage": ["en", "zh-CN"],
                "author": {"@id": f"{BASE_URL}#nana-tan"},
            }
        )
    if meta.get("image"):
        graph[1]["image"] = f"{BASE_URL}{meta['image']}"

    script = etree.SubElement(head, "script", type="application/ld+json")
    script.text = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))


def build_page(source_path: Path, language: str) -> str:
    filename = source_path.name.removesuffix(".template")
    document = html.document_fromstring(source_path.read_text(encoding="utf-8"))
    document = copy.deepcopy(document)
    document.set("lang", "en" if language == "en" else "zh-CN")
    document.attrib.pop("data-lang", None)

    remove_language_nodes(document, language)
    replace_language_switcher(document, filename, language)
    if language == "zh":
        localize_shared_ui(document)
    adjust_asset_paths(document, language)
    add_head_metadata(document, filename, language)

    return html.tostring(
        document,
        encoding="unicode",
        pretty_print=True,
        doctype="<!doctype html>",
    )


def write_search_files() -> None:
    sitemap_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]
    for filename in sorted(PAGE_META):
        for language in ("en", "zh"):
            current_url = page_url(filename, language)
            sitemap_lines.extend(
                [
                    "  <url>",
                    f"    <loc>{current_url}</loc>",
                    f'    <xhtml:link rel="alternate" hreflang="en" href="{page_url(filename, "en")}" />',
                    f'    <xhtml:link rel="alternate" hreflang="zh-CN" href="{page_url(filename, "zh")}" />',
                    f'    <xhtml:link rel="alternate" hreflang="x-default" href="{page_url(filename, "en")}" />',
                    "  </url>",
                ]
            )
    sitemap_lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sitemap_lines) + "\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nDisallow: /source/\n\nSitemap: {BASE_URL}sitemap.xml\n",
        encoding="utf-8",
    )


def main() -> None:
    ZH_DIR.mkdir(exist_ok=True)
    for source_path in sorted(SOURCE_DIR.glob("*.html.template")):
        filename = source_path.name.removesuffix(".template")
        if filename not in PAGE_META:
            raise KeyError(f"Missing metadata for {filename}")
        (ROOT / filename).write_text(build_page(source_path, "en"), encoding="utf-8")
        (ZH_DIR / filename).write_text(build_page(source_path, "zh"), encoding="utf-8")
    write_search_files()


if __name__ == "__main__":
    main()
