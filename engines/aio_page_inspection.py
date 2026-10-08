"""Selected HTML inspection functions from the operating AIO authority radar.

Private strategy, paths, source lists and production delivery are excluded.
Facts about local HTML are not a ranking or attribution model.
"""
from pathlib import Path
import re


def read_text(path: Path, limit: int = 500_000) -> str:
    # The public runner exposes read failures instead of treating them as empty pages.
    return path.read_text(encoding="utf-8")[:limit]

def strip_tags(html: str) -> str:
    return re.sub(r"<[^>]+>", " ", html)

def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()

def tag_attributes(tag: str) -> dict[str, str]:
    """Parse quoted HTML attributes without depending on their order."""
    return {
        match.group(1).lower(): match.group(3)
        for match in re.finditer(r"([:\w-]+)\s*=\s*([\"'])(.*?)\2", tag, re.S)
    }

def first_tag_attribute(html: str, tag_name: str, predicate, value_name: str) -> str:
    for match in re.finditer(rf"<{tag_name}\b[^>]*>", html, re.I | re.S):
        attrs = tag_attributes(match.group(0))
        if predicate(attrs):
            return attrs.get(value_name, "").strip()
    return ""

def parse_html(path: Path, root: Path) -> dict:
    html = read_text(path)
    text = strip_tags(html)
    rel = path.relative_to(root).as_posix()
    title = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.I | re.S)
    canonical = first_tag_attribute(
        html, "link", lambda attrs: "canonical" in attrs.get("rel", "").lower().split(), "href"
    )
    robots = first_tag_attribute(
        html, "meta", lambda attrs: attrs.get("name", "").lower() == "robots", "content"
    )
    schemas = re.findall(r"<script[^>]+type=[\"']application/ld\+json[\"'][^>]*>(.*?)</script>", html, re.I | re.S)
    return {
        "path": rel,
        "title": strip_tags(title.group(1)).strip() if title else "",
        "h1": strip_tags(h1.group(1)).strip() if h1 else "",
        "canonical": canonical,
        "robots": robots,
        "h2_count": len(re.findall(r"<h2\b", html, re.I)),
        "schema_count": len(schemas),
        "has_faq_schema": "FAQPage" in html,
        "has_person_schema": "Person" in html,
        "has_org_schema": "Organization" in html or "MusicGroup" in html,
        "has_video_schema": "VideoObject" in html,
        "has_review_terms": bool(re.search(r"review|testimonial|result|parent|student", text, re.I)),
        "has_proof_terms": bool(re.search(r"example|case study|transcript|video|credit|project|lesson plan|pricing|table", text, re.I)),
        "has_sameas": "sameAs" in html,
        "noindex": "noindex" in robots.lower(),
        "word_count": len(re.findall(r"\w+", text)),
        "text_norm": norm(text[:200_000]),
    }
