"""
validate_output.py — Apple PPT HTML output validator

Usage:
    python validate_output.py <path_to_html_file>

Checks:
1. At least 1 section with data-index
2. Navigation JS present (goTo function)
3. Edit mode present (editToggle button, SLIDE_FIELDS)
4. No external CDN / http links
5. Progress bar + slide counter present
6. data-in elements present (stagger animations)
7. Glass card CSS present (backdrop-filter)
8. At least one data-in element per slide
"""

import sys
import re
from pathlib import Path


def check(name: str, condition: bool, detail: str = "") -> tuple[bool, str]:
    status = "✅" if condition else "❌"
    msg = f"  {status}  {name}"
    if detail:
        msg += f"\n       {detail}"
    return condition, msg


def validate(html_path: str) -> bool:
    path = Path(html_path)
    if not path.exists():
        print(f"❌  File not found: {html_path}")
        return False

    content = path.read_text(encoding="utf-8", errors="replace")
    results = []
    passed = 0

    # 1. Slide sections with data-index
    slides = re.findall(r'<section[^>]*data-index=["\'](\d+)["\']', content)
    slide_count = len(slides)
    ok, msg = check("Slide sections (data-index)", slide_count >= 3,
                    f"Found {slide_count} slides — need at least 3")
    results.append((ok, msg))
    if ok: passed += 1

    # 2. Navigation JS
    has_nav = "function goTo(" in content or "function goTo (" in content
    ok, msg = check("Navigation JS (goTo function)", has_nav)
    results.append((ok, msg))
    if ok: passed += 1

    # 3. Edit mode: toggle button
    has_edit_toggle = 'id="editToggle"' in content or "id='editToggle'" in content
    ok, msg = check("Edit mode toggle button", has_edit_toggle)
    results.append((ok, msg))
    if ok: passed += 1

    # 4. Edit mode: SLIDE_FIELDS
    has_slide_fields = "SLIDE_FIELDS" in content
    ok, msg = check("Edit mode SLIDE_FIELDS defined", has_slide_fields)
    results.append((ok, msg))
    if ok: passed += 1

    # 5. No external CDN links (script src or link href pointing to http)
    ext_links = re.findall(r'(?:src|href)=["\']https?://', content)
    ok, msg = check("No external CDN/HTTP links", len(ext_links) == 0,
                    f"Found external links: {ext_links[:3]}" if ext_links else "")
    results.append((ok, msg))
    if ok: passed += 1

    # 6. Progress bar + counter
    has_progress = 'id="progress"' in content or "id='progress'" in content
    has_counter  = 'id="counter"'  in content or "id='counter'"  in content
    ok, msg = check("Progress bar + slide counter", has_progress and has_counter)
    results.append((ok, msg))
    if ok: passed += 1

    # 7. data-in elements (stagger animations)
    data_in_count = len(re.findall(r'data-in', content))
    ok, msg = check("data-in stagger animation elements", data_in_count >= slide_count,
                    f"Found {data_in_count} data-in across {slide_count} slides")
    results.append((ok, msg))
    if ok: passed += 1

    # 8. Glass card (backdrop-filter)
    has_backdrop = "backdrop-filter" in content
    ok, msg = check("Glass card CSS (backdrop-filter)", has_backdrop)
    results.append((ok, msg))
    if ok: passed += 1

    # 9. SF Pro Display font
    has_font = "SF Pro Display" in content
    ok, msg = check("SF Pro Display font declared", has_font)
    results.append((ok, msg))
    if ok: passed += 1

    # 10. CSS variables present
    has_tokens = "--accent" in content and "--card-bg" in content
    ok, msg = check("CSS design tokens (--accent, --card-bg)", has_tokens)
    results.append((ok, msg))
    if ok: passed += 1

    # 11. Radial gradient background
    has_radial = "radial-gradient" in content
    ok, msg = check("Radial gradient background halo", has_radial)
    results.append((ok, msg))
    if ok: passed += 1

    # 12. Responsive breakpoint
    has_media = "@media" in content and "960px" in content
    ok, msg = check("Responsive @media breakpoint", has_media)
    results.append((ok, msg))
    if ok: passed += 1

    # 13. Nav dots
    has_nav_dots = "nav-dot" in content
    ok, msg = check("Navigation dots (nav-dot class)", has_nav_dots)
    results.append((ok, msg))
    if ok: passed += 1

    # Report
    total = len(results)
    print(f"\n{'='*54}")
    print(f"  Apple PPT HTML Validator")
    print(f"  File: {path.name}")
    print(f"  Slides detected: {slide_count}")
    print(f"{'='*54}")
    for _, msg in results:
        print(msg)
    print(f"{'='*54}")
    score = passed / total * 100
    print(f"  Score: {passed}/{total}  ({score:.0f}%)")

    if passed == total:
        print("  🎉 All checks passed!")
    elif passed >= total * 0.8:
        print("  ⚠️  Minor issues — review failures above.")
    else:
        print("  ❌  Significant issues — fix before delivery.")
    print(f"{'='*54}\n")

    return passed == total


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_output.py <html_file>")
        sys.exit(1)
    success = validate(sys.argv[1])
    sys.exit(0 if success else 1)
